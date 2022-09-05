import random
import time
from threading import Thread

from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop, IRREGULAR_RATE

import globals
from misc import enums, log
from misc.LSLStreamInfoInterface import add_mappings, add_channel_names, add_parameters
from misc.gui import BoldLabel
from misc.timing import clock
from modules.module import Module
from misc import myomo
logger = log.getLogger("MyomoModule")


class MyomoFeedbackModule(Module):
    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "Myomo Exoskeleton TCP Control Module"
    MODULE_DESCRIPTION: str = ""

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_TASK_EVENTS]

    # parameters of LSL outlet
    NUM_OUTPUT_CHANNELS: int = 1
    OUTPUT_CHANNEL_NAMES = ['command_sent']
    OUTPUT_SAMPLING_RATE: float = IRREGULAR_RATE
    OUTPUT_CHANNEL_FORMAT: str = 'int32'

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
            'name': 'activate',
            'displayname': 'Activate the exo',
            'description': 'Whether the exo should activate or not.',
            'type': bool,
            'unit': '',
            'default': True
        },
        {
            'name': 'comport',
            'displayname': 'COMport',
            'description': '',
            'type': str,
            'unit': '',
            'default': 'COM4'
        },
        {
            'name': 'min_angle',
            'displayname': 'Min hand',
            'description': 'Minimum angle of hand movement',
            'type': int,
            'unit': '°',
            'default': 0
        },
        {
            'name': 'max_angle',
            'displayname': 'Max hand',
            'description': 'Maximum angle of hand movement',
            'type': int,
            'unit': '°',
            'default': 100
        },
        {
            'name': 'min_arm',
            'displayname': 'Min arm',
            'description': 'Minimum angle of arm movement',
            'type': int,
            'unit': '°',
            'default': 20
        },
        {
            'name': 'max_arm',
            'displayname': 'Max arm',
            'description': 'Maximum angle of arm movement',
            'type': int,
            'unit': '°',
            'default': 100
        },
        {
            'name': 'gain',
            'displayname': 'EMG gain',
            'description': 'Gain to amplify EMG',
            'type': int,
            'unit':'',
            'default': 5
        }
    ]

    # exo states
    EXO_STATE_START = 0
    EXO_STATE_CLOSE_HAND = 1
    EXO_STATE_OPEN_HAND = 2
    EXO_STATE_CLOSE_ARM = 3
    EXO_STATE_OPEN_ARM = 4
    EXO_STATE_STOP = 5
    EXO_STATE_LOCK = 6
    EXO_STATE_NEUTRAL_HAND = 7
    EXO_STATE_NEUTRAL_ARM = 8

    def __init__(self):

        super(MyomoFeedbackModule, self).__init__()
        self.setStatus(Module.Status.STOPPED)

        self.lsl_inlet = None
        self.lsl_outlet = None
        self.lsl_stream_info = None
        self.running = False
        self.datathread = None
        self.state_machine_state = 5
        self.mute_output = False
        self.state_machine_state_change_time = clock()
        # self.number_open = 0
        self.start_position = 70
        self.position_common = self.start_position

    def initGui(self):
        super(MyomoFeedbackModule, self).initGui()

        row: int = self.layout.rowCount()

        btn_send_connect = QPushButton("Connect", clicked = lambda: [self.Connect()])
        btn_send_disconnect = QPushButton("Disconnect", clicked = lambda: [self.Disconnect()])
        btn_send_action = QPushButton("Action", clicked = lambda: [self.Action()])

        self.state = QLineEdit()

        label = QLabel(
            "Connect and disconnect the exo with bluetooth: ")
        label.setWordWrap(True);
        label1 = QLabel(
            "HAND [1: open, 2: close, 7: neutral]\nARM  [3: open, 4: close, 8:neutral]")
        label1.setWordWrap(True)

        self.layout.addWidget(label, row, 0, 1, 5)
        self.layout.addWidget(btn_send_connect, row + 1, 0, 1, 2)
        self.layout.addWidget(btn_send_disconnect, row + 1, 2, 1, 3)
        self.layout.addWidget(BoldLabel("Actions"), row + 2, 0, 1, 4)
        self.layout.addWidget(label1, row + 3, 0, 1, 5)
        self.layout.addWidget(btn_send_action, row + 4, 2, 2, 3)
        self.layout.addWidget(self.state, row + 4, 0, 1, 2)

    def Connect(self):
        self.exo = myomo.Myomo(port=self.getParameter('comport'), hand_min_angle=self.getParameter("min_angle"),
                              hand_max_angle=self.getParameter("max_angle"))
            #, arm_min_angle=self.getParameter("min_arm"),
                    #          arm_max_angle=self.getParameter("max_arm"))
        self.exo.connect()
        self.exo.set_arm_flexor_gain(gain=self.getParameter('gain'))
        self.state_machine_thread = Thread(target=self.state_machine, daemon=True)
        self.state_machine_thread.start()

    def Disconnect(self):
        logger.info("Exo Disconnected")
        self.exo.disconnect()

    def start(self):

        # do not start if the LSL LabRecorder App is not available
        if not globals.LSLAvailable:
            return

        # do not start up the module if it was already started
        if self.status != Module.Status.STOPPED:
            return

        # set status
        self.setStatus(Module.Status.STARTING)

        # open connection to myomo.exo
        self.Connect()

        # fetch necessary lsl stream
        streams = resolve_byprop("name", globals.STREAM_NAME_TASK_EVENTS, minimum=1, timeout=10)

        if len(streams) < 1:
            self.Disconnect()
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

        # parameter for start position
        self.position_common = self.start_position

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

        # close connection to exoskeleton
        self.Disconnect()

        # close lsl connections
        if self.lsl_inlet is not None:
            self.lsl_inlet.close_stream()
        self.lsl_inlet = None
        self.lsl_outlet = None

        # set status
        self.setStatus(Module.Status.STOPPED)
        logger.info(f"Module {self.MODULE_NAME} stopped")

    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()

    def state_machine(self):

        while True and self.getParameter('activate'):
            time.sleep(0.01)

            time_since_state_change = clock() - self.state_machine_state_change_time
            # stop
            if self.state_machine_state == self.EXO_STATE_STOP:
                self.exo.stop()

            # start
            elif self.state_machine_state == self.EXO_STATE_START:
                self.exo.close_hand()
                if time_since_state_change >= 0.5:
                    self.exo.set_hand_position(self.position_common)
                if time_since_state_change >= 1:
                    self.state_machine_state = self.EXO_STATE_STOP

            # hand
            if self.state_machine_state == self.EXO_STATE_OPEN_HAND:

                self.position_common -= 20
                self.exo.set_hand_position(self.position_common)
                time.sleep(1)  # check times
                # self.exo.open_hand()

            elif self.state_machine_state == self.EXO_STATE_CLOSE_HAND:
                self.exo.close_hand()

            # arm
            elif self.state_machine_state == self.EXO_STATE_OPEN_ARM:
                self.exo.open_arm()

            elif self.state_machine_state == self.EXO_STATE_CLOSE_ARM:
                self.exo.close_arm()

            # lock
            elif self.state_machine_state == self.EXO_STATE_LOCK:
                self.exo.stop()

            # neutral position
            elif self.state_machine_state == self.EXO_STATE_NEUTRAL_HAND:
                if time_since_state_change < 2:
                    self.exo.set_hand_position(0)
                elif time_since_state_change >= 2:  # Can be changed.
                    self.exo.set_hand_position(60)

                # parameter for start position
                self.position_common = self.start_position

            elif self.state_machine_state == self.EXO_STATE_NEUTRAL_ARM:
                self.exo.set_arm_position(60)

    def handle_input(self):
        self.last_relevant_exo_state = None

        while self.running:
            in_sample, in_timestamp = self.lsl_inlet.pull_sample(timeout=1)

            if in_sample is not None:

                #out_sample, out_timestamp = (None, in_timestamp)  # self.process_data(in_sample, in_timestamp)

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
                    # send Message

                    if relevant_exo_state == enums.ExoState.OPEN:

                        self.state_machine_state = self.EXO_STATE_OPEN_HAND
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.OPEN_ARM:

                        self.state_machine_state = self.EXO_STATE_OPEN_ARM
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.CLOSE:

                        self.state_machine_state = self.EXO_STATE_CLOSE_HAND
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.CLOSE_ARM:

                        self.state_machine_state = self.EXO_STATE_CLOSE_ARM
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.STOP:

                        self.state_machine_state = self.EXO_STATE_STOP
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.LOCK:

                        self.state_machine_state = self.EXO_STATE_LOCK
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.START:

                        self.state_machine_state = self.EXO_STATE_START
                        self.state_machine_state_change_time = clock()

                    elif relevant_exo_state == enums.ExoState.NEUTRAL_HAND:
                        self.state_machine_state = self.EXO_STATE_NEUTRAL_HAND
                        self.state_machine_state_change_time = clock()

                    # elif relevant_exo_state == enums.ExoState.NEUTRAL_ARM:
                    #
                    #     self.state_machine_state = self.EXO_STATE_NEUTRAL_ARM
                    #     self.state_machine_state_change_time = clock()

                self.last_relevant_exo_state = relevant_exo_state

                # # if a message was sent to the exoskeleton and thus out_sample is not None -> push a sample documenting the message
                # if out_sample is not None:
                #     self.lsl_outlet.push_sample(out_sample, out_timestamp)

    def Action(self):
        if self.state.text().strip() == '0':
            self.state_machine_state = self.EXO_STATE_START
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '1':
            self.state_machine_state = self.EXO_STATE_OPEN_HAND
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '2':
            self.state_machine_state = self.EXO_STATE_CLOSE_HAND
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '3':
            self.state_machine_state = self.EXO_STATE_OPEN_ARM
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '4':
            self.state_machine_state = self.EXO_STATE_CLOSE_ARM
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '5':
            self.state_machine_state = self.EXO_STATE_STOP
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '6':
            self.state_machine_state = self.EXO_STATE_LOCK
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '7':
            self.state_machine_state = self.EXO_STATE_NEUTRAL_HAND
            self.state_machine_state_change_time = clock()
        elif self.state.text().strip() == '8':
            self.state_machine_state = self.EXO_STATE_NEUTRAL_ARM
            self.state_machine_state_change_time = clock()


#testen z.B.     logger.info('change state to close')