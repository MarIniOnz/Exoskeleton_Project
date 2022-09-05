import pathlib
import os
import time

import globals
from misc import NeuroPypeInterface as npi, log
from modules.module import Module

logger = log.getLogger("NeuroPypeBurgSmrPowerModule")

class NeuroPypeBurgSmrPowerModule(Module):
    
    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "NeuroPype Burg SMR-Power"
    MODULE_DESCRIPTION: str = "Executes the data preprocessing pipeline in NeuroPype."

    MODULE_PATH = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])
    PIPELINE_PATH = MODULE_PATH / 'SMR-ERD-Pipeline.pyp'
    PIPELINE_VISUALS_PATH = MODULE_PATH / 'SMR-ERD-Pipeline+Visuals.pyp'

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_RAW_SIGNAL]

    PREPROCESSING_PIPELINES = [ x.name for x in list(os.scandir(str(MODULE_PATH / "pipelines_processing"))) if x.name.endswith(".pyp") ]
    VISUALIZATION_PIPELINES = [ x.name for x in list(os.scandir(str(MODULE_PATH / "pipelines_visualization"))) if x.name.endswith(".pyp") ]

    # overwrite parameter definition which is empty by superclass
    PARAMETER_DEFINITION = [    
        {
            'name': 'pipeline',
            'displayname': 'Pipeline',
            'description': '',
            'type': list,
            #'unit': ['BurgBothHandsPlusEOG.pyp', 'BurgLeftHandPlusEOG.pyp', 'BurgRightHandPlusEOG.pyp'],
            #'default': 'BurgBothHandsPlusEOG.pyp'
            'unit': ['None'] + PREPROCESSING_PIPELINES,
            'default': PREPROCESSING_PIPELINES[1]
        },
        {
            'name': 'tickrate',
            'displayname': 'Pipeline update rate',
            'description': '',
            'type': int,
            'unit': 'Hz',
            'default': int(globals.NEUROPYPE_TICK_RATE)
        },
        {
            'name': 'pipeline_visualization',
            'displayname': 'Visualization pipeline',
            'description': '',
            'type': list,
            'unit': ['None'] + VISUALIZATION_PIPELINES,
            'default': 'None'
        },
        {
            'name': 'tickrate_vis',
            'displayname': 'Visualization update rate',
            'description': 'decreasing reduces power consumption drastically.',
            'type': int,
            'unit': 'Hz',
            'default': 10
        },
        {
            'name': 'FOI',
            'displayname': 'Frequency of interest',
            'description': '',
            'type': float,
            'unit': 'Hz',
            'default': 11.0
        }
    ]

    def __init__(self):
        super(NeuroPypeBurgSmrPowerModule, self).__init__()

        self.setStatus(Module.Status.STOPPED)
        self.execution_id = None
        self.execution_id_vis = None
        self.started = None


    def start(self):

        # do not start up the module if Neuropype is not available or not started yet
        if not globals.NeuroPypeAvailable or not npi.neuropype_api_available():
            return

        # do not start up the module if it was already started
        if self.status != Module.Status.STOPPED:
            return

        # do not start up the module if no pipeline is selected
        if self.getParameter("pipeline") == "None":
            return

        # set status
        self.setStatus(Module.Status.STARTING)

        # check for required LSL streams
        if not self.lslStreamsAvailable(self.REQUIRED_LSL_STREAMS):
            self.setStatus(Module.Status.STOPPED)
            logger.error(f"Could not start module {self.MODULE_NAME} because of missing lsl stream(s).")
            return


        # create an execution
        self.execution_id = npi.create_execution(tickrate = self.getParameter("tickrate"))

        # load the pipeline
        npi.load_execution_pipeline(self.execution_id, self.MODULE_PATH / "pipelines_processing" / self.getParameter("pipeline"))

        # get nodes in the pipeline
        nodes = npi.get_execution_nodes(self.execution_id)

        #node_lsl_input = None
        #node_lsl_output = None
        node_burg_spectrum = None

        # find the LSL input and output nodes
        for n in nodes:

            # find the LSL Input Node
            #if n['type'] == 'LSLInput':
            #    node_lsl_input = n

            #if n['type'] == 'LSLOutput':
            #    stream_name = npi.get_execution_node_parameter(self.execution_id, n['id'], 'stream_name')['value']
            #    if stream_name == 'PreprocessedData':
            #        node_lsl_output = n

            if n['type'] == 'BurgSpectrum':
                node_burg_spectrum = n

        #print(node_lsl_input, node_lsl_output, node_burg_spectrum)

        # if the lsl nodes could not be found, stop execution
        #if node_lsl_input is None or node_lsl_output is None or node_burg_spectrum is None:
        if node_burg_spectrum is None:
            self.setStatus(Module.Status.STOPPED)
            npi.delete_execution(self.execution_id)
            self.execution_id = None
            logger.error(f"Could not start module {self.MODULE_NAME} because nodes could not be configured.")
            return

        # adjust the input stream query
        #param_query = npi.get_execution_node_parameter(self.execution_id, node_lsl_input['id'], 'query')
        #param_query['value'] = "type='EEG' and name='" + globals.STREAM_NAME_RAW_SIGNAL + "'"
        #npi.update_execution_node_parameter(self.execution_id, node_lsl_input['id'], 'query', param_query)

        # adjust the output stream's name
        #param_stream_name = npi.get_execution_node_parameter(self.execution_id, node_lsl_output['id'], 'stream_name')
        #param_stream_name['value'] = globals.STREAM_NAME_PREPROCESSED_SIGNAL
        #npi.update_execution_node_parameter(self.execution_id, node_lsl_output['id'], 'stream_name', param_stream_name)

        # adjust the frequency of interes
        param_foi = npi.get_execution_node_parameter(self.execution_id, node_burg_spectrum['id'], 'foi')
        param_foi['value'] = self.getParameter('FOI')
        npi.update_execution_node_parameter(self.execution_id, node_burg_spectrum['id'], 'foi', param_foi)

        # run the pipeline
        npi.run_execution(self.execution_id)


        # if there is an additional pipeline for visualizations to be loaded
        if self.getParameter("pipeline_visualization") != "None":

            # create an execution
            self.execution_id_vis = npi.create_execution(tickrate = self.getParameter("tickrate_vis"))

            # load the pipeline
            npi.load_execution_pipeline(self.execution_id_vis, self.MODULE_PATH / "pipelines_visualization" / self.getParameter("pipeline_visualization"))

            # run the pipeline
            npi.run_execution(self.execution_id_vis)


        # set status
        self.setStatus(Module.Status.RUNNING)


    def stop(self):

        # do not try to stop the module if it is not even running
        if self.getStatus() != Module.Status.RUNNING:
            return

        # do not call any NeuroPype API functions if NeuroPype is not available
        if not globals.NeuroPypeAvailable or not npi.neuropype_api_available():
            return

        self.setStatus(Module.Status.STOPPING)

        # stop the pipeline
        npi.stop_execution(self.execution_id)

        # delete the NeuroPype instance
        npi.delete_execution(self.execution_id)

        # reset execution id
        self.execution_id = None

        # if there is a neuropype execution for visuals, delete it, too
        if self.execution_id_vis is not None:
            npi.stop_execution(self.execution_id_vis)
            npi.delete_execution(self.execution_id_vis)
            self.execution_id_vis = None

        # reset status
        self.setStatus(Module.Status.STOPPED)


    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()
