from misc.enums import Cue, ExoState, Side
import globals

from misc.LSLStreamInfoInterface import add_channel_names, add_parameters
from misc.timing import clock
import time
from time import sleep

from modules.module import Module

import serial
from serial import Serial
from serial.tools import list_ports

import misc.log as log

logger = log.getLogger("NeoMano_Communication")

try:
    ser.close()
except:
    pass

cdc = next(list_ports.grep("VID:PID=10C4:EA60"))
ser = serial.Serial(port=cdc.device, baudrate=115200, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False,
                    write_timeout=None, dsrdtr=False, inter_byte_timeout=None, exclusive=None)
logger.info(f"Dongle detected at port: {ser.name}")

if not ser.isOpen():
    ser.open()

# Parameters settings
time_long = 1.5


def opening(serial_obj=ser):
    serial_obj.write(b'2')


def closing(serial_obj=ser):
    serial_obj.write(b'1')


def stopping(serial_obj=ser):
    serial_obj.write(b'3')


# ROUTINE 1
def routine_1(time_used, serial_obj=ser):
    closing()
    sleep(time_used)
    opening()
    sleep(time_used)
    closing()
    sleep(time_used)
    opening()


# routine_1(2)

# ROUTINE 2
def routine_2(time_used, time_stop, serial_obj=ser):
    closing()
    sleep(time_used)
    opening()
    sleep(time_used)
    stopping()  ###
    sleep(time_stop)
    closing()
    sleep(time_used)
    opening()
    sleep(time_used)
    stopping()


# Introduces random commands and creates more at the end of the routine.
opening()
# sleep(3)
# routine_2(1,2)

# ROUTINE 3
def routine_3(time_used, serial_obj=ser):
    closing()
    sleep(time_used)
    opening()
    sleep(time_used)
    closing()
    sleep(time_used)
    opening()
    sleep(time_used)
    stopping()


# Stop as "other command" executed
# routine_3(2)

# ROUTINE 4
def routine_4(time_while, type=True):
    start = clock()
    while start <= clock() - time_while:
        if type:
            opening()
        else:
            closing()


# routine_4(4, False)

# ROUTINE 5
def routine_5(time_while, type=True):
    start = clock()
    while start <= clock() - time_while:
        if type:
            opening()
            closing()
        else:
            closing()
            opening()


# routine_5(4, False)

# ROUTINE 6
def routine_6(time_wait, time_while, type=True):
    if type:
        opening()
        sleep(time_wait)
        start = clock()
        while start <= clock() - time_while:
            closing()
    else:
        closing()
        sleep(time_wait)
        start = clock()
        while start <= clock() - time_while:
            opening()


# routine_6(2, 2)

# ROUTINE 7
def routine_7(time_wait, for_times, type=True):
    for i in range(0, for_times):
        if type:
            opening()
        else:
            closing()
        sleep(time_wait)
    stopping()


# Works as intended, when too much time fully closed: starts opening.
# routine_7(1, 2, False)


# ROUTINE 8
def routine_8(time_wait, time_stop, for_times, type=True):
    for i in range(0, for_times):
        if type:
            opening()
        else:
            closing()
        sleep(time_wait)
        stopping()
        sleep(time_stop)


# Stops prevents from opening.
# routine_8(1, 1, 2, False)


# ROUTINE 9
def routine_9(time_wait, time_stop, for_times, type=True):
    stopping()
    sleep(time_stop)

    for i in range(0, for_times):
        if type:
            opening()
        else:
            closing()
        sleep(time_wait)

    stopping()


# routine_9(1, 1, 2, True)


# closing()
# sleep(4)
# stopping()
# opening()
# sleep(3)
# closing()

# Opens when +10 seconds fully closed.

# Long break before the routine ends
# x=2
#
# if x==1:
#
#     closing()
#     sleep(4)
#     stopping()
#
# elif x==2:
#     opening()
#     # sleep(1)
#     # stopping()
#     sleep(2)
#     opening()
#     # sleep(2)
#     # stopping()
#     sleep(2)
#     print('hello')
#     opening()
#     # sleep(2)
#     # stopping()
#     sleep(2)
#     opening()
#     sleep(2)
#     stopping()
# sleep(2)
#
# opening()
# sleep(2)
# stopping()
