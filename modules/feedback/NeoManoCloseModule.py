import time
import random
from threading import Thread
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit

import globals
from misc import enums, log
from misc.timing import clock
from modules.module import Module
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop, IRREGULAR_RATE
from misc.LSLStreamInfoInterface import add_channel_names, add_parameters, add_mappings
from misc.gui import BoldLabel

import serial
from serial.tools import list_ports

logger = log.getLogger("NeoManoCloseModule")


class NeoManoCloseModule(Module):
    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "Neo Mano Control Module"
    MODULE_DESCRIPTION: str = ""
    # MODULE_PATH = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])
    # APP_PATH = MODULE_PATH / "SinglePacmanFeedbackApp.py"

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_TASK_EVENTS]

    # parameters of LSL outlet
    OUTPUT_STREAM_NAME = globals.STREAM_NAME_FEEDBACK_STATES
    NUM_OUTPUT_CHANNELS: int = 1
    OUTPUT_CHANNEL_NAMES = ['command_sent']
    OUTPUT_SAMPLING_RATE: float = IRREGULAR_RATE
    OUTPUT_CHANNEL_FORMAT: str = 'int32'

    # overwrite parameter definition which is empty by superclass
    PARAMETER_DEFINITION = [
        {
            'name': 'laterality',
            'displayname': 'Laterality',
            'description': 'On which side (left/right) is the exoskeleton mounted?',
            'type': list,
            'unit': [enums.Side.LEFT.value, enums.Side.RIGHT.value],
            'default': enums.Side.RIGHT.value
        },
        {
            'name': 'send_open_time',
            'displayname': 'Time on opening the hand',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 8.0
        },
    ]

    # machine states
    STATE_SEND_LOCK = 0
    STATE_SEND_OPEN = 1
    STATE_SEND_CLOSE = 2
    STATE_STOP = 3
    STATE_READY = 4
    STATE_START = 5
    STATE_INACTIVE = 6

    # exo commands
    EXO_COMMAND_STOP = b'0'
    EXO_COMMAND_CLOSE = b'1'
    EXO_COMMAND_OPEN = b'2'

    def __init__(self):

        super(NeoManoCloseModule, self).__init__()
        self.state = None
        self.setStatus(Module.Status.STOPPED)

        self.lsl_inlet = None
        self.lsl_outlet = None
        self.lsl_stream_info = None

        self.running = False
        self.datathread = None
        self.mute_output = False
        self.socket = None

        self.last_msg_sent = None
        self.last_msg_time = None

        self.btn = None

        self.time_start_open = 0.3  # short time for sending open command in the ready state
        self.exo_start = False

        # Separate flows of execution: two things happening at once.
        self.state_machine_thread = Thread(target=self.state_machine, daemon=True)
        # You create a thread and then you start it.
        self.state_machine_thread.start()

        self.state_machine_state = 4
        self.state_machine_state_change_time = clock()

        self.last_command_sent_to_exo = b''
        self.last_command_sent_to_exo_time = clock()

        self.list_commands = []
        self.cdc = None

        try:
            self.cdc = next(list_ports.grep("VID:PID=10C4:EA60"))

        except:
            pass

        if self.cdc is None:
            logger.error("No dongle found")
        else:
            self.ser = serial.Serial(port=self.cdc.device, baudrate=115200, bytesize=serial.EIGHTBITS,
                                     parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None,
                                     xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False,
                                     inter_byte_timeout=None, exclusive=None)
            logger.info(f"Dongle detected at port: {self.ser.name}")

    def initGui(self):

        super(NeoManoCloseModule, self).initGui()
        row: int = self.layout.rowCount()

        # entry box for entering a command
        self.state = QLineEdit()

        # push button and connect that to the Action function
        btn_send = QPushButton("Action", clicked=lambda: [self.Action()])
        btn_send.setAutoDefault(True)

        label = QLabel("Enter a command!\n[LOCK: 0, OPEN: 1, CLOSE: 2]")
        label.setWordWrap(True)

        self.layout.addWidget(BoldLabel("Actions"), row + 1, 0, 1, 4)
        self.layout.addWidget(label, row + 6, 0, 1, 5)
        self.layout.addWidget(self.state, row + 7, 0, 1, 1)
        self.layout.addWidget(btn_send, row + 7, 2, 1, 2)

    def handle_input(self):

        self.last_relevant_exo_state = None

        while self.running:

            in_sample, in_timestamp = self.lsl_inlet.pull_sample(timeout=1)

            if in_sample is not None:

                out_sample, out_timestamp = (None, in_timestamp)  # self.process_data(in_sample, in_timestamp)

                # split the input samples into a readable form
                cue = enums.Cue(in_sample[0])
                left_exo_state = enums.ExoState(in_sample[1])
                right_exo_state = enums.ExoState(in_sample[2])

                # choose the relevant exo-state based on the selected laterality
                relevant_exo_state = None

                if self.getParameter('laterality') == enums.Side.LEFT.value:

                    relevant_exo_state = left_exo_state

                elif self.getParameter('laterality') == enums.Side.RIGHT.value:

                    relevant_exo_state = right_exo_state

                if relevant_exo_state != self.last_relevant_exo_state:

                    # logger.info("RECV:"+relevant_exo_state.name)

                    # send Message

                    if relevant_exo_state == enums.ExoState.OPEN:

                        self.state_machine_state = self.STATE_SEND_OPEN
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.CLOSE:

                        self.state_machine_state = self.STATE_SEND_CLOSE
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.STOP:

                        self.state_machine_state = self.STATE_STOP
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.LOCK:

                        self.state_machine_state = self.STATE_SEND_LOCK
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.START:

                        self.state_machine_state = self.STATE_START
                        self.state_machine_state_change_time = clock()

                self.last_relevant_exo_state = relevant_exo_state

    def start(self):
        # do not start if the LSL LabRecorder App is not available
        if not globals.LSLAvailable:
            return

        # do not start up the module if it was already started
        if self.status != Module.Status.STOPPED:
            return

        # set status
        self.setStatus(Module.Status.STARTING)

        # fetch necessary lsl stream
        streams = resolve_byprop("name", globals.STREAM_NAME_TASK_EVENTS, minimum=1, timeout=10)

        if len(streams) < 1:
            self.setStatus(Module.Status.STOPPED)
            logger.error(
                f"Could not start {self.MODULE_NAME} because of missing stream: {globals.STREAM_NAME_CLASSIFIED_SIGNAL}")
            return

        # init LSL inlet
        self.lsl_inlet = StreamInlet(streams[0], max_buflen=360, max_chunklen=1, recover=True)

        # create stream info for lsl outlet
        self.lsl_stream_info = StreamInfo(
            globals.STREAM_NAME_FEEDBACK_STATES,
            'mixed',
            self.NUM_OUTPUT_CHANNELS,
            self.OUTPUT_SAMPLING_RATE,
            self.OUTPUT_CHANNEL_FORMAT,
            'uid' + str(random.randint(100000, 999999))
        )

        # add channel names and mappings to stream info
        add_channel_names(self.lsl_stream_info, self.OUTPUT_CHANNEL_NAMES)
        add_mappings(self.lsl_stream_info, ['cues', 'exo_states'], [enums.Cue, enums.ExoState])
        add_parameters(self.lsl_stream_info, self.parameters)

        # init LSL outlet
        self.lsl_outlet = StreamOutlet(self.lsl_stream_info, chunk_size=1)

        # set running true to signal threads to continue running
        self.running = True

        # create thread to handle lsl input
        self.datathread = Thread(target=self.handle_input, daemon=True)
        self.datathread.start()

        # set status
        self.setStatus(Module.Status.RUNNING)

    def stop(self):

        # do not try to stop if not even running
        if self.getStatus() != Module.Status.RUNNING:
            return

        self.setStatus(Module.Status.STOPPING)

        # set the running flag to false which signals threads to stop
        self.running = False

        # stop data thread
        # print(self.MODULE_NAME + ': Waiting for data handling thread to terminate... ')
        logger.info(f"Waiting for data handling thread to terminate...")
        while self.datathread is not None and self.datathread.is_alive():
            time.sleep(0.1)
        print("done.")

        # clear reference to threads
        self.datathread = None

        # close lsl connections
        if self.lsl_inlet is not None:
            self.lsl_inlet.close_stream()
        self.lsl_inlet = None
        self.lsl_outlet = None

        # set status
        self.setStatus(Module.Status.STOPPED)
        self.ser.close()
        logger.info(f"Module {self.MODULE_NAME} stopped")

    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()

    def exo_open(self):
        self.ser.write(b'2')

    def exo_close(self):
        self.ser.write(b'1')

    def exo_stop(self):
        self.ser.write(b'3')

    def commands_exo(self, command_type: int):
        if command_type == 0:
            self.exo_open()
        # Grasping.
        elif command_type == 1:
            self.exo_close()
        # STOP
        elif command_type == 3:
            self.exo_stop()

    def send_command_to_exo(self, command_type: int):
        self.list_commands.append(command_type)

        # time since last state change
        time_since_last_command = clock() - self.last_command_sent_to_exo_time

        if time_since_last_command >= 0.2:

            while len(self.list_commands) > 0:

                current_command = self.list_commands.pop(0)

                # TODO: Calibrate this time, ask Annalisa and test needed.
                # if current_command == self.last_command_sent_to_exo and time_since_last_command < 3.5:
                #     continue

                try:
                    self.commands_exo(command_type)
                    self.last_command_sent_to_exo = current_command
                    self.last_command_sent_to_exo_time = clock()
                    if self.lsl_outlet is not None:
                        self.lsl_outlet.push_sample([0], clock())

                except:
                    pass

                break

    def state_machine(self):

        while True:
            time.sleep(0.01)

            time_since_state_change = clock() - self.state_machine_state_change_time

            # start
            # TODO: Do not know whether any step is required at the start.
            if self.state_machine_state == self.STATE_START:

                self.send_command_to_exo(1)

                if time_since_state_change > self.time_start_open:
                    self.state_machine_state = self.STATE_STOP
                    self.state_machine_state_change_time = clock()

            # stop
            elif self.state_machine_state == self.STATE_STOP:
                self.send_command_to_exo(3)

            # lock
            elif self.state_machine_state == self.STATE_SEND_LOCK:
                self.send_command_to_exo(3)

            # close
            elif self.state_machine_state == self.STATE_SEND_CLOSE:
                self.send_command_to_exo(1)

            # open
            elif self.state_machine_state == self.STATE_SEND_OPEN:
                self.send_command_to_exo(0)

                if time_since_state_change > self.getParameter('send_open_time'):
                    self.state_machine_state = self.STATE_STOP
                    self.state_machine_state_change_time = clock()

    # sends a command to the exoskeleton
    def Action(self):

        # close
        if str(self.state.text()) == "2":
            self.send_command_to_exo(1)
            # self.ser.write(b'2')
            # self.state_machine_s1tate = self.STATE_SEND_CLOSE
            # self.state_machine_state_change_time = clock()

        # open
        elif str(self.state.text()) == "1":
            self.send_command_to_exo(0)
            # self.ser.write(b'1')
            # self.state_machine_state = self.STATE_SEND_OPEN
            # self.state_machine_state_change_time = clock()

        # lock
        elif str(self.state.text()) == "0":
            self.send_command_to_exo(3)
            # self.ser.write(b'0')
            # self.state_machine_state = self.STATE_SEND_LOCK
            # self.state_machine_state_change_time = clock()

        # # Clear the QLineEdit box
        self.state.setText("")
