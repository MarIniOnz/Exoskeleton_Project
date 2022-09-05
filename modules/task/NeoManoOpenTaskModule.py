from typing import Any, Union

from modules.task.TaskModule import TaskModule

from misc.enums import Cue, ExoState, Side
import globals
from misc.timing import clock

from misc import log

logger = log.getLogger("NeoManoOpenTaskModule")


class NeoManoOpenTaskModule(TaskModule):
    state_machine_state_change_time: Union[float, Any]
    # make it a runnable descent of the module-class (which in this case is TaskModule)
    MODULE_RUNNABLE: bool = True

    MODULE_NAME = "NeoMano Open Task Module"
    MODULE_DESCRIPTION = "Allows to open the exo by EEG, grasp it and then release it with EOG."

    # get the stream corresponding to the classifier module output
    REQUIRED_LSL_STREAMS = [globals.STREAM_NAME_CLASSIFIED_SIGNAL]

    NUM_OUTPUT_CHANNELS: int = 3
    OUTPUT_SAMPLING_RATE: float = globals.NEUROPYPE_TICK_RATE
    OUTPUT_CHANNEL_FORMAT: str = 'int32'
    OUTPUT_CHANNEL_NAMES: list = ['Cue', 'leftExoState', 'rightExoState']

    # overwrite the parameter definition, empty in the superclass
    PARAMETER_DEFINITION = [
        {
            'name': 'exo_side',
            'displayname': 'Side of the exoskeleton:',
            'description': '',
            'type': list,
            'unit': ['right', 'left'],
            'default': 'right',
        },
        {
            'name': 'open_erd_length',
            'displayname': 'ERD minimum length',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 0.5,
        },
        {
            'name': 'max_open_motion_length',
            'displayname': 'Maximum opening motion time',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 2.0,
        },
        {
            'name': 'wait_time_till_close',
            'displayname': 'Time between full open and grasp',
            'description': 'Wait time between the hand achieves its full open position and the closing is performed.',
            'type': float,
            'unit': 's',
            'default': 8.0,
        },
        {
            'name': 'grasp_closing_time',
            'displayname': 'Time on closing the hand',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 2.0,
        },
        {
            'name': 'time_neutral_pos',
            'displayname': 'Time for neutral position',
            'description': 'Specify the maximum time it takes to go to neutral position from a completely closed one.',
            'type': float,
            'unit': 's',
            'default': 8.0,
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
    STATE_SEND_NEUTRAL_HAND = 7

    STATE_NAMES = {
        STATE_INACTIVE: 'non active',
        STATE_START: 'start',
        STATE_READY: 'ready',
        STATE_SEND_CLOSE: "sending CLOSE",
        STATE_SEND_OPEN: "sending OPEN",
        STATE_SEND_LOCK: "sending LOCK",
        STATE_SEND_NEUTRAL_HAND: "sending NEUTRAL POSITION"
    }

    def __init__(self):
        super(NeoManoOpenTaskModule, self).__init__()

        self.cue = Cue.EMPTY
        self.left_exo_state = ExoState.STOP
        self.right_exo_state = ExoState.STOP

        # Parameters start
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
        self.last_sample = None

        self.state_machine_state = self.STATE_INACTIVE
        self.time_state_machine_update = clock()
        self.time_in_open_state = 0

    def run_task(self):
        self.left_exo_state = ExoState.STOP
        self.right_exo_state = ExoState.STOP
        self.state_machine_state = self.STATE_INACTIVE
        logger.info(f"Inactive state")
        logger.info("4s to start")
        self.wait(2)
        logger.info("2s to start")
        self.wait(2)

        self.state_machine_state_change_time = clock()
        self.state_machine_state = self.STATE_SEND_NEUTRAL_HAND
        logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")
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
        hov_event = False
        if self.HOV and not last_hov:
            hov_event = True

        # state machine

        # inactive state
        if self.state_machine_state == self.STATE_INACTIVE:
            pass

        # exo is in its READY position (already neutral position achieved)
        elif self.state_machine_state == self.STATE_READY:

            # if ERD is starting:
            if self.eeg_start is None and self.low_mu:
                self.eeg_start = clock()

            elif self.eeg_start is None and not self.low_mu:
                self.state_machine_state = self.STATE_READY

            # if ERD is ongoing
            elif self.eeg_start is not None and self.low_mu:

                # if ERD exceeded the ERD length
                if clock() - self.eeg_start >= self.getParameter("open_erd_length"):
                    self.state_machine_state = self.STATE_SEND_OPEN
                    self.state_machine_state_change_time = clock()
                    logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

            # if EOG is positive -> go back to LOCK
            if hov_event:
                # stop any EEG counting
                self.eeg_start = None

                self.state_machine_state = self.STATE_SEND_LOCK
                self.state_machine_state_change_time = clock()
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

        # start state
        elif self.state_machine_state == self.STATE_START:

            if hov_event:

                self.state_machine_state = self.STATE_READY
                logger.info(f'Change state to {self.STATE_NAMES[self.state_machine_state]}')

                if Side(self.getParameter("exo_side")) == Side.RIGHT:
                    self.right_exo_state = ExoState.START
                elif Side(self.getParameter("exo_side")) == Side.LEFT:
                    self.left_exo_state = ExoState.START

        # exo is open and resting state
        elif self.state_machine_state == self.STATE_SEND_LOCK:

            self.time_in_open_state = 0
            # set exo state for lock exo
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.LOCK
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.LOCK

            # if EOG is positive -> Go back to Neutral position and to READY state
            if hov_event:
                self.state_machine_state_change_time = clock()
                self.state_machine_state = self.STATE_SEND_NEUTRAL_HAND
                # we are now in READY state again
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

        # NEUTRAL_POS ExoState
        elif self.state_machine_state == self.STATE_SEND_NEUTRAL_HAND:

            # if self.getParameter("integrated_neutral") == 'True'
            # set exo state for going to the neutral position
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.NEUTRAL_HAND
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.NEUTRAL_HAND

            # set state to start state after max motion length (s)
            if clock() - self.state_machine_state_change_time >= self.getParameter("time_neutral_pos"):
                self.state_machine_state_change_time = clock()
                self.state_machine_state = self.STATE_START
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

        # CLOSE exo state
        elif self.state_machine_state == self.STATE_SEND_CLOSE:

            # set exo state for close exo
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.CLOSE
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.CLOSE

            # set state to start state after max motion length (s)
            if (clock() - self.state_machine_state_change_time >= self.getParameter("grasp_closing_time")) or hov_event:

                self.state_machine_state = self.STATE_SEND_LOCK
                self.state_machine_state_change_time = clock()
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

        # OPEN exo state
        elif self.state_machine_state == self.STATE_SEND_OPEN:

            # set exo state for close exo
            if Side(self.getParameter("exo_side")) == Side.RIGHT:
                self.right_exo_state = ExoState.OPEN
            elif Side(self.getParameter("exo_side")) == Side.LEFT:
                self.left_exo_state = ExoState.OPEN

            # if the time reaches the maximum close time send lock command
            self.time_in_open_state += clock() - self.time_state_machine_update
            if hov_event:
                self.eeg_start = None
                self.state_machine_state = self.STATE_SEND_LOCK
                self.state_machine_state_change_time = clock()

                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")

            elif self.time_in_open_state >= self.getParameter('max_open_motion_length'):
                logger.info("MAX OPEN was reached")

                self.time_in_open_state = 0
                self.eeg_start = None

                # close the hand after the waiting time for grasping is over
                if clock() - self.state_machine_state_change_time >= self.getParameter('wait_time_till_close'):
                    self.state_machine_state = self.STATE_SEND_CLOSE
                    logger.info(f'Change state to {self.STATE_NAMES[self.state_machine_state]}')
                    self.state_machine_state_change_time = clock()

                # close the hand after the waiting time for grasping is over

            # if ERD ended
            elif self.eeg_start is not None and not self.low_mu:
                logger.info(self.time_in_open_state)

                self.state_machine_state = self.STATE_READY
                self.state_machine_state_change_time = clock()
                logger.info(f"Change state to {self.STATE_NAMES[self.state_machine_state]}")
                self.left_exo_state = ExoState.STOP
                self.right_exo_state = ExoState.STOP
                self.eeg_start = None

        self.time_state_machine_update = clock()

        # create output sample and return
        out_sample = [self.cue.value, self.left_exo_state.value, self.right_exo_state.value]
        return out_sample, timestamp
