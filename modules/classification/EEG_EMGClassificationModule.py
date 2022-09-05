import pathlib
import os
import time
from threading import Thread
import random

from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop

import globals
from modules.module import Module
from misc import LSLStreamInfoInterface,log
logger = log.getLogger("EEG_EMGClassificationModule")


class EEG_EMGClassificationModule(Module):

    MODULE_RUNNABLE: bool = True
    MODULE_NAME: str = "EEG and EMG Classification Module"
    MODULE_DESCRIPTION: str = ""
    MODULE_PATH = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_PREPROCESSED_SIGNAL]

    NUM_OUTPUT_CHANNELS: int = 8
    OUTPUT_SAMPLING_RATE = globals.NEUROPYPE_TICK_RATE
    OUTPUT_CHANNEL_FORMAT = 'float32'
    OUTPUT_CHANNEL_NAMES: list = ['NormOutC3', 'NormOutC4', 'HOVleft', 'HOVright', 'lowMuC3', 'lowMuC4','highEMG', 'lowEMG']


    PARAMETER_DEFINITION = [
        {
            'name': 'ReferenceC3',
            'displayname': 'Reference value C3',
            'description': '',
            'type': float,
            'unit': '',
            'default': 15.0
        },
        {
            'name': 'ReferenceC4',
            'displayname': 'Reference value C4',
            'description': '',
            'type': float,
            'unit': '',
            'default': 15.0
        },
        {
            'name': 'ThresholdC3',
            'displayname': 'Threshold value C3',
            'description': '',
            'type': float,
            'unit': '',
            'default': 0.2
        },
        {
            'name': 'ThresholdC4',
            'displayname': 'Threshold value C4',
            'description': '',
            'type': float,
            'unit': '',
            'default': 0.2
        },
        {
            'name': 'ThresholdEOGleft',
            'displayname': 'Threshold left EOG',
            'description': '',
            'type': int,
            'unit': 'uV',
            'default': 400
        },
        {
            'name': 'ThresholdEOGright',
            'displayname': 'Threshold right EOG',
            'description': '',
            'type': int,
            'unit': 'uV',
            'default': -400
        },
        {
            'name': 'HighThresholdEMG',
            'displayname': 'High Threshold EMG',
            'description': '',
            'type': float,
            'unit': 'uV',
            'default': 70
        },{
            'name': 'LowThresholdEMG',
            'displayname': 'Low Threshold EMG',
            'description': '',
            'type': float,
            'unit': 'uV',
            'default': 30
        }
    ]

    def __init__(self):
        super(EEG_EMGClassificationModule, self).__init__()

        self.setStatus(Module.Status.STOPPED)

        self.lsl_inlet = None # StreamInlet(max_buflen=360, max_chunklen=1, recover=True)
        self.lsl_stream_info = None
        self.lsl_outlet = None # StreamOutlet(streaminfo, chunk_size=1)
        self.emg_inlet = None

        self.worker_thread = None # Thread(target=self.worker_thread, args=(self, self.inlet, self.outlet), daemon=True)
        self.running: bool = False

        self.samples_received: int = 0
        self.samples_sent: int = 0

    # function to be run as a thread. Pulls a sample, hands it over to process_data function and pushes the returned sample
    def worker_thread_func(self):
        # EMG SIGNAL
        emg_stream = resolve_byprop("name", 'MyomoEMG', minimum=1, timeout=30)

        if len(emg_stream) < 1:
            self.setStatus(Module.Status.STOPPED)
            print("Could not start", self.MODULE_NAME, "because of missing stream:", globals.STREAM_NAME_PREPROCESSED_SIGNAL)
            return
        else:
            print('Found EMG stream')

        # init LSL inlet of EMG signal
        self.emg_inlet = StreamInlet(emg_stream[0], max_buflen=360, max_chunklen=1, recover=True)


        last_emg_sample = None
        last_emg_timestamp = None

        while self.running:

            in_sample, in_timestamp = self.lsl_inlet.pull_sample(timeout=1)

            #print("Received EEG", in_sample)

            if in_sample is not None:  # to check for emg because it should take anyway longer

                #have a loop to take only the most recent one, the inlet gives you the oldest only
                while True:

                    emg_sample, emg_timestamp = self.emg_inlet.pull_sample(timeout=0.0)

                    print("EMG", emg_sample)

                    if emg_sample is None:
                        break
                    else:
                        last_emg_sample = emg_sample
                        last_emg_timestamp = emg_timestamp

                if last_emg_sample is None:
                    continue

                # logger.info(last_emg_sample)
                print("EMG", last_emg_sample)
                self.samples_received += 1

                out_sample, out_timestamp = self.process_data(in_sample, in_timestamp, last_emg_sample, last_emg_timestamp)

                if out_sample is not None:

                    if globals.OUTPUT_TRUE_TIMESTAMPS:
                        self.lsl_outlet.push_sample(out_sample)
                    else:
                        self.lsl_outlet.push_sample(out_sample, out_timestamp)

                    self.samples_sent += 1

    # mu-power normalization function
    def normalize_mu_power(self, mu_power, rv):

        return (float(mu_power) / float(rv)) - 1.0

    def process_data(self, sample, timestamp, emg_sample, emg_timestamp):
        # extract single values
        sample_eog = sample[0]
        sample_c3 = sample[1]
        sample_c4 = sample[2]
        sample_emg = emg_sample[1] #0 = arm_extensor #1 = arm_flexor #2= hand_extensor #3=hand_flexor

        # normalize mu-power signals
        sample_c3_norm = self.normalize_mu_power(sample_c3,
                                                 self.parameters['ReferenceC3'].getValue())  # self.PARAM_MU_NORM_RV_C3)
        sample_c4_norm = self.normalize_mu_power(sample_c4,
                                                 self.parameters['ReferenceC4'].getValue())  # self.PARAM_MU_NORM_RV_C4)

        # classify mu-power signals
        lowMuC3 = 1.0 if sample_c3_norm < -self.parameters['ThresholdC3'].getValue() else 0.0
        lowMuC4 = 1.0 if sample_c4_norm < -self.parameters['ThresholdC4'].getValue() else 0.0

        # classify EOG signal
        HOVleft = 1.0 if sample_eog > self.parameters['ThresholdEOGleft'].getValue() else 0.0
        HOVright = 1.0 if sample_eog < self.parameters['ThresholdEOGright'].getValue() else 0.0

        # classify EMG signal
        highEMG = 1.0 if sample_emg > self.parameters['HighThresholdEMG'].getValue() else 0.0
        lowEMG = 1.0 if sample_emg < self.parameters['LowThresholdEMG'].getValue() else 0.0

        # build output sample
        outsample = [sample_c3_norm, sample_c4_norm, HOVleft, HOVright, lowMuC3, lowMuC4, highEMG, lowEMG]
        return (outsample, timestamp)


    def start(self):

        # do not start up the LSL LabRecorder App is not available
        if not globals.LSLAvailable:
            return

        # do not start up the module if it was already started
        if self.status != Module.Status.STOPPED:
            return

        # set status
        self.setStatus(Module.Status.STARTING)

        # reset sample counter
        self.samples_received = 0
        self.samples_sent = 0

        # fetch necessary lsl stream
        #PREPROCESSED DATA
        streams = resolve_byprop("name", globals.STREAM_NAME_PREPROCESSED_SIGNAL, minimum=1, timeout=10)

        if len(streams) < 1:
            self.setStatus(Module.Status.STOPPED)
            print("Could not start", self.MODULE_NAME, "because of missing stream:", globals.STREAM_NAME_PREPROCESSED_SIGNAL)
            return

        # init LSL inlet
        self.lsl_inlet = StreamInlet(streams[0], max_buflen=360, max_chunklen=1, recover=True)

        # generate stream info
        self.lsl_stream_info = StreamInfo(
            globals.STREAM_NAME_CLASSIFIED_SIGNAL,
            'mixed',
            self.NUM_OUTPUT_CHANNELS,
            self.OUTPUT_SAMPLING_RATE,
            self.OUTPUT_CHANNEL_FORMAT,
            'uid'+str(random.randint(100000, 999999))
        )

        # add channel names to stream info
        LSLStreamInfoInterface.add_channel_names(self.lsl_stream_info, self.OUTPUT_CHANNEL_NAMES)

        # add parameters to stream info
        LSLStreamInfoInterface.add_parameters(self.lsl_stream_info, self.parameters)

        # init LSL outlet
        self.lsl_outlet = StreamOutlet(self.lsl_stream_info, chunk_size=1)

        # start worker thread which receives and processes signals
        self.worker_thread = Thread(target=self.worker_thread_func, daemon=True)
        self.running = True
        self.worker_thread.start()

        # set status
        self.setStatus(Module.Status.RUNNING)


    def stop(self):

        # do not try to stop the LSL LabRecorder App if it is not available
        if not globals.LSLAvailable:
            return

        # don't try to stop anything that is already stopped.
        if self.getStatus() is not Module.Status.RUNNING:
            return

        self.setStatus(Module.Status.STOPPING)

        # stop the worker thread
        self.running = False
        print(self.MODULE_NAME + ': Waiting for worker thread to terminate... ')
        while self.worker_thread.is_alive():
            time.sleep(0.1)
        self.worker_thread = None
        print("done.")

        # close the LSL streams
        self.lsl_inlet.close_stream()
        self.emg_inlet.close_stream()
        self.lsl_inlet = None
        self.emg_inlet = None
        self.lsl_outlet = None

        # reset status
        self.setStatus(Module.Status.STOPPED)

        # print(self.MODULE_NAME, ": stopped. {} samples received, {} samples sent.".format(self.samples_received, self.samples_sent))


    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()