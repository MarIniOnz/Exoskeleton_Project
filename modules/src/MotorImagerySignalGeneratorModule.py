from threading import Thread
import time
import math
import random
from typing import List

from modules.module import Module

import globals
from misc import LSLStreamInfoInterface
from misc.timing import clock
from pylsl import StreamInfo, StreamOutlet

from PyQt5.QtWidgets import QPushButton
from misc.gui import BoldLabel

import logging
logger = logging.getLogger("pythonbci.modules.src.MotorImagerySignalGeneratorModule")

class RingBuffer(object):

    def __init__(self, datatype=float, size: int = 1000, default_value=1.0):

        self.data_type = datatype
        self.size = size
        self.default_value = default_value
        self.buffer: List[datatype] = [default_value] * size

        self.pointer: int = 0

    def movePointer(self, steps:int = 1):

        self.pointer = (self.pointer + steps) % self.size

    def read(self):

        val = self.buffer[self.pointer]
        self.buffer[self.pointer] = self.default_value
        self.movePointer(1)
        return val

    def insert_ahead(self, values: list):

        for i, v in enumerate(values):

            insert_index = (self.pointer + 1 + i) % self.size
            self.buffer[insert_index] = v


class MotorImagerySignalGeneratorModule(Module):

     # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "Motor Imagery Signal Generator"
    MODULE_DESCRIPTION: str = ""

    PARAMETER_DEFINITION = [
        {
            'name': 'setup',
            'displayname': 'Electrode setup',
            'description': '',
            'type': list,
            'unit': ['bilateral', 'bilateral+EOG', 'unilateralC3', 'unilateralC3+EOG', 'unilateralC4', 'unilateralC4+EOG'],
            'default': 'bilateral+EOG'
        },
        {
            'name': 'fs',
            'displayname': 'Sample rate',
            'description': '',
            'type': int,
            'unit': 'Hz',
            'default': 500
        },
        {
            'name': 'chunksize',
            'displayname': 'Chunk size',
            'description': '',
            'type': int,
            'unit': 'samples',
            'default': 10
        },
        {
            'name': 'f_smr',
            'displayname': 'SMR frequency',
            'description': '',
            'type': float,
            'unit': 'Hz',
            'default': 11.0
        },
        {
            'name': 'amplitude_smr',
            'displayname': 'SMR amplitude',
            'description': '',
            'type': float,
            'unit': 'uV',
            'default': 2.0
        },
        {
            'name': 'amplitude_noise',
            'displayname': 'Noise amplitude',
            'description': '',
            'type': float,
            'unit': 'uV',
            'default': 1.0
        },
        {
            'name': 'erd_length',
            'displayname': 'ERD length',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 4.0
        },
        {
            'name': 'erd_shape',
            'displayname': 'ERD temporal shape',
            'description': '',
            'type': list,
            'unit': ['squared sine halfwave', 'rectangular'],
            'default': 'squared sine halfwave'
        },
        {
            'name': 'hov_amplitude',
            'displayname': 'HOV amplitude',
            'description': '',
            'type': float,
            'unit': 'uV',
            'default': 750.0
        }

    ]    

    def __init__(self):
        super(MotorImagerySignalGeneratorModule, self).__init__()

        self.setStatus(Module.Status.STOPPED)

        self.lsl_streaminfo = None
        self.lsl_outlet = None
        self.num_channels = None
        self.channel_names = None

        self.generator_thread = None

        self.running = False

        self.ringbuffer_c3 = None
        self.ringbuffer_c4 = None

    def initGui(self):

        Module.initGui(self)
    
        row: int = self.layout.rowCount()
        
        button_c3_erd = QPushButton("ERD C3")
        button_c4_erd = QPushButton("ERD C4")
        button_hov_left = QPushButton("HOV left")
        button_hov_right = QPushButton("HOV right")

        button_c3_erd.clicked.connect(lambda: [self.insertERD(self.ringbuffer_c3, self.getParameter("erd_length"), 0.7), self.insertERD(self.ringbuffer_c4, self.getParameter("erd_length"), 0.3)])
        button_c4_erd.clicked.connect(lambda: [self.insertERD(self.ringbuffer_c4, self.getParameter("erd_length"), 0.7), self.insertERD(self.ringbuffer_c3, self.getParameter("erd_length"), 0.3)])

        button_hov_left.clicked.connect(lambda: self.insertHOV(self.ringbuffer_eog_left, amount=self.getParameter("hov_amplitude")))
        button_hov_right.clicked.connect(lambda: self.insertHOV(self.ringbuffer_eog_right, amount=self.getParameter("hov_amplitude")))

        self.layout.addWidget(BoldLabel("Actions"), row, 0, 1, 4)

        self.layout.addWidget(button_c3_erd, row+1, 0, 1, 2)
        self.layout.addWidget(button_c4_erd, row+1, 2, 1, 2)

        self.layout.addWidget(button_hov_left, row+2, 0, 1, 2)
        self.layout.addWidget(button_hov_right, row+2, 2, 1, 2)


    def insertERD(self, buffer: RingBuffer, length: float = 1.0, amount: float = 1.0):

        samples = [buffer.default_value] * int(length * self.getParameter("fs"))

        if self.getParameter("erd_shape") == "rectangular":
        
            for i in range(len(samples)):
                samples[i] -= samples[i]*amount*1

        else:
            T_sine = 2 * length
            f_sine = 1 / T_sine

            for i in range(len(samples)):

                t = T_sine/2 + i * T_sine/2/len(samples)
                samples[i] -= samples[i]*amount*(math.sin(2 * math.pi * f_sine * t)**2)

        buffer.insert_ahead(samples)

    def insertHOV(self, buffer: RingBuffer, length: float = 0.8, amount: float = 700.0):

        samples = [buffer.default_value] * int(length * self.getParameter("fs"))

        T_sine = 2 * length
        f_sine = 1 / T_sine

        for i in range(len(samples)):

            t = T_sine/2 + i * T_sine/2/len(samples)
            samples[i] = samples[i] + amount*(math.sin(2 * math.pi * f_sine * t)**4)

        buffer.insert_ahead(samples)


    def sine_value(self, t: float, f: float, amplitude: float):

        return math.sin(t * 2 * math.pi * f ) * amplitude


    def generateSample(self, t: float):

        sample = []

        for i in range(self.num_channels):

            sample.append(random.random() * self.getParameter('amplitude_noise'))

            # C3 EEG channel
            if "C3" in self.channel_names and i == self.channel_names.index("C3"):
                sample[-1] += self.sine_value(t, self.getParameter('f_smr'), self.ringbuffer_c3.read())

            # C4 EEG channel
            elif "C4" in self.channel_names and i == self.channel_names.index("C4"):
                sample[-1] += self.sine_value(t, self.getParameter('f_smr'), self.ringbuffer_c4.read())
            
            # if an EOG-setup is used, insert the EOG signal on its channels
            if self.getParameter("setup").endswith("+EOG"):
                
                # left EOG channel
                if "F7" in self.channel_names and i == self.channel_names.index("F7"):
                    sample[-1] += self.ringbuffer_eog_left.read()

                # right EOG channel
                elif "F8" in self.channel_names and i == self.channel_names.index("F8"):
                    sample[-1] += self.ringbuffer_eog_right.read()

            # if there are no seperate electrodes for EOG, add a portion of the signal to F3 and F4
            else:
                if i == self.channel_names.index("F3"):
                    sample[-1] += 0.5 * self.ringbuffer_eog_left.read()
                elif i == self.channel_names.index("F4"):
                    sample[-1] += 0.5 * self.ringbuffer_eog_right.read()


        return sample


    def sendChunk(self, t_last_sample=clock()):

        if self.lsl_outlet is None:
            return

        chunksize = self.getParameter("chunksize")
        delta_T = 1/self.getParameter('fs')
        
        chunk = []
        for i in range(chunksize,0,-1):
            t_sample = t_last_sample - ((i-1) * delta_T)
            chunk.append(self.generateSample(t_sample))



        self.lsl_outlet.push_chunk(chunk, t_last_sample)
        

    def signal_generator(self):

        start = clock()

        fs: int = self.getParameter('fs')
        delta_T = 1/fs
        chunksize: int = self.getParameter("chunksize")

        samples_sent: int = 0

        sleeptime: float = max(0.001, 1/fs*chunksize/10)

        while self.running:

            time.sleep(sleeptime)

            now = clock()

            time_since_start = now-start

            samples_target_now = math.floor(time_since_start * fs)

            samples_missing = samples_target_now - samples_sent

            if samples_missing >= chunksize:

                time_of_chunks_last_sample = clock() - ( (samples_missing-chunksize) * delta_T )
                self.sendChunk(time_of_chunks_last_sample)
                samples_sent += chunksize




    def start(self):

        if self.getStatus() is not Module.Status.STOPPED:
            return

        self.setStatus(Module.Status.STARTING)

        # set channel count and channel labels based on which electrode setup was selected
        if self.getParameter('setup') == 'bilateral':

            self.num_channels = 9
            self.channel_names = ["P3", "F3", "C3", "Cz", "T7", "P4", "F4", "C4", "T8"]

        if self.getParameter('setup') == 'bilateral+EOG':

            self.num_channels = 11
            self.channel_names = ["P3", "F3", "C3", "Cz", "T7", "P4", "F4", "C4", "T8", "F7", "F8"]

        elif self.getParameter('setup') == 'unilateralC3':

            self.num_channels = 5
            self.channel_names = ["P3", "F3", "C3", "Cz", "T7"]
        
        elif self.getParameter('setup') == 'unilateralC3+EOG':

            self.num_channels = 7
            self.channel_names = ["P3", "F3", "C3", "Cz", "T7", "F7", "F8"]

        elif self.getParameter('setup') == 'unilateralC4':

            self.num_channels = 5
            self.channel_names = ["Cz", "P4", "F4", "C4", "T8"]
        
        elif self.getParameter('setup') == 'unilateralC4+EOG':

            self.num_channels = 7
            self.channel_names = ["Cz", "P4", "F4", "C4", "T8", "F7", "F8"]



        # generate stream info
        self.lsl_streaminfo = StreamInfo(
            globals.STREAM_NAME_RAW_SIGNAL,
            'EEG',
            self.num_channels,
            float(self.getParameter("fs")),
            'double64',
            'uid'+str(random.randint(100000, 999999))
        )

        # add channel names to stream info
        LSLStreamInfoInterface.add_channel_names(self.lsl_streaminfo, self.channel_names)

        # add parameters to stream info
        LSLStreamInfoInterface.add_parameters(self.lsl_streaminfo, self.parameters)

        # init LSL outlet
        self.lsl_outlet = StreamOutlet(self.lsl_streaminfo, chunk_size=self.getParameter('chunksize'))


        # init ringbuffers
        self.ringbuffer_c3 = RingBuffer(float, size=10*self.getParameter("fs"), default_value=self.getParameter('amplitude_smr'))
        self.ringbuffer_c4 = RingBuffer(float, size=10*self.getParameter("fs"), default_value=self.getParameter('amplitude_smr'))

        # init ringbuffers for EOG signal with random offset
        self.ringbuffer_eog_left = RingBuffer(float, size=10*self.getParameter("fs"), default_value=(random.random()-0.5)*10000)
        self.ringbuffer_eog_right = RingBuffer(float, size=10*self.getParameter("fs"), default_value=(random.random()-0.5)*10000)

        # start generator thread
        self.running = True
        self.generator_thread = Thread(daemon=True, target=self.signal_generator)
        self.generator_thread.start()

        self.setStatus(Module.Status.RUNNING)
        logger.info("Module started")

    
    def stop(self):

        print("STOPPING", self.MODULE_NAME)

        if self.getStatus() is not Module.Status.RUNNING:
            return

        self.setStatus(Module.Status.STOPPING)

        # wait for signal generator thread to stop
        self.running = False
        print(self.MODULE_NAME + ': Waiting for generator thread to terminate... ')
        while self.generator_thread.is_alive():
            time.sleep(0.1)

        time.sleep(0.1)

        self.generator_thread = None
        print("done.")

        self.lsl_outlet = None

        self.setStatus(Module.Status.STOPPED)



    def restart(self):
        self.stop()
        time.sleep(0.2)
        self.start()