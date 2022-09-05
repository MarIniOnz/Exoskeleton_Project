import requests

from pylsl import StreamOutlet, StreamInfo, resolve_byprop

import globals
from misc import NeuroPypeInterface as npi, log
from ..module import Module
from .NeuroPypeBurgSmrPowerModule import NeuroPypeBurgSmrPowerModule
from misc.LSLStreamInfoInterface import add_channel_names, add_parameters

logger = log.getLogger(__name__)

class NeuroPypeBurgSmrPowerPlusHRVModule(NeuroPypeBurgSmrPowerModule):

    MODULE_NAME: str = "NeuroPype Burg SMR-Power + HRV"
    MODULE_DESCRIPTION: str = "Executes HRV pipeline in addition to the data preprocessing pipeline in NeuroPype."

    EXTRA_STREAM = 'hrv'

    PARAMETER_DEFINITION = NeuroPypeBurgSmrPowerModule.PARAMETER_DEFINITION.copy()
    PARAMETER_DEFINITION.extend([
        {
            'name': 'pipeline_hrv',
            'displayname': 'HRV pipeline',
            'description': '',
            'type': list,
            'unit': ['None'] + ["HRVPipeline.pyp"],
            'default': 'HRVPipeline.pyp'
        },
        {
            'name': 'tickrate_hrv',
            'displayname': 'Pipeline update rate',
            'description': '',
            'type': int,
            'unit': 'Hz',
            'default': 1
        },
        {
            'name': 'hrv_window_len',
            'displayname': 'Window length',
            'description': '',
            'type': int,
            'unit': 'sec',
            'default': 100
        },
        {
            'name': 'hrv_shift',
            'displayname': 'Shift window by',
            'description': '',
            'type': int,
            'unit': 'sec',
            'default': 10
        }
    ])

    def __init__(self):
        super().__init__()
        self.execution_id_hrv = None

        self.lsl_stream_info = None
        self.lsl_outlet = None

    def generate_dummy_stream(self):
        # setup dummy stream to be available until NeuroPype produces output
        # generate stream info
        self.lsl_stream_info = StreamInfo(
            name=self.EXTRA_STREAM,
            type='ECG',
            channel_count=2,
            nominal_srate=self.getParameter('tickrate_hrv'),
            channel_format='double64',
            source_id='HRV'
        )

        # add channel names and parameters to stream info
        add_channel_names(self.lsl_stream_info, ['rsa_porges', 'std'])
        add_parameters(self.lsl_stream_info, self.parameters)

        # init LSL outlet
        self.lsl_outlet = StreamOutlet(self.lsl_stream_info, chunk_size=1)
        globals.RECORD_STREAMS.append(self.EXTRA_STREAM)

    def replace_dummy_stream(self):
        # delete dummy stream once NeuroPype's stream produces output
        if len(resolve_byprop('name', self.EXTRA_STREAM, minimum=2, timeout=120)) == 2:
            self.lsl_outlet = None
            return True
        else:
            if self.getStatus() not in [Module.Status.STOPPING, Module.Status.STOPPED]:
                self.stop()
                logger.error(f"{self.MODULE_NAME}: Aborting experiment because stream {self.EXTRA_STREAM} is missing.")
            return False

    def start(self):
        # run parent's start function, then reset status
        super().start()

        if self.getStatus() == Module.Status.RUNNING:

            # if the HRV pipeline should be loaded
            if self.getParameter("hrv") != "None":

                # set status back to starting until the HRV pipeline
                # is configured and running
                self.setStatus(Module.Status.STARTING)

                # create an execution
                self.execution_id_hrv = npi.create_execution(
                    tickrate=self.getParameter("tickrate_hrv"))

                # load the pipeline
                hrv_path = self.MODULE_PATH / 'pipelines_processing' / \
                    self.getParameter("pipeline_hrv")
                try:
                    npi.load_execution_pipeline(
                        self.execution_id_hrv, hrv_path)
                except requests.HTTPError:
                    super().stop()
                    npi.delete_execution(self.execution_id_hrv)
                    self.execution_id_hrv = None
                    logger.error(f"Could not start module {self.MODULE_NAME} because the pipeline could not be loaded.")
                    return

                # get nodes in the pipeline
                nodes = npi.get_execution_nodes(self.execution_id_hrv)
                nodes_dict = nodes_dict = {n['type']: n['id'] for n in nodes}

                try:
                    buffer_id = nodes_dict['SlidingBuffer']
                except KeyError:
                    super().stop()
                    npi.delete_execution(self.execution_id_hrv)
                    self.execution_id_hrv = None
                    logger.error(f"Could not start module {self.MODULE_NAME} because nodes could not be configured.")
                    return

                # adjust window length and shift
                param_window_len = npi.get_execution_node_parameter(
                    self.execution_id_hrv, buffer_id, 'window_length')
                param_window_len['value'] = self.getParameter('hrv_window_len')
                npi.update_execution_node_parameter(
                    self.execution_id_hrv, buffer_id,
                    'window_length', param_window_len)

                param_shift_window = npi.get_execution_node_parameter(
                    self.execution_id_hrv, buffer_id, 'shift_window')
                param_shift_window['value'] = self.getParameter('hrv_shift')
                npi.update_execution_node_parameter(
                    self.execution_id_hrv, buffer_id,
                    'shift_window', param_shift_window)

                # run the pipeline
                npi.run_execution(self.execution_id_hrv)

                logger.info(f"{self.getParameter('pipeline_hrv')} will yield first value in about {self.getParameter('hrv_window_len')} sec...")
                self.generate_dummy_stream()

                # once all pipelines are running, change status to running
                self.setStatus(Module.Status.RUNNING)

                # delete dummy when actual pipeline becomes available else stop
                replaced = self.replace_dummy_stream()
                if not replaced:
                    return

    def stop(self):
        if self.getStatus() != Module.Status.RUNNING:
            return
            
        # run parent's start function, then reset status
        super().stop()
        self.setStatus(Module.Status.STOPPING)

        # if there is a neuropype execution for HRV, delete it, too
        if self.execution_id_hrv is not None:
            npi.stop_execution(self.execution_id_hrv)
            npi.delete_execution(self.execution_id_hrv)
            self.execution_id_hrv = None

            self.lsl_outlet = None
            self.lsl_stream_info = None

            globals.RECORD_STREAMS.remove(self.EXTRA_STREAM)

        # reset status
        self.setStatus(Module.Status.STOPPED)
