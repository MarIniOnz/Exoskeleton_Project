from typing import List, Union, Dict
from enum import Enum
from threading import Thread
import time

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QComboBox, QLineEdit, QLabel
from PyQt5 import QtCore
from misc.gui import BoldLabel, fireoffFunction
from pylsl import resolve_streams
from misc.timing import clock
import math

from misc import log

logger = log.getLogger("ModuleBaseClass")


class Module(object):
    # whether this is a runnable module or only a blueprint to create runnable module from by extension
    MODULE_RUNNABLE: bool = False

    MODULE_NAME: str = "ModuleBaseClass"
    MODULE_DESCRIPTION: str = "-"

    PARAMETER_DEFINITION: List[dict] = []

    REQUIRED_LSL_STREAMS: List[str] = []

    class Status(Enum):
        DEFAULT = 'default'
        RUNNING = 'running'
        STARTING = 'starting'
        STOPPED = 'stopped'
        STOPPING = 'stopping'

    class Parameter():

        DEFAULT = None
        TYPES = Union[str, float, int, list, bool, 'button']

        # Using button, a button with text 'displayname' will be inserted. You can associate a function call with it
        # by using parameter.input.clicked.connect(<function>)

        def __init__(self, name: str, displayname: str, data_type: type, default_value: TYPES,
                     unit: Union[str, List[str]], description: str = '', value=DEFAULT):

            self.name = name
            self.displayname = displayname
            self.data_type = data_type
            self.default_value = default_value
            self.unit = unit
            self.description = description

            # field to optionally contain a GUI Input later on
            self.input = None

            self.setValue(value)

        def getValue(self) -> TYPES:

            return self.value

        def setValue(self, val: TYPES) -> bool:

            if val == Module.Parameter.DEFAULT:
                self.value = self.default_value
            if type(val) == self.data_type:
                self.value = val
                return True
            if self.data_type is list and val in self.unit:
                self.value = val
                return True
            return False

        def __str__(self):
            return "Parameter(name: '{}', type: {}, value: '{}', unit: '{}' default: '{}', description: '{}')".format(
                self.name, self.data_type, self.value, self.unit, self.default_value, self.description)

        def __repr__(self):
            return self.__str__()

    def __init__(self):

        self.status: str = Module.Status.DEFAULT
        self.parameters: Dict[Module.Parameter] = {}
        self.running_since: float = clock()

        # initiate parameters
        for p in self.PARAMETER_DEFINITION:
            self.parameters[p['name']] = Module.Parameter(p['name'], p['displayname'], p['type'], p['default'],
                                                          p['unit'], p['description'])

        # init gui
        self.gui = None

        # observe required streams
        d = Thread(daemon=True, target=self.stopIfStreamMissingDaemon)
        d.start()

        # start daemon to update GUI every second
        t = Thread(daemon=True, target=self.updateGuiSecondly)
        t.start()

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status):

        # set status
        self.status = status

        # update GUI depeding on status
        if self.gui is not None:
            self.status_label.setText(self.status.value)
            if status is Module.Status.RUNNING:
                self.status_label.setStyleSheet('QLabel{ color: green;}')
            else:
                self.status_label.setStyleSheet('QLabel{ color: black;}')

            # set parameter inputs en/disabled depending on state
            if status is Module.Status.STOPPED:
                self.setInputsEnabled(True)
            else:
                self.setInputsEnabled(False)

            # set start button en/disabled depending on state
            if status is Module.Status.STOPPED:
                self.btn_start.setEnabled(True)
            else:
                self.btn_start.setEnabled(False)

            # set stop and restart buttons en/disabled depending on state
            if status is Module.Status.RUNNING:
                self.btn_stop.setEnabled(True)
                self.btn_restart.setEnabled(True)
                self.running_since = clock()
            else:
                # Note: changing the order of the following two lines prevents the application from
                # crashing without any error from time to time when hitting the "STOP" button
                self.btn_restart.setEnabled(False)
                self.btn_stop.setEnabled(False)

    def getParameter(self, key: str) -> Parameter.TYPES:
        try:
            return self.parameters[key].getValue()
        except KeyError:
            return None

    def setParameter(self, key: str, val: Union[str, float, int]) -> bool:

        # don't change parameters while the module is running
        if self.getStatus() == Module.Status.RUNNING:
            return False

        # don't set any parameters that don't exist
        if not key in self.parameters.keys():
            return False

        # set value
        return self.parameters[key].setValue(val)

    # creates a GUI Widget displaying the module's status and allowing to adjust its parameters
    def initGui(self):

        self.gui = QWidget()
        self.gui.setObjectName("ModuleGUI " + self.MODULE_NAME)
        self.status_label = QLabel(self.status.value)
        self.status_label.setAlignment(QtCore.Qt.AlignRight)
        self.running_since_label = QLabel("")
        self.running_since_label.setAlignment(QtCore.Qt.AlignRight)

        # create a grid layout
        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(3)
        self.layout.setHorizontalSpacing(3)

        # add the module's name as a label as well as its status
        l = BoldLabel(self.MODULE_NAME)
        l.setToolTip(
            '<br />Module Description:<br /><b>' + self.MODULE_NAME + '</b><hr /><pre>' + self.MODULE_DESCRIPTION + '</pre>')
        self.layout.addWidget(l, 0, 0, 1, 3)
        self.layout.addWidget(self.status_label, 0, 3, 1, 1)
        self.layout.addWidget(self.running_since_label, 0, 4, 1, 1)

        # create three buttons to control the module
        self.btn_start = QPushButton("start")
        self.btn_stop = QPushButton("stop")
        self.btn_restart = QPushButton("restart")

        # connect the actions
        self.btn_start.clicked.connect(lambda: fireoffFunction(self.start))
        self.btn_stop.clicked.connect(lambda: fireoffFunction(self.stop))
        self.btn_restart.clicked.connect(lambda: fireoffFunction(self.restart))

        # add the buttons to the layout in a single row
        sublayout = QHBoxLayout()
        sublayout.addWidget(self.btn_start)
        sublayout.addWidget(self.btn_stop)
        sublayout.addWidget(self.btn_restart)
        self.layout.addLayout(sublayout, 1, 0, 1, 5)

        # if there are any parameters for this module, create inputs for them
        if len(self.parameters) > 0:

            self.layout.addWidget(BoldLabel("Parameters:"), 2, 0, 1, 5)

            row = 3

            for n, p in self.parameters.items():

                parameter_display_name = p.displayname
                if type(p.unit) is str and len(p.unit) >= 1:
                    parameter_display_name += " (" + p.unit + ")"
                self.layout.addWidget(QLabel(parameter_display_name), row, 0, 1, 2)

                if p.data_type is list:
                    p.input = QComboBox()
                    p.input.addItems(p.unit)
                    p.input.setCurrentIndex(p.input.findText(p.getValue()))
                    p.input.activated.connect(lambda: self.updateParametersFromGUI())

                elif p.data_type is bool:
                    p.input = QCheckBox()
                    p.input.setChecked(p.getValue())
                    p.input.stateChanged.connect(lambda: self.updateParametersFromGUI())

                elif p.data_type == 'button':
                    p.input = QPushButton(p.displayname)

                else:
                    p.input = QLineEdit(str(p.getValue()))
                    p.input.textEdited.connect(lambda: self.updateParametersFromGUI())

                self.layout.addWidget(p.input, row, 2, 1, 3)

                row += 1

        self.gui.setLayout(self.layout)

    def getGUI(self) -> QWidget:

        if self.gui is None:
            self.initGui()

        self.setStatus(self.getStatus())

        return self.gui

    def setInputsEnabled(self, en: bool):

        for n, p in self.parameters.items():
            p.input.setEnabled(en)

    def updateParametersFromGUI(self):

        COLOR_GOOD = "#ffffff";
        COLOR_BAD = "#ff8844";

        for n, p in self.parameters.items():

            if p.data_type is list:

                p.setValue(p.input.currentText())

            elif p.data_type is bool:

                p.setValue(p.input.isChecked())

            elif p.data_type is int:

                try:
                    val = int(p.input.text())
                    p.setValue(val)
                    p.input.setStyleSheet("QLineEdit{ background-color: %s;}" % COLOR_GOOD)
                except:
                    print(n, "could not convert to int")
                    p.input.setStyleSheet("QLineEdit{ background-color: %s; }" % COLOR_BAD)


            elif p.data_type is float:

                try:
                    val = float(p.input.text())
                    p.setValue(val)
                    p.input.setStyleSheet("QLineEdit{ background-color: %s; }" % COLOR_GOOD)
                except:
                    print(n, "could not convert to float")
                    p.input.setStyleSheet("QLineEdit{ background-color: %s; }" % COLOR_BAD)

            elif p.data_type == 'button':
                pass

            elif p.data_type is str:

                p.setValue(p.input.text())

    def updateGuiSecondly(self):

        while True:

            time.sleep(1)

            # do not do anything if there is no GUI (yet)
            if self.gui is None:
                continue

            # if module is running
            if self.getStatus() is Module.Status.RUNNING:

                # update the runnig since label
                running_seconds = clock() - self.running_since
                if running_seconds >= 60:
                    self.running_since_label.setText(
                        "{:d}m {:02.0f}s".format(math.floor(running_seconds / 60), running_seconds % 60))
                else:
                    self.running_since_label.setText("{:02.0f}s".format(clock() - self.running_since))

            # if module is starting, empty the running since label
            elif self.getStatus() is Module.Status.STARTING:
                self.running_since_label.setText("")

    # function to be run by a daemon which checks every few seconds wether a specified lsl stream
    # is available, else it stops the module
    def stopIfStreamMissingDaemon(self):
        while True:
            if self.getStatus() is Module.Status.RUNNING and len(self.REQUIRED_LSL_STREAMS) > 0:
                if not self.lslStreamsAvailable(self.REQUIRED_LSL_STREAMS, wait_time=2.0):
                    if self.getStatus() is Module.Status.RUNNING:
                        logger.error(
                            f"Stopping module {self.MODULE_NAME} because of missing LSL streams: {self.REQUIRED_LSL_STREAMS}")
                        self.stop()

            else:
                time.sleep(2)

            time.sleep(3)

    # checks wether lsl streams with given names are available
    def lslStreamsAvailable(self, stream_names: List[str], wait_time=1.0):

        streams = resolve_streams(wait_time=wait_time)
        names = list(map(lambda x: x.name(), streams))

        for name in stream_names:

            if not name in names:
                return False

        return True
