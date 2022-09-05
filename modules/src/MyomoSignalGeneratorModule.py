import globals
from modules.module import Module
from modules.src.MotorImagerySignalGeneratorModule import MotorImagerySignalGeneratorModule

from misc.gui import BoldLabel
from misc import LSLStreamInfoInterface
from misc.timing import clock

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QSlider, QLabel

from pylsl import StreamInfo, StreamOutlet

import random
import time
import math
from typing import Optional
from threading import Thread


class MyomoSignalGeneratorModule(MotorImagerySignalGeneratorModule):

    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "Myomo Signal Generator"
    MODULE_DESCRIPTION: str = ""

    EMG_STREAM_NAME = 'MyomoEMG'
    EMG_SAMPLING_FREQUENCY = 10
    EMG_NUM_CHANNELS = 4
    EMG_CHANNEL_NAMES = ['arm_extensor', 'arm_flexor', 'hand_extensor', 'hand_flexor']
    EMG_CHANNEL_TYPES = ['EMG'] * 4
    EMG_CHANNEL_UNITS = ['-'] * 4


    PARAMETER_DEFINITION = MotorImagerySignalGeneratorModule.PARAMETER_DEFINITION
    PARAMETER_DEFINITION += [
        {
            'name': 'emg_min_value',
            'displayname': 'EMG Minimum',
            'description': '',
            'type': int,
            'unit': '',
            'default': 10
        },
        {
            'name': 'emg_max_value',
            'displayname': 'EMG Maximum',
            'description': '',
            'type': int,
            'unit': '',
            'default': 100
        },
        {
            'name': 'emg_noise_level',
            'displayname': 'EMG Noise',
            'description': '',
            'type': int,
            'unit': '',
            'default': 5
        },
    ]

    def __init__(self):
        super().__init__()

        self.emg_lsl_streaminfo: Optional[StreamInfo] = None
        self.emg_lsl_outlet: Optional[StreamOutlet] = None


    def emg_signal_generator(self):

        start = clock()

        fs: int = self.EMG_SAMPLING_FREQUENCY
        delta_T = 1/fs

        samples_sent: int = 0

        sleeptime: float = max(0.001, 1/fs/10)

        timestamp_next = start + delta_T

        emg_min = self.getParameter('emg_min_value')
        emg_range = self.getParameter('emg_max_value') - emg_min
        emg_noise = self.getParameter('emg_noise_level')

        while self.running:

            time.sleep(sleeptime)

            now = clock()

            if now >= timestamp_next:

                sample = [
                    max(0, emg_min + self.emg_slider_1.value()/1000 * emg_range + (random.random()-0.5) * emg_noise),
                    max(0, emg_min + self.emg_slider_2.value()/1000 * emg_range + (random.random()-0.5) * emg_noise),
                    max(0, emg_min + self.emg_slider_3.value()/1000 * emg_range + (random.random()-0.5) * emg_noise),
                    max(0, emg_min + self.emg_slider_4.value()/1000 * emg_range + (random.random()-0.5) * emg_noise),
                ]
                self.emg_lsl_outlet.push_sample(sample, timestamp_next)

                timestamp_next += delta_T
                samples_sent += 1


    def start(self):

        if self.getStatus() is not Module.Status.STOPPED:
            return

        self.setStatus(Module.Status.STARTING)

        # generate stream info
        self.emg_lsl_streaminfo = StreamInfo(
            self.EMG_STREAM_NAME,
            'EMG',
            self.EMG_NUM_CHANNELS,
            float(self.EMG_SAMPLING_FREQUENCY),
            'double64',
            'uid'+str(random.randint(100000, 999999))
        )

        # add channel names to stream info
        LSLStreamInfoInterface.add_channel_names(self.emg_lsl_streaminfo, self.EMG_CHANNEL_NAMES)
        LSLStreamInfoInterface.add_channel_metadata(self.emg_lsl_streaminfo, self.EMG_CHANNEL_NAMES, self.EMG_CHANNEL_UNITS, None, self.EMG_CHANNEL_TYPES)

        # add parameters to stream info
        LSLStreamInfoInterface.add_parameters(self.emg_lsl_streaminfo, self.parameters)

        # init LSL outlet
        self.emg_lsl_outlet = StreamOutlet(self.emg_lsl_streaminfo)

        self.setStatus(Module.Status.STOPPED)

        super().start()

        self.setStatus(Module.Status.STARTING)

        self.emg_generator_thread = Thread(daemon=True, target=self.emg_signal_generator)
        self.emg_generator_thread.start()

        self.setStatus(Module.Status.RUNNING)


    def stop(self):

        super().stop()

        self.setStatus(Module.Status.STOPPING)

        # wait for signal generator thread to stop
        self.running = False
        print(self.MODULE_NAME + ': Waiting for EMG generator thread to terminate... ')
        while self.emg_generator_thread.is_alive():
            time.sleep(0.1)

        time.sleep(0.1)

        self.emg_generator_thread = None
        print("done.")

        self.emg_lsl_outlet = None


        self.setStatus(Module.Status.STOPPED)

    def initGui(self):

        super().initGui()


        row: int = self.layout.rowCount()

        self.layout.addWidget(BoldLabel("EMG"), row, 0, 1, 1)
        self.layout.addWidget(QLabel("Ch 1 & 2:"), row, 1, 1, 1)
        self.layout.addWidget(QLabel("Ch 3 & 4:"), row+1, 1, 1, 1)

        button_1 = QPushButton("+")
        button_1.setStyleSheet("background-color: red; color: white; border: none;")

        #self.layout.addWidget(button_1, row, 1, 1, 1)

        SLIDER_WIDTH: int = 100

        self.emg_slider_1 = QSlider(Qt.Horizontal)
        self.emg_slider_1.setRange(0,1000)
        self.emg_slider_1.setFixedWidth(SLIDER_WIDTH)

        self.emg_slider_2 = QSlider(Qt.Horizontal)
        self.emg_slider_2.setRange(0,1000)
        self.emg_slider_2.setFixedWidth(SLIDER_WIDTH)

        self.emg_slider_3 = QSlider(Qt.Horizontal)
        self.emg_slider_3.setRange(0,1000)
        self.emg_slider_3.setFixedWidth(SLIDER_WIDTH)

        self.emg_slider_4 = QSlider(Qt.Horizontal)
        self.emg_slider_4.setRange(0,1000)
        self.emg_slider_4.setFixedWidth(SLIDER_WIDTH)

        self.layout.addWidget(self.emg_slider_1, row, 2, 1, 1)
        self.layout.addWidget(self.emg_slider_2, row, 3, 1, 1)
        self.layout.addWidget(self.emg_slider_3, row+1, 2, 1, 1)
        self.layout.addWidget(self.emg_slider_4, row+1, 3, 1, 1)

