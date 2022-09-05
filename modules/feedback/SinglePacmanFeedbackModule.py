import pathlib
import os
import sys
import time
import subprocess

from pylsl import resolve_byprop

import globals
from modules.module import Module


class SinglePacmanFeedbackModule(Module):

    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "Single Pacman Feedback Module"
    MODULE_DESCRIPTION: str = ""
    MODULE_PATH = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])
    APP_PATH = MODULE_PATH / "SinglePacmanFeedbackApp.py"

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_TASK_EVENTS]

    # overwrite parameter definition which is empty by superclass
    PARAMETER_DEFINITION = [
        {
            'name': 'laterality',
            'displayname': 'Laterality',
            'description': 'Which hand (left/right) is to be represented by the pacman.',
            'type': list,
            'unit': ['left', 'right'],
            'default': 'right'
        },
        {
            'name': 'display_pacman',
            'displayname': 'display pacman',
            'description': 'whether to show or to hide the pacman representing the controlled hand/exoskeleton',
            'type': bool,
            'unit': '',
            'default': False
        },
        {
            'name': 'display_relax',
            'displayname': 'display relax feedback',
            'description': 'whether to show or hide the relax cue text and present a colour changing ball as feedback.',
            'type': bool,
            'unit': '',
            'default': False
        },
        {
            'name': 'window_maximized',
            'displayname': 'window maximized',
            'description': '',
            'type': bool,
            'unit': '',
            'default': True
        },
        {
            'name': 'window_width',
            'displayname': 'window width',
            'description': '',
            'type': int,
            'unit': 'px',
            'default': 1000
        },
        {
            'name': 'window_height',
            'displayname': 'window height',
            'description': '',
            'type': int,
            'unit': 'px',
            'default': 750
        },
        {
            'name': 'window_left',
            'displayname': 'window left',
            'description': '',
            'type': int,
            'unit': 'px',
            'default': 0
        },
        {
            'name': 'window_top',
            'displayname': 'window top',
            'description': '',
            'type': int,
            'unit': 'px',
            'default': 0
        }

    ]


    def __init__(self):
        super(SinglePacmanFeedbackModule, self).__init__()


        self.setStatus(Module.Status.STOPPED)

        self.feedback_app_process = None


    def start(self):

        # do not start up if LSL is not available
        if not globals.LSLAvailable:
            return

        # do not start up if the corresponding app is missing
        if not self.APP_PATH.exists():
            return

        # do not start up the module if it was already started
        if self.getStatus() != Module.Status.STOPPED:
            return

        # set status
        self.setStatus(Module.Status.STARTING)


        # fetch available lsl streams
        resolve_task_stream = resolve_byprop("name", globals.STREAM_NAME_TASK_EVENTS, minimum=1, timeout=10)

        # if the required task output stream is not available -> do not start
        if len(resolve_task_stream) < 1:
            self.setStatus(Module.Status.STOPPED)
            print("Could not start", self.MODULE_NAME,"because of missing stream:", globals.STREAM_NAME_TASK_EVENTS)
            return

        # start the external app process
        self.start_app()

        # set status
        self.setStatus(Module.Status.RUNNING)



    def stop(self):

        # do not stop if not running
        if not self.getStatus() in [Module.Status.RUNNING, Module.Status.STARTING]:
            return

        self.setStatus(Module.Status.STOPPING)

        # stop the feedback app process
        self.stop_app()

        # reset status
        self.setStatus(Module.Status.STOPPED)


    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()


    def start_app(self):

        # convert to str: if pyth is not give as string but as Path-Object -> conversion is necessary
        args = [
            sys.executable,
            str(self.APP_PATH),
            "--side="+self.parameters["laterality"].getValue(),
            "--showpacman="+str(int(self.parameters['display_pacman'].getValue())),
            "--showopen="+str(int(self.parameters['display_relax'].getValue())),
            "--maximized="+str(int(self.getParameter('window_maximized'))),
            "--width="+str(self.getParameter('window_width')),
            "--height=" + str(self.getParameter('window_height')),
            "--left=" + str(self.getParameter('window_left')),
            "--top=" + str(self.getParameter('window_top'))
        ]

        print("START FB APP:", args)

        # start the subprocess
        self.feedback_app_process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stdin=subprocess.PIPE)


    def stop_app(self):
        if self.feedback_app_process is not None:
            self.feedback_app_process.terminate()
            print("Waiting for feedback App to terminate...")
            self.feedback_app_process.wait()
            print("terminated.")
            self.feedback_app_process = None
