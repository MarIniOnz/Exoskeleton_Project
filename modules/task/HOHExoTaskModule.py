from modules.task.TaskModule import TaskModule

from misc.enums import Cue, ExoState, Side
import globals

from misc.timing import clock

from misc import log
logger = log.getLogger("HOHExoTaskModul")


class HOHExoTaskModule(TaskModule):
    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME = "HOH Exo control Task Module"
    MODULE_DESCRIPTION = "Allows to close exo by EEG and open it EOG."

    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_CLASSIFIED_SIGNAL]

    NUM_OUTPUT_CHANNELS: int = 3
    OUTPUT_SAMPLING_RATE: float = globals.NEUROPYPE_TICK_RATE
    OUTPUT_CHANNEL_FORMAT: str = 'int32'
    OUTPUT_CHANNEL_NAMES: list = ['Cue', 'leftExoState', 'rightExoState']

    # overwrite parameter definition which is empty by superclass
    PARAMETER_DEFINITION = [
        {
            'name': 'exo_side',
            'displayname': 'Side of exoskeleton:',
            'description': '',
            'type': list,
            'unit': ['right', 'left'],
            'default': 'left'
        },
        {
            'name': 'close_erd_length',
            'displayname': 'ERD minimum length',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 2.0
        },
        {
            'name': 'max_motion_length',
            'displayname': 'Maximum motion time',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 6
        },
    ]

    STATE_START = 0
    STATE_READY = 1
    STATE_SEND_OPEN = 2
    STATE_SEND_CLOSE = 3
    STATE_STOP = 4
    STATE_SEND_LOCK = 5
    STATE_INACTIVE = 6

    STATE_NAMES = {
        STATE_INACTIVE: "not active",
        STATE_START: "start",
        STATE_READY: "ready",
        STATE_SEND_CLOSE: "sending CLOSE",
        STATE_SEND_OPEN: "sending OPEN",
        STATE_SEND_LOCK: "sending LOCK",
    }

    def __init__(self):
        super(HOHExoTaskModule, self).__init__()

        self.cue = Cue.EMPTY
        self.left_exo_state = ExoState.STOP
        self.right_exo_state = ExoState.STOP
        
        self.state_machine_state = self.STATE_INACTIVE
        self.state_machine_state_change_time = clock()

        self.eeg_start = None
        self.close_clock = None
        # placeholders
        self.norm_out_c3 = None
        self.norm_out_c4 = None
        self.HOV_left = None
        self.HOV_right = None
        self.low_mu_c3 = None
        self.low_mu_c4 = None
        self.low_mu = None
        self.HOV = None
        self.last_sample= None

        self.time_state_machine_update = clock()
        self.time_in_close_state = 0

    def run_task(self):
        self.state_machine_state = self.STATE_INACTIVE
        logger.info(f"Inactive state")
        logger.info("10s to start")
        self.wait(5)
        logger.info("5s to start")
        self.wait(5)
        self.state_machine_state = self.STATE_START
        self.state_machine_state_change_time = clock()
        logger.info(f'Change state to {self.STATE_NAMES[self.state_machine_state]}')
        self.wait(60 * 120)

    def process_data(self, sample, timestamp):

        # copy inputs
        self.norm_out_c3 = sample[0]
        self.norm_out_c4 = sample[1]
        self.HOV_left = sample[2] > 0.5
        self.HOV_right = sample[3] > 0.5
        self.low_mu_c3 = sample[4] > 0.5
        self.low_mu_c4 = sample[5] > 0.5

        # select relevant EEG signal
        self.low_mu = self.low_mu_c3
        if Side(self.getParameter("exo_side")) is Side.LEFT:
            self.low_mu = self.low_mu_c4

        # create non-directional EOG signal, which is True as soon as any directional signal is True
        last_hov = self.HOV
        self.HOV = self.HOV_left or self.HOV_right
        HOV_EVENT = False
        if self.HOV and not last_hov:
            HOV_EVENT = True

        # state machine

        # inactive state
        if self.state_machine_state == self.STATE_INACTIVE:
            self.cue = Cue.EXO_INACTIVE
            pass

        # start state
        elif self.state_machine_state == self.STATE_START:
            self.cue = Cue.EXO_ACTIVE
            if HOV_EVENT:

                self.state_machine_state = self.STATE_READY
                logger.info(f'Change state to {self.STATE_NAMES[self.state_machine_state]}')
                # self.left_exo_state = ExoState.START
                # self.right_exo_state = ExoState.START

                # set exo state for start exo
                if Side(self.getParameter("exo_side")) == Side.RIGHT:
                    self.right_exo_state = ExoState.START
                elif Side(self.getParameter("exo_side")) == Side.LEFT:
                    self.left_exo_state = ExoState.START



        # exo is open and resting state
        elif self.state_machine_state == self.STATE_READY:
            self.cue = Cue.EXO_READY

            # if ERD is starting:
            if self.eeg_start is None and self.low_mu:
                self.eeg_start = clock()

            elif self.eeg_start is None and not self.low_mu:
                 self.state_machine_state = self.STATE_READY

            # if ERD is ongoing
            elif self.eeg_start is not None and self.low_mu:

                # if ERD exceeded 1s
                if clock() - self.eeg_start >= self.getParameter("close_erd_length"):

                    self.state_machine_state = self.STATE_SEND_CLOSE
                    self.state_machine_state_change_time = clock()
                    logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

            # if EOG is positive -> opening is required
            if HOV_EVENT:
                # stop any EEG counting
                self.eeg_start = None

                self.state_machine_state = self.STATE_SEND_LOCK
                self.state_machine_state_change_time = clock()

                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")


        # exo is open and resting state
        elif self.state_machine_state == self.STATE_SEND_LOCK:
            self.cue = Cue.EXO_BLOCKED

            # set exo state for lock exo
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.LOCK
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.LOCK
            
            # if EOG is positive -> opening is required
            if HOV_EVENT:
                self.state_machine_state = self.STATE_SEND_OPEN
                logger.info(f'Change state to {self.STATE_NAMES[self.state_machine_state]}')
                self.state_machine_state_change_time = clock()


        # open exo state
        elif self.state_machine_state == self.STATE_SEND_OPEN:
            self.cue = Cue.EXO_BLOCKED
            # set exo state for open exo
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.OPEN
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.OPEN

            # set state to start state after max motion length (s)
            if clock() - self.state_machine_state_change_time >= self.getParameter("max_motion_length"):
                self.state_machine_state = self.STATE_START
                self.state_machine_state_change_time = clock()
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")


        # close exo state
        elif self.state_machine_state == self.STATE_SEND_CLOSE:
            self.cue = Cue.EXO_READY

            # set exo state for close exo
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.CLOSE
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.CLOSE

            # if the time reaches the maximum close time send lock command
            self.time_in_close_state += clock() - self.time_state_machine_update
            if HOV_EVENT:
                self.eeg_start = None
                self.state_machine_state = self.STATE_SEND_LOCK
                self.state_machine_state_change_time = clock()

                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

            elif self.time_in_close_state >= self.getParameter('max_motion_length'):
               logger.info(self.time_in_close_state)
               logger.info("MAX CLOSE was reached")
               self.state_machine_state = self.STATE_SEND_LOCK
               self.state_machine_state_change_time = clock()
               self.time_in_close_state = 0
               logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")
               self.eeg_start = None

            # if ERD ended
            elif self.eeg_start is not None and not self.low_mu:
                logger.info(self.time_in_close_state)

                self.state_machine_state = self.STATE_READY
                self.state_machine_state_change_time = clock()
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")
                self.left_exo_state = ExoState.STOP
                self.right_exo_state = ExoState.STOP
                self.eeg_start = None



        # if self.left_exo_state == self.last_sample:
        #     self.left_exo_state = ExoState.HIDE_OPEN
        # else:
        #     self.last_sample = self.left_exo_state

        self.time_state_machine_update = clock()

        # create output sample and return
        out_sample = [self.cue.value, self.left_exo_state.value, self.right_exo_state.value]
        return out_sample, timestamp

    def onStop(self):

        if self.state_machine_state == self.STATE_SEND_CLOSE or self.state_machine_state == self.STATE_SEND_LOCK or self.state_machine_state == self.STATE_READY:

            self.state_machine_state = self.STATE_START

            # set exo state for open 
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.OPEN
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.OPEN

            # set exo state for stop
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.STOP
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.STOP

        self.wait(1)