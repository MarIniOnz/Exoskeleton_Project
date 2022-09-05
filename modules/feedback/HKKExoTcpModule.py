import time
import random 
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from PyQt5.QtWidgets import QPushButton, QLabel, QCheckBox

import globals
from misc import enums, log
from misc.timing import clock
from modules.module import Module
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop, IRREGULAR_RATE
from misc.LSLStreamInfoInterface import add_mappings, add_channel_names, add_parameters
from misc.gui import BoldLabel

logger = log.getLogger("HKKExoTcpModule")

class HKKExoTcpModule(Module):

    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    
    MODULE_NAME: str = "HKK Exoskeleton TCP Control Module"
    MODULE_DESCRIPTION: str = ""
    # MODULE_PATH = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])
    # APP_PATH = MODULE_PATH / "SinglePacmanFeedbackApp.py"

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_TASK_EVENTS]

    # parameters of LSL outlet
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
            'name': 'exo_ip',
            'displayname': 'Exoskeleton IP address',
            'description': '',
            'type': str,
            'unit': '',
            'default': '192.168.4.1'
        },
        {
            'name': 'exo_port',
            'displayname': 'Exoskeleton port',
            'description': '',
            'type': int,
            'unit': '',
            'default': 22123
        }

    ]

    # exo commands
    EXO_COMMAND_NONE = b'0'
    EXO_COMMAND_CLOSE = b'1'
    EXO_COMMAND_OPEN = b'2'


    def __init__(self):

        super(HKKExoTcpModule, self).__init__()
        self.setStatus(Module.Status.STOPPED)

        self.lsl_inlet = None
        self.lsl_outlet = None
        self.lsl_stream_info = None

        self.running = False
        self.datathread = None
        self.socket = None
        self.last_msg_sent = None
        self.last_msg_time = None

        self.mute_output = False


    def initGui(self):
        super(HKKExoTcpModule, self).initGui()

        row: int = self.layout.rowCount()

        btn_send_close = QPushButton("Send CLOSE")
        btn_send_open = QPushButton("Send OPEN")

        btn_send_close.clicked.connect(lambda: [self.sendMessage(self.EXO_COMMAND_NONE), self.sendMessage(self.EXO_COMMAND_CLOSE)])
        btn_send_open.clicked.connect(lambda: [self.sendMessage(self.EXO_COMMAND_NONE), self.sendMessage(self.EXO_COMMAND_OPEN)])

        label = QLabel("These controls allow to send close and open commands manually. Be aware that these commands are sent without checking the current state of the exoskeleton and are not recorded in the experiments data.")
        label.setWordWrap(True);

        label1 = QLabel("Check this box to disable any reaction to the BCI signal. The button for manual control above will still work.")
        label1.setWordWrap(True);


        self.checkbox_mute = QCheckBox("ignore control commands")



        self.layout.addWidget(BoldLabel("Actions"), row, 0, 1, 4)
        self.layout.addWidget(label, row+1, 0, 1, 5)
        self.layout.addWidget(btn_send_close, row+2, 0, 1, 2)
        self.layout.addWidget(btn_send_open, row+2, 2, 1, 3)
        self.layout.addWidget(label1, row+3, 0, 1, 5)
        self.layout.addWidget(self.checkbox_mute, row+4, 0, 1, 5)

    def start(self):
        
        # do not start if the LSL LabRecorder App is not available
        if not globals.LSLAvailable:
            return

        # do not start up the module if it was already started
        if self.status != Module.Status.STOPPED:
            return

        # set status
        self.setStatus(Module.Status.STARTING)


        # connect to exo's electronic box
        try:
            self.socket = socket(AF_INET, SOCK_STREAM)
            self.socket.settimeout(2)
            self.socket.connect((self.getParameter('exo_ip'), self.getParameter('exo_port')))
            # send initial zero
            self.sendMessage(self.EXO_COMMAND_NONE)
        except Exception:
            self.setStatus(Module.Status.STOPPED)
            self.socket = None
            logger.error(f"Could not start {self.MODULE_NAME} because exoskeleton could not be connected.")
            return


        # fetch necessary lsl stream
        streams = resolve_byprop("name", globals.STREAM_NAME_TASK_EVENTS, minimum=1, timeout=10)

        if len(streams) < 1:
            self.socket.close()
            self.socket = None
            self.setStatus(Module.Status.STOPPED)
            logger.error(f"Could not start {self.MODULE_NAME} because of missing stream: {globals.STREAM_NAME_CLASSIFIED_SIGNAL}")
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
            'uid'+str(random.randint(100000, 999999))
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

        # close TCP connection to exoskeleton
        self.socket.close()
        self.socket = None

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


    # sends a TCP message to the exoskeleton
    def sendMessage(self, msg: bytes) -> bool:

        try:
            self.socket.sendall(msg)
            if msg != self.EXO_COMMAND_NONE:
                self.last_msg_sent = msg
            self.last_msg_time = clock()
            return True
        except Exception:
            return False


    def handle_input(self):

        while self.running:

            in_sample, in_timestamp = self.lsl_inlet.pull_sample(timeout=1)

            if in_sample is not None:

                out_sample, out_timestamp = (None, in_timestamp) #self.process_data(in_sample, in_timestamp)

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

                self.mute_output = self.checkbox_mute.isChecked()

                # send Message
                if self.mute_output:
                    self.sendMessage(self.EXO_COMMAND_NONE)
                    out_sample = [int(self.EXO_COMMAND_NONE)]
                elif relevant_exo_state == enums.ExoState.OPEN:
                    self.sendMessage(self.EXO_COMMAND_OPEN)
                    out_sample = [int(self.EXO_COMMAND_OPEN)]
                elif relevant_exo_state == enums.ExoState.CLOSE:
                    self.sendMessage(self.EXO_COMMAND_CLOSE)
                    out_sample = [int(self.EXO_COMMAND_CLOSE)]
                else:
                    self.sendMessage(self.EXO_COMMAND_NONE)
                    out_sample = [int(self.EXO_COMMAND_NONE)]
                
                
                # if a message was sent to the exoskeleton and thus out_sample is not None -> push a sample documenting the message
                if out_sample is not None:

                    self.lsl_outlet.push_sample(out_sample, out_timestamp)
    
