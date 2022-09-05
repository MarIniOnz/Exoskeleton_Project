import pathlib
import os
import time
from typing import List, Union
import subprocess

import pylsl

import globals
from modules.module import Module

from misc import log

logger = log.getLogger("LabRecorderModule")

class LabRecorderModule(Module):
    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "LabRecorder Module"
    MODULE_DESCRIPTION: str = "Automatically controls the LSL LabRecorder App to record all LSL streams configured."
    MODULE_PATH = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])

    REQUIRED_LSL_STREAMS = []

    # overwrite parameter definition which is empty by superclass
    PARAMETER_DEFINITION = [
        {
            'name': 'Study',
            'displayname': 'Study',
            'description': '',
            'type': str,
            'unit': '',
            'default': 'BCISTUDY'
        },
        {
            'name': 'Subject',
            'displayname': 'Subject',
            'description': '',
            'type': str,
            'unit': '',
            'default': 'P01'
        },
        {
            'name': 'Task',
            'displayname': 'Task',
            'description': '',
            'type': str,
            'unit': '',
            'default': 'Task_1'
        },
        {
            'name': 'Run',
            'displayname': 'Run',
            'description': '',
            'type': int,
            'unit': '',
            'default': 1
        },
        {
            'name': 'require_streams',
            'displayname': 'Require default streams',
            'description': '',
            'type': bool,
            'unit': '',
            'default': True
        },
        {
            'name': 'record_all_streams',
            'displayname': 'Record all available streams',
            'description': '',
            'type': bool,
            'unit': '',
            'default': False
        }
    ]

    def __init__(self):
        super(LabRecorderModule, self).__init__()

        self.setStatus(Module.Status.STOPPED)

        self.labrecorder_output: List[str] = []

        self.labrecorder_process = None


    def start(self):

        # do not start up the LSL LabRecorder App is not available
        if not globals.LabRecorderAvailable:
            logger.error("LabRecorder is not available.")
            return

        # do not start up the module if it was already started
        if self.status != Module.Status.STOPPED:
            return

        # set status
        self.setStatus(Module.Status.STARTING)


        # check wether study name and subject name are specified
        if len(self.parameters["Study"].getValue()) < 1 or len(self.parameters["Subject"].getValue()) < 1 or len(self.parameters["Task"].getValue()) < 1 or self.getParameter("Run") < 1:
            self.setStatus(Module.Status.STOPPED)
            logger.error(f"Could not start {self.MODULE_NAME} because no study name or subject name were specified.")
            return


        # check whether recording data folder exists
        if not (globals.DATA_PATH.exists() and globals.DATA_PATH.is_dir()):
            os.mkdir(str(globals.DATA_PATH))

            if not (globals.DATA_PATH.exists() and globals.DATA_PATH.is_dir()):
                self.setStatus(Module.Status.STOPPED)
                logger.error(f"Could not start {self.MODULE_NAME} because data directory is missing and could not be created.")
                return

        # create study folder if not exists
        study_path = globals.DATA_PATH / self.parameters["Study"].getValue()

        if not (study_path.exists() and study_path.is_dir()):
            os.mkdir(str(study_path))

            if not (study_path.exists() and study_path.is_dir()):
                self.setStatus(Module.Status.STOPPED)
                logger.error(f"Could not start {self.MODULE_NAME} because the study directory is missing and could not be created.")
                return

        # create subject folder if not exists
        subject_path = study_path / self.parameters["Subject"].getValue()

        if not (subject_path.exists() and subject_path.is_dir()):
            os.mkdir(str(subject_path))

            if not (subject_path.exists() and subject_path.is_dir()):
                self.setStatus(Module.Status.STOPPED)
                logger.error(f"Could not start {self.MODULE_NAME} because the subject directory is missing and could not be created.")
                return


        # check whether required lsl streams are available
        if self.getParameter('require_streams') and not self.lslStreamsAvailable(globals.RECORD_STREAMS, wait_time=10.0):
            self.setStatus(Module.Status.STOPPED)
            logger.error(f"Could not start {self.MODULE_NAME} because of missing stream(s).")
            return


        # create file path
        filename = "{}_{:02d}.xdf".format(self.getParameter("Task"), self.getParameter("Run"))
        xdf_path = subject_path / filename

        # if there exists already an xdf file -> rename it by increasing the Run number
        if xdf_path.exists():

            while True:

                # increase run number by 1
                self.setParameter("Run", self.getParameter("Run")+1)

                # update filename and complete file path
                filename = "{}_{:02d}.xdf".format(self.getParameter("Task"), self.getParameter("Run"))
                xdf_path = subject_path / filename

                # stop increasing the run number if a free one was found
                if not xdf_path.exists():
                    break

            # update value in GUI
            self.parameters["Run"].input.setText(str(self.getParameter("Run")))

            # if file still exists after renaming
            if xdf_path.exists():
                self.setStatus(Module.Status.STOPPED)
                logger.error(f"Could not start {self.MODULE_NAME} because xdf file already exists and could not be renamed.")
                return


        # select streams to be recorded
        record_streams = []
        available_streams = [x.name() for x in pylsl.resolve_streams(wait_time=1.0)]

        if self.getParameter('require_streams') and not self.getParameter('record_all_streams'):
            record_streams = globals.RECORD_STREAMS

        elif not self.getParameter('require_streams') and not self.getParameter('record_all_streams'):

            for stream_name in available_streams:
                if stream_name in globals.RECORD_STREAMS:
                    record_streams.append(stream_name)

        elif self.getParameter('record_all_streams'):
            record_streams = available_streams

        # start the labrecorder process
        self.start_labrecorder(record_stream_names=record_streams, out_xdf_path=xdf_path)

        # set the required streams attribute to make the LabRecorder stop automatically
        LabRecorderModule.REQUIRED_LSL_STREAMS = record_streams

        # set status
        self.setStatus(Module.Status.RUNNING)


    def stop(self):

        # do not try to stop if already stopped
        if self.getStatus() is Module.Status.STOPPED or self.getStatus() is Module.Status.STOPPING:
            return

        # do not try to stop the LSL LabRecorder App if it is not available
        if not globals.LabRecorderAvailable:
            return

        self.setStatus(Module.Status.STOPPING)

        # stop the labrecorder process
        self.stop_labrecorder()

        # reset status
        self.setStatus(Module.Status.STOPPED)


    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()


    def start_labrecorder(self, record_stream_names, out_xdf_path: Union[str,pathlib.Path]):

        # convert to str: if pyth is not give as string but as Path-Object -> conversion is necessary
        args = [str(globals.LABRECORDER_CLI_EXE), str(out_xdf_path)]

        # append stream names to the parameter array
        for n in record_stream_names:
            args.append("name='" + n + "'")

        # start the subprocess
        self.labrecorder_process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stdin=subprocess.PIPE)


    def stop_labrecorder(self):
        if self.labrecorder_process is None:
            return
        print("LabRecorder stop:", self.labrecorder_process.communicate(b"\n"))
        self.labrecorder_process = None


    def readline_labrecorder(self):
        return self.labrecorder_process.stdout.readline()
