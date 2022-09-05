import random
import threading

from pylsl import StreamInfo, StreamInlet, StreamOutlet, resolve_byprop

import globals
from misc.LSLStreamInfoInterface import add_channel_names, add_parameters
from ..module import Module
from .ThresholdClassificationModule import ThresholdClassificationModule
from misc import log

logger = log.getLogger(__name__)

class ThresholdClassificationWithHRVModule(ThresholdClassificationModule):

    MODULE_NAME: str = "Threshold Classification Module + HRV"

    HRV_INPUT_STREAM = 'hrv'
    REQUIRED_LSL_STREAMS = ThresholdClassificationModule.REQUIRED_LSL_STREAMS.copy()
    REQUIRED_LSL_STREAMS.append(HRV_INPUT_STREAM)

    HRV_OUTPUT_STREAM = 'ClassifierOutputHRV'
    HRV_OUTPUT_CHANNEL_NAMES = ['hrv_norm', 'hrv_class']

    PARAMETER_DEFINITION = ThresholdClassificationModule.PARAMETER_DEFINITION.copy()
    HRV_PARAMETERS = [
        {
            'name': 'hrv_type',
            'displayname': 'HRV measure',
            'description': '',
            'type': list,
            'unit': ['hf-porges', 'hf-std'],
            'default': 'hf-std'
        },
        {
            'name': 'hrv_thresh',
            'displayname': 'HRV Threshold',
            'description': 'Threshold below which HRV is considered too low for optimal MI performance.',
            'type': float,
            'unit': '',
            'default': 0.3
        },
    ]
    PARAMETER_DEFINITION.extend(HRV_PARAMETERS)

    def __init__(self):
        super().__init__()

        # add HRV streams
        self.hrv_lsl_inlet = None
        self.hrv_lsl_outlet = None
        self.hrv_lsl_stream_info = None
        self.hrv_worker_thread = None
        
        self.hrv_baseline = None
        
    # function to be run as a thread. Pulls a sample, 
    # hands it over to process_hrv function and pushes the returned sample
    def hrv_worker_thread_func(self):

        while self.running:

            hrv_sample, hrv_timestamp = self.hrv_lsl_inlet.pull_sample(timeout=1)

            if hrv_sample is not None:

                out_sample, out_timestamp = self.process_hrv(hrv_sample, hrv_timestamp)

                if out_sample is not None:

                    if globals.OUTPUT_TRUE_TIMESTAMPS:
                        self.hrv_lsl_outlet.push_sample(out_sample)
                    else:
                        self.hrv_lsl_outlet.push_sample(out_sample, out_timestamp)

    def start(self):
        super().start()  

        if self.getStatus() == Module.Status.RUNNING:

            hrv_stream = resolve_byprop(
                "name", self.HRV_INPUT_STREAM, minimum=1, timeout=1)
            if not hrv_stream:
                super().stop()
                self.setStatus(Module.Status.STOPPED)
                logger.error(f"{self.MODULE_NAME}: Aborting experiment because stream {self.HRV_INPUT_STREAM} is missing.")

                return

            # init LSL inlet
            self.hrv_lsl_inlet = StreamInlet(
                hrv_stream[0], max_buflen=360, max_chunklen=1, recover=True)
            self.hrv_worker_thread = threading.Thread(target=self.hrv_worker_thread_func, daemon=True).start()
                
            # init LSL outlet
            self.hrv_lsl_stream_info = StreamInfo(
                self.HRV_OUTPUT_STREAM,
                'mixed',
                len(self.HRV_OUTPUT_CHANNEL_NAMES),
                10, #TODO: soft-code
                self.OUTPUT_CHANNEL_FORMAT,
                self.HRV_OUTPUT_STREAM+str(random.randint(100000, 999999))
            )

            # add channel names and parameters to stream info
            add_channel_names(self.hrv_lsl_stream_info, self.HRV_OUTPUT_CHANNEL_NAMES)
            add_parameters(
                self.hrv_lsl_stream_info,
                {par['name']: self.parameters[par['name']] for par in self.HRV_PARAMETERS})

            # init LSL outlet
            globals.RECORD_STREAMS.append(self.HRV_OUTPUT_STREAM)
            self.hrv_lsl_outlet = StreamOutlet(self.hrv_lsl_stream_info, chunk_size=1)

    def stop(self):   
        # let parent module stop all regular classifier resources
        super().stop()
        self.setStatus(Module.Status.STOPPING)

        # close all hrv classifier resources
        self.hrv_worker_thread = None
        
        if self.hrv_lsl_inlet:
            self.hrv_lsl_inlet.close_stream()
            self.hrv_lsl_inlet = None
        
        if self.hrv_lsl_outlet:
            self.hrv_lsl_outlet = None
            globals.RECORD_STREAMS.remove(self.HRV_OUTPUT_STREAM)
        
        self.setStatus(Module.Status.STOPPED)           

    # hrv normalization function
    def normalize_hrv(self, hrv, baseline):

        return (float(hrv) / baseline) - 1.0

    # overwrite the process data method to implement the classification
    def process_hrv(self, sample, timestamp):

        # get baseline value at start of HRV stream
        if self.hrv_baseline is None and sample is not None:
            self.hrv_baseline = sample
            self.last_thresh_change = timestamp

        # select the HRV measure to use and normalise HRV
        if self.getParameter('hrv_type') == 'hf-porges':
            sample_norm = self.normalize_hrv(
                sample_hrv[0], self.hrv_baseline[0])

        elif self.getParameter('hrv_type') == 'hf-std':
            sample_norm = self.normalize_hrv(
                sample_hrv[1], self.hrv_baseline[1])

        # classify HRV signal:
        # 0=easy enough, no action required
        # 1=too exhausting, action required
        sample_class = sample_norm <= -self.getParameter('hrv_thresh')

        # return the output sample with the input timestamp
        return ([sample_norm, sample_class], timestamp)