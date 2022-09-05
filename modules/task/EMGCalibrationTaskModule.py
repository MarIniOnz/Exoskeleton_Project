import random

import globals
from misc.enums import ExoState, Cue

from .TaskModule import TaskModule
from pylsl import IRREGULAR_RATE

from misc import log

logger = log.getLogger("EMGCalibrationTaskModule")


class EMGCalibrationTaskModule(TaskModule):
    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME = "EMG Calibration Task Module"
    MODULE_DESCRIPTION = ""

    REQUIRED_LSL_STREAMS = []

    TYPE_OUTPUT_STREAM: str = 'Markers'
    NUM_OUTPUT_CHANNELS: int = 4
    OUTPUT_SAMPLING_RATE: float = IRREGULAR_RATE
    OUTPUT_CHANNEL_FORMAT: str = 'string'
    OUTPUT_CHANNEL_NAMES: list = ['Cue', 'leftExoState', 'rightExoState', 'Cue_marker']

    # overwrite parameter definition which is empty by superclass
    PARAMETER_DEFINITION = [
        {
            'name': 'num_cues',
            'displayname': 'Number of Cues:',
            'description': 'How many close and relax cues (each) will be displayed.',
            'type': int,
            'unit': '',
            'default': 10
        },
        {
            'name': 'cue_length',
            'displayname': 'Cue length',
            'description': 'How long the close/relax cues will be displayed.',
            'type': float,
            'unit': 's',
            'default': 5.0
        },
        {
            'name': 'random_order',
            'displayname': 'Pseudo-random Order',
            'description': 'Whether to pseudo-randomize the order of cues or display them alternating.',
            'type': bool,
            'unit': '',
            'default': False
        },
        {
            'name': 'iti_min',
            'displayname': 'Min ITI length',
            'description': 'How long the ITI (inter trial interval) will last at least',
            'type': float,
            'unit': 's',
            'default': 1.0
        },
        {
            'name': 'iti_max',
            'displayname': 'Max ITI length',
            'description': 'How long the ITI (inter trial interval) will last at most',
            'type': float,
            'unit': 's',
            'default': 3.0
        }
    ]

    def __init__(self):
        super(EMGCalibrationTaskModule, self).__init__()

        # outputs
        self.cue = Cue.EMPTY
        ##
        self.state_left_exo = ExoState.HIDE_STOP
        self.state_right_exo = ExoState.HIDE_STOP

        self.control_by_eeg = False
        self.control_by_emg = False

    # overwrite run method
    def run_task(self):

        # fetch parameters for ITI length and calculate the amount of ITI which will be randomly determined
        min_iti_length: float = self.parameters['iti_min'].getValue()
        max_iti_length: float = self.parameters['iti_max'].getValue()
        iti_random_amount: float = max(0, max_iti_length - min_iti_length)

        self.wait(10)

        self.cue = Cue.STARTIN5
        self.wait(2.5)

        self.cue = Cue.EMPTY
        self.wait(2.5)

        # create a list of Hovleft / Hovright cues in alternating order
        cues = [Cue.LIFT, Cue.RELAX, Cue.HOLD_STILL] * self.parameters['num_cues'].getValue()

        # if the user selected to pseudo-randomize the order of cues, shuffle the cue-list
        if self.parameters['random_order'].getValue():
            random.shuffle(cues)

        # play cues
        for c in cues:

            # display the cue
            self.cue = c

            # if this is a close cue, enable EEG control
            if c == Cue.LIFT or c == Cue.HOLD_STILL or c == Cue.RELAX:
                self.control_by_emg = True

            self.wait(self.parameters['cue_length'].getValue())

            # disabled EEG control after Cue
            self.control_by_eeg = False
            # disabled EMG control after Cue
            self.control_by_emg = False

            # display no cue = ITI
            self.cue = Cue.EMPTY

            # reopen the Exo
            self.state_left_exo = ExoState.HIDE_OPEN
            self.state_right_exo = ExoState.HIDE_OPEN

            self.wait(min_iti_length + random.random() * iti_random_amount)



        self.cue = Cue.END
        self.wait(2)

        self.cue = Cue.EMPTY
        self.wait(3)

    # overwrite process_data input method
    def process_data(self, sample, timestamp):

        # copy inputs
        self.norm_out_c3 = sample[0]
        self.norm_out_c4 = sample[1]
        self.HOV_left = sample[2] > 0.5
        self.HOV_right = sample[3] > 0.5
        self.low_mu_c3 = sample[4] > 0.5
        self.low_mu_c4 = sample[5] > 0.5
        self.high_emg = sample[6] > 0.5 # TODO check with Martín
        self.low_emg = sample[7] > 0.5

        # set some outputs
        if self.control_by_emg:

            if self.high_emg:
                self.state_right_exo = ExoState.CLOSE_ARM
            elif self.low_emg:
                self.state_right_exo = ExoState.OPEN_ARM
            else:
                self.state_left_exo = ExoState.STOP


        # Send a string marker to analyze the data
        if self.cue == Cue.LIFT and self.cue != self.last_cue:
            Cue_Markers = 'LIFT'
        elif self.cue == Cue.HOLD_STILL and self.cue != self.last_cue:
            Cue_Markers = 'STILL'
        elif self.cue == Cue.RELAX and self.cue != self.last_cue:
            Cue_Markers = 'RELAX'
        elif self.cue == Cue.STARTIN5 and self.cue != self.last_cue:
            Cue_Markers = 'START'
        elif self.cue == Cue.END and self.cue != self.last_cue:
            Cue_Markers = 'END'
        else:
            Cue_Markers = 'none'

        self.last_cue = self.cue
        logger.info(self.cue.value)
        out_sample = [str(self.cue.value), str(self.state_left_exo.value), str(self.state_right_exo.value), Cue_Markers]
        return (out_sample, timestamp)