from enum import Enum
import queue
from threading import Thread

import serial

import time
from typing import Union
from pylsl import StreamInfo, StreamOutlet, local_clock, cf_float32


class MyomoCommands():

    START_STREAM = b'$6\n'
    STOP_STREAM = b'$7\n'


class SerialHandler(Thread):

    def __init__(self, connection, t_update=0.02):
        super().__init__(daemon=True)


        self.t_update = t_update
        self.receive_queue = queue.Queue()

        self.connection = connection
        self.out_queue = queue.Queue()
        self.running = False

    def run(self):
        self.running = True

        while self.running:

            time.sleep(self.t_update)

            # read incoming messages
            recv = self.connection.read_all()
            received_messages = recv.decode(Myomo.ENCODING).split('\n')
            for m in received_messages:
                if len(m.strip()) > 0:
                    self.receive_queue.put(m)

            # send outgoing data
            while not self.out_queue.empty():
                self.connection.write(self.out_queue.get())

        self.connection.close()
        self.running = False

    def send(self, msg: bytes):
        self.out_queue.put(msg)

    def get_message(self) -> Union[str, None]:
        if not self.receive_queue.empty():
            return self.receive_queue.get()
        else:
            return None


class MessageHandler(Thread):

    def __init__(self, get_message_func, myomo_instance):
        super().__init__(daemon=True)

        self.get_message = get_message_func
        self.myomo = myomo_instance

        self.running = False

        self.arm_emg_flex = None
        self.arm_emg_ext = None
        self.arm_angle = None
        self.arm_temp = None

        self.hand_emg_flex = None
        self.hand_emg_ext = None
        self.hand_angle = None
        self.hand_temp = None

        self.bat_capacity = 100
        self.bat_current = 0

        self.lsl_info_emg = StreamInfo(
            'MyomoEMG',          # stream name
            'mixed',                    # stream type
            4,                         # number of channels
            20,                         # sampling rate (Hz)
            cf_float32                  # data type
        )

        desc = self.lsl_info_emg.desc()
        channels = desc.append_child('channels')

        channel_names = ['arm_extensor', 'arm_flexor', 'hand_extensor', 'hand_flexor']
        channel_types = ['EMG'] * 4
        channel_units = ['-'] * 4

        for name, ch_type, unit in zip(channel_names, channel_types, channel_units):
            channel = channels.append_child('channel')
            channel.append_child_value('label', name)
            channel.append_child_value('type', ch_type)
            channel.append_child_value('unit', unit)

        self.lsl_outlet_emg = StreamOutlet(self.lsl_info_emg)


        self.lsl_info_pos = StreamInfo(
            'MyomoMotorPositions',  # stream name
            'mixed',  # stream type
            2,  # number of channels
            20,  # sampling rate (Hz)
            cf_float32  # data type
        )

        desc = self.lsl_info_pos.desc()
        channels = desc.append_child('channels')

        channel_names = ['arm_joint_angle', 'hand_joint_angle']
        channel_types = ['motor_temperature'] * 2
        channel_units = ['%'] * 2

        for name, ch_type, unit in zip(channel_names, channel_types, channel_units):
            channel = channels.append_child('channel')
            channel.append_child_value('label', name)
            channel.append_child_value('type', ch_type)
            channel.append_child_value('unit', unit)

        self.lsl_outlet_pos = StreamOutlet(self.lsl_info_pos)



        self.lsl_info_device = StreamInfo(
            'MyomoDeviceInfo',  # stream name
            'mixed',  # stream type
            4,  # number of channels
            20,  # sampling rate (Hz)
            cf_float32  # data type
        )

        desc = self.lsl_info_device.desc()
        channels = desc.append_child('channels')

        channel_names = ['arm_motor_temp', 'hand_motor_temp', 'battery_capacity', 'battery_current']
        channel_types = ['motor_temperature'] * 2 + ['-'] * 2
        channel_units = ['fahrenheit'] * 2 + ['%', 'Ampere']

        for name, ch_type, unit in zip(channel_names, channel_types, channel_units):
            channel = channels.append_child('channel')
            channel.append_child_value('label', name)
            channel.append_child_value('type', ch_type)
            channel.append_child_value('unit', unit)

        self.lsl_outlet_device = StreamOutlet(self.lsl_info_device)


    def run(self):

        self.running = True

        while self.running:

            msg: str = self.get_message()

            if msg is None:
                time.sleep(0.01)
                continue

            label, *args = msg.split(' ')

            if label == '#x':
                self.arm_emg_ext = float(args[0])
                self.arm_emg_flex = float(args[1])

            elif label == '@x':
                self.hand_emg_ext = float(args[0])
                self.hand_emg_flex = float(args[1])

            elif label == '#y':
                self.arm_angle = float(args[0])
                self.arm_angle -= self.myomo.arm_min_angle
                self.arm_angle = round(100 * self.arm_angle / (self.myomo.arm_max_angle - self.myomo.arm_min_angle))
                self.arm_temp = float(args[1])
                # print(self.arm_angle, "%")

            elif label == '@y':
                self.hand_angle = float(args[0])
                self.hand_angle -= self.myomo.hand_min_angle
                self.hand_angle = round(100 * self.hand_angle / (self.myomo.hand_max_angle - self.myomo.hand_min_angle))
                self.hand_temp = float(args[1])
                # print(self.hand_angle, "%")

            elif label == '#z' or label == '@z':
                self.bat_capacity = float(args[0])
                self.bat_current = float(args[1])

            else:
                print(label, args)

            if self.arm_emg_ext is not None and self.arm_angle is not None \
                    and self.hand_emg_ext is not None and self.hand_angle is not None:

                sample = [self.arm_emg_ext, self.arm_emg_flex, self.hand_emg_ext, self.hand_emg_flex]

                self.lsl_outlet_emg.push_sample(sample)

                sample = [self.arm_angle, self.hand_angle]

                self.lsl_outlet_pos.push_sample(sample)

                sample = [self.arm_temp, self.hand_temp, self.bat_capacity, self.bat_current]

                self.lsl_outlet_device.push_sample(sample)

                self.arm_emg_ext = None
                self.arm_emg_flex = None
                self.arm_angle = None
                self.arm_temp = None
                self.hand_emg_flex = None
                self.hand_emg_ext = None
                self.hand_angle = None
                self.hand_temp = None

        # close outlet
        self.lsl_outlet_emg = None
        self.lsl_outlet_device = None
        self.lsl_outlet_pos = None


class Myomo:

    ENCODING = 'ascii'

    def __init__(self, port='COM3', baud=115200, default_speed=50, hand_min_angle: int = 0, hand_max_angle: int = 100, arm_min_angle: int = 0, arm_max_angle: int = 135):
        """
        :param port: Serial port of the Bluetooth Serial Connection (e.g. 'COM3' on windows, '/dev/...' on unix)
        :param baud: baud rate of the serial connection, defaults to 115200
        :param default_speed: default % speed of exoskeleton movements
        """
        self.connected = False

        self.port = port
        self.baud: int = baud
        self.default_speed: int = default_speed

        self.serial_handler: SerialHandler = None
        self.message_handler: MessageHandler = None
        self.connection: serial.Serial = None

        self.hand_min_angle = hand_min_angle
        self.hand_max_angle = hand_max_angle
        self.arm_min_angle = arm_min_angle
        self.arm_max_angle = arm_max_angle

    def connect(self) -> None:
        """
        Connects to the myomo exoskeleton using a Bluetooth SPP connection
        """

        if self.connected:
            return

        try:
            self.connection = serial.Serial(self.port, self.baud)
        except Exception:
            print("ERROR: Could not establish Bluetooth Serial connection.")
        else:

            self.serial_handler = SerialHandler(self.connection)
            self.serial_handler.start()

            self.message_handler = MessageHandler(self.serial_handler.get_message, self)
            self.message_handler.start()

            # set Mode: 0 -> no internal control
            self.serial_handler.send(b'$0 0\n')
            self.serial_handler.send(b'&0 0\n')

            # set hand min and max degrees
            self.set_hand_boundaries(self.hand_min_angle, self.hand_max_angle)
            self.set_arm_boundaries(self.arm_min_angle, self.arm_max_angle)

            self.serial_handler.send(MyomoCommands.START_STREAM)

            self.connected = True

    def disconnect(self):
        """
        Disconnects a connected exoskeleton.
        """

        if not self.connected:
            return

        self.serial_handler.running = False
        self.message_handler.running = False

        self.serial_handler.join()
        self.message_handler.join()

        self.connected = False

    def set_hand_boundaries(self, min_angle: int = 0, max_angle: int = 100):
        self.hand_min_angle = min_angle
        self.hand_max_angle = max_angle
        self.serial_handler.send(bytes('&\x1bZ {:d} {:d}\n'.format(self.hand_min_angle, self.hand_max_angle), 'ascii'))

    def set_arm_boundaries(self, min_angle: int = 0, max_angle: int = 100):
        self.arm_min_angle = min_angle
        self.arm_max_angle = max_angle
        self.serial_handler.send(bytes('$\x1bZ {:d} {:d}\n'.format(self.arm_min_angle, self.arm_max_angle), 'ascii'))

    def set_default_speed(self, speed: int = 50):
        """
        Sets the default value of movement speed which will be used whenever no specific value is given to movement functions (e.g. close_hand).
        :param speed: % value of movement speed
        """
        self.default_speed = speed

    def _get_speed(self, speedval):
        if type(speedval) is not int or speedval == -1:
            return self.default_speed
        return min(100, max(0, speedval))

    def set_hand_position(self, pos: int, speed: int = -1) -> None:
        """
        Executes a movement of the hand actuator to a certain position.

        :param pos: % value of movement target position (0=open, 100=closed)
        :param speed: % value of movement speed
        """
        self.serial_handler.send(bytes('&C {} {}\n'.format(pos, self._get_speed(speed)), 'ascii'))

    def set_arm_position(self, pos: int, speed: int = -1):
        """
        Executes a movement of the arm/elbow actuator to a certain position.

        :param pos: % value of movement target position (0=extended, 100=flexed)
        :param speed: % value of movement speed
        """
        self.serial_handler.send(bytes('$C {} {}\n'.format(pos, self._get_speed(speed)), Myomo.ENCODING))

    def close_hand(self, speed: int = -1):
        self.set_hand_position(100, speed)

    def close_arm(self, speed: int = -1):
        self.set_arm_position(100, speed)

    def open_hand(self, speed: int = -1):
        self.set_hand_position(0, speed)

    def open_arm(self, speed: int = -1):
        self.set_arm_position(0, speed)


    def stop(self):
        """
        Interrupts and stops any ongoing movement.
        @return:
        """
        self.serial_handler.send(b'$)\n')

    def set_arm_mode(self, mode: int = 0):
        self.serial_handler.send(bytes('$0 {}\n'.format(mode), Myomo.ENCODING))

    def set_hand_mode(self, mode: int = 0):
        self.serial_handler.send(bytes('&0 {}\n'.format(mode), Myomo.ENCODING))


    def set_arm_flexor_gain(self, gain: int = 0, mode: int = 0):
        self.serial_handler.send(bytes('$3 {} {}\n'.format(mode, gain), Myomo.ENCODING))

    def set_arm_extensor_gain(self, gain: int = 0, mode: int = 0):
        self.serial_handler.send(bytes('$4 {} {}\n'.format(mode, gain), Myomo.ENCODING))

    def set_hand_flexor_gain(self, gain: int = 0, mode: int = 0):
        self.serial_handler.send(bytes('&3 {} {}\n'.format(mode, gain), Myomo.ENCODING))

    def set_hand_extensor_gain(self, gain: int = 0, mode: int = 0):
        self.serial_handler.send(bytes('&4 {} {}\n'.format(mode, gain), Myomo.ENCODING))


# add function to set boost and threshold for emg
# add function to set dsampling rate / constant
# add function to set mode