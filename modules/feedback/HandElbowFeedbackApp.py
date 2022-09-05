import sys, time
import PyQt5 as Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout
# import simpleaudio as sa
from threading import Thread
import random
import os
import argparse
import math

import pathlib
curpath = pathlib.Path(os.path.split(os.path.abspath(__file__))[0])
modules_path = curpath.parent
pybci_path = modules_path.parent
sys.path.append(str(modules_path))
sys.path.append(str(pybci_path))

import globals
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop
from misc.enums import Side, Cue, DisplayText, ExoState
from modules.module import Module
from misc import LSLStreamInfoInterface
from misc.timing import clock

class TextWidget(QWidget):

    def __init__(self):

        super(TextWidget, self).__init__()

        self.visible = True

        self.text_lines = []

        self.color = QtGui.QColor(255, 255, 255)


    def paintEvent(self, e):

        if self.visible:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawText(qp)
            qp.end()


    def drawText(self, qp):

        size = self.size()
        w = size.width()
        h = size.height()

        fontdiv = 16

        if len(self.text_lines) == 1 and len(self.text_lines[0]) < 4:
            fontdiv = 4
        elif len(self.text_lines) == 1 and len(self.text_lines[0]) <= 12:
            fontdiv = 8

        font = qp.font()
        font.setPixelSize(int(round(3*h/fontdiv)))
        qp.setFont(font)
        qp.setPen(self.color)

        for i in range(len(self.text_lines)):
            qp.drawText(0, 0+int(round(i*h/(fontdiv-3))), w, h, QtCore.Qt.AlignHCenter, self.text_lines[i])

    def setText(self, text: str):
        self.text_lines = text.split("\n")


class RelaxFeedbackWidget(QWidget):
    GOOD_COLOR = Qt.QtGui.QColor(100, 200, 255)
    BAD_COLOR = Qt.QtGui.QColor(255, 200, 50)
    
    def __init__(self):
        super().__init__()

        self.visible: bool = True
        self.enabled: bool = True

        self.relax_value = 1.0
        self.state: int = Cue.EMPTY.value

        self.background = Qt.QtGui.QColor(0, 0, 0)
        self.color = Qt.QtGui.QColor(0, 0, 0)

    def updateStates(self):

        if self.state == Cue.RELAX.value:
            value = self.relax_value

            if value > 1:
                value = 1
            elif value < 0:
                value = 0

            value = value*0.8+0.2

            # mix colors
            self.color.setRed(int(round(
                self.GOOD_COLOR.red()*value + self.BAD_COLOR.red()*(1-value)
            )))
            self.color.setGreen(int(round(
                self.GOOD_COLOR.green()*value + self.BAD_COLOR.green()*(1-value)
            )))
            self.color.setBlue(int(round(
                self.GOOD_COLOR.blue()*value + self.BAD_COLOR.blue()*(1-value)
            )))

    def paintEvent(self, e):

        self.updateStates()

        if self.visible and self.state == Cue.RELAX.value:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawRelax(qp)
            qp.end()
      
    def drawRelax(self, qp):

        size = self.size()
        w = size.width()
        h = size.height()

        gr = Qt.QtGui.QRadialGradient(0.5, 0.5, 0.5)
        gr.setCoordinateMode(Qt.QtGui.QRadialGradient.ObjectBoundingMode)

        gr.setColorAt(1, self.background)
        if self.enabled:
            gr.setColorAt(0, self.color)
        else:
            gr.setColorAt(0, self.background)

        br = Qt.QtGui.QBrush(gr)
        qp.setBrush(br)

        qr_size = min(w, h)
        radius = qr_size/2
        qp.fillRect(int(round(w/2-radius)), int(round(h/2-radius)), qr_size, qr_size, br)


class PacmanWidget(QWidget):

    ENABLED_COLOR = QtGui.QColor(255, 200, 100)
    DISABLED_COLOR = QtGui.QColor(100, 100, 100)

    CLOSE_SPEED_PERCENT_PER_SEC: float = 25
    OPEN_SPEED_PERCENT_PER_SEC: float = 200

    def __init__(self, rotation: int = 0):
        super().__init__()

        self.rotation = rotation

        self.visible: bool = True
        self.enabled: bool = True

        self.closed_percent: float = 0.0

        self.lastUpdate = time.time()

        self.state: int = ExoState.STOP.value


    def updateStates(self):

        t = time.time()
        dt = t - self.lastUpdate

        self.lastUpdate = t

        if self.state == ExoState.CLOSE.value or self.state == ExoState.HIDE_CLOSE.value:
            self.closed_percent += dt * self.CLOSE_SPEED_PERCENT_PER_SEC
            self.closed_percent = max(0, min(100, self.closed_percent))
        elif self.state == ExoState.OPEN.value or self.state == ExoState.HIDE_OPEN.value:
            self.closed_percent -= dt * self.OPEN_SPEED_PERCENT_PER_SEC
            self.closed_percent = max(0, min(100, self.closed_percent))


    def paintEvent(self, e):

        self.updateStates()

        if self.visible and self.state not in [ExoState.HIDE_STOP.value, ExoState.HIDE_OPEN.value, ExoState.HIDE_CLOSE.value]:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawPacman(qp)
            qp.end()


    def drawPacman(self, qp):

        size = self.size()
        w = size.width()
        h = size.height()

        if self.enabled:
            qp.setPen(self.ENABLED_COLOR)
            qp.setBrush(self.ENABLED_COLOR)
        else:
            qp.setPen(self.DISABLED_COLOR)
            qp.setBrush(self.DISABLED_COLOR)

        diameter = min(w, h)
        radius = diameter / 2
        qp.drawPie(
            int(round(w/2 - radius)), int(round(h/2 - radius)), diameter, diameter, 
            int(round(self.rotation + 60-self.closed_percent*1.2/2))*16, int(round(240+self.closed_percent*1.2))*16
        )


class PacmanWidget1(QWidget):

    ENABLED_COLOR = QtGui.QColor(255, 200, 100)
    DISABLED_COLOR = QtGui.QColor(100, 100, 100)

    CLOSE_SPEED_PERCENT_PER_SEC: float = 25
    OPEN_SPEED_PERCENT_PER_SEC: float = 200

    def __init__(self, rotation: int = 0, radius: int = 100, x: int = 100, y: int = 100, debug = False):
        super().__init__()

        self.rotation = rotation

        self.visible: bool = True
        self.enabled: bool = True

        self.closed_percent: float = 0.0

        self.lastUpdate = time.time()

        self.state: int = ExoState.STOP.value

        self.x = x
        self.y = y
        self.r = radius

        self.debug = debug


    def updateStates(self):

        t = time.time()
        dt = t - self.lastUpdate

        self.lastUpdate = t

        if self.state == ExoState.CLOSE.value or self.state == ExoState.HIDE_CLOSE.value:
            self.closed_percent += dt * self.CLOSE_SPEED_PERCENT_PER_SEC
            self.closed_percent = max(0, min(100, self.closed_percent))
        elif self.state == ExoState.OPEN.value or self.state == ExoState.HIDE_OPEN.value:
            self.closed_percent -= dt * self.OPEN_SPEED_PERCENT_PER_SEC
            self.closed_percent = max(0, min(100, self.closed_percent))


    def paintEvent(self, e):

        self.updateStates()

        if self.visible and self.state not in [ExoState.HIDE_STOP.value, ExoState.HIDE_OPEN.value, ExoState.HIDE_CLOSE.value]:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawPacman(qp)
            qp.end()


    def drawPacman(self, qp):

        size = self.size()
        w = size.width()
        h = size.height()

        if self.enabled:
            qp.setPen(self.ENABLED_COLOR)
            qp.setBrush(self.ENABLED_COLOR)
        else:
            qp.setPen(self.DISABLED_COLOR)
            qp.setBrush(self.DISABLED_COLOR)

        diameter = self.r * 2

        x = self.x - self.r
        y = self.y - self.r

        qp.drawPie(
            x, y, diameter, diameter,
            int(round(self.rotation + 60-self.closed_percent*1.2/2))*16, int(round(240+self.closed_percent*1.2))*16
        )

        if self.debug:
            qp.setBrush(QtGui.QColor(255, 0, 0))
            qp.setPen(QtGui.QColor(255, 0, 0))

            qp.drawPie(self.x - 5, self.y - 5, 10, 10, 0, 360*16)


class BeamWidget(QWidget):

    ENABLED_COLOR = QtGui.QColor(255, 200, 100)
    DISABLED_COLOR = QtGui.QColor(100, 100, 100)

    CLOSE_SPEED_PERCENT_PER_SEC: float = 25
    OPEN_SPEED_PERCENT_PER_SEC: float = 200

    def __init__(self, default_angle: int = 0, angle: int = 0, x = 0, y = 0, length = 1, width = 1, debug = False):
        super().__init__()

        self.visible: bool = True
        self.enabled: bool = True

        self.debug = debug

        self.default_angle = default_angle

        self.update_geometry(x, y, length, width, angle)

    def update_geometry(self, x = None, y = None, l = None, w = None, angle = None, default_angle = None):

        if x is None: x = self.start_x
        if y is None: y = self.start_y
        if l is None: l = self.length
        if w is None: w = self.width
        if angle is None: angle = self.angle
        if default_angle is None: default_angle = self.default_angle

        self.length = l
        self.width = w
        self.angle = angle
        self.default_angle = default_angle
        self.pivot_dist = self.length - self.width
        self.start_x = x
        self.start_y = y

        self.radius = round(w/2)

        angle = self.default_angle + self.angle
        angle_rad = 2*math.pi*angle/360

        self.end_x = round(self.start_x + math.cos(angle_rad) * self.length)
        self.end_y = round(self.start_y + math.sin(angle_rad) * self.length)

        self.pivot1_x = round(self.start_x + math.cos(angle_rad) * self.radius)
        self.pivot1_y = round(self.start_y + math.sin(angle_rad) * self.radius)

        self.pivot2_x = round(self.pivot1_x + math.cos(angle_rad) * self.pivot_dist)
        self.pivot2_y = round(self.pivot1_y + math.sin(angle_rad) * self.pivot_dist)




        self.p1x = round(self.pivot1_x+math.sin(angle_rad)*self.radius)
        self.p1y = round(self.pivot1_y-math.cos(angle_rad)*self.radius)

        self.p2x = round(self.pivot1_x-math.sin(angle_rad)*self.radius)
        self.p2y = round(self.pivot1_y+math.cos(angle_rad)*self.radius)

        self.p3x = round(self.pivot2_x-math.sin(angle_rad)*self.radius)
        self.p3y = round(self.pivot2_y+math.cos(angle_rad)*self.radius)

        self.p4x = round(self.pivot2_x+math.sin(angle_rad)*self.radius)
        self.p4y = round(self.pivot2_y-math.cos(angle_rad)*self.radius)

        self.points = QtGui.QPolygon([
            QtCore.QPoint(self.p1x, self.p1y),    # top left
            QtCore.QPoint(self.p2x, self.p2y),    # bottom left
            QtCore.QPoint(self.p3x, self.p3y),    # bottom right
            QtCore.QPoint(self.p4x, self.p4y)     # top right
        ])

    def paintEvent(self, e):

        if self.visible:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawBeam(qp)
            qp.end()


    def drawBeam(self, qp: QtGui.QPainter):

        if self.enabled:
            qp.setPen(self.ENABLED_COLOR)
            qp.setBrush(self.ENABLED_COLOR)
        else:
            qp.setPen(self.DISABLED_COLOR)
            qp.setBrush(self.DISABLED_COLOR)


        angle = self.default_angle + self.angle

        qp.drawPolygon(self.points)

        qp.drawPie(self.pivot1_x - self.radius, self.pivot1_y - self.radius, self.width, self.width, round((90-angle)*16), 360*16)
        qp.drawPie(self.pivot2_x - self.radius, self.pivot2_y - self.radius, self.width, self.width, round((270-angle)*16), 360*16)

        if self.debug:
            qp.setBrush(QtGui.QColor(255, 0, 0))
            qp.setPen(QtGui.QColor(255, 0, 0))

            qp.drawPie(self.pivot1_x - 5, self.pivot1_y - 5, 10, 10, 0, 360*16)
            qp.drawPie(self.pivot2_x - 5, self.pivot2_y - 5, 10, 10, 0, 360*16)

            qp.setBrush(QtGui.QColor(0, 255, 0))
            qp.setPen(QtGui.QColor(0, 255, 0))

            qp.drawPie(self.p1x - 5, self.p1y - 5, 10, 10, 0, 360*16)
            qp.drawPie(self.p2x - 5, self.p2y - 5, 10, 10, 0, 360*16)
            qp.drawPie(self.p3x - 5, self.p3y - 5, 10, 10, 0, 360*16)
            qp.drawPie(self.p4x - 5, self.p4y - 5, 10, 10, 0, 360*16)

            qp.setBrush(QtGui.QColor(0, 0, 255))
            qp.setPen(QtGui.QColor(0, 0, 255))

            qp.drawPie(self.start_x - 5, self.start_y - 5, 10, 10, 0, 360*16)
            qp.drawPie(self.end_x - 5, self.end_y - 5, 10, 10, 0, 360*16)


class SinglePacmanFeedbackApp(QMainWindow):

    OUTPUT_CHANNEL_NAMES: list = ["left pacman closed", "right pacman closed"]

    def __init__(self,
                 left, top, width=1000, height=700,
                 fullscreen=False, maximized=False, frameless=False, stay_on_top=False, fps = 0,
                 side=Side.RIGHT, display_pacman: bool = True,  display_relax: bool = False,
                 time_close_hand = 2.0, time_open_hand = 0.5, time_close_arm = 3.0, time_open_arm = 1.5
                 ):

        if stay_on_top:
            super().__init__(None, QtCore.Qt.WindowStaysOnTopHint)
        else:
            super().__init__()

        self.side = side
        self.display_pacman = display_pacman
        self.display_relax = display_relax

        self.time_close_hand = time_close_hand
        self.time_open_hand = time_open_hand
        self.time_close_arm = time_close_arm
        self.time_open_arm = time_open_arm

        if fps == 0:
            self.fps = globals.FEEDBACK_FRAMERATE
        else:
            self.fps = fps

        self.parameters = {
            "laterality": Module.Parameter("laterality", "laterality", str, self.side.value, "", ""),
            "display pacman": Module.Parameter("display_pacman", "display pacman", bool, self.display_pacman, "", ""),
            "display relax": Module.Parameter("display_relax", "display pacman during open", bool, self.display_relax, "", "")
        }


        # states
        self.state_display_text: int = 0
        self.state_left_pacman: int = 0
        self.state_right_pacman: int = 0

        # flag to allow external process to close the window
        self.close_sheduled = False

        # lsl setup
        streams = resolve_byprop("name", globals.STREAM_NAME_TASK_EVENTS, minimum=1, timeout=3)
        if len(streams) < 1:
            print("Missing LSL stream")
            sys.exit()
        self.lsl_inlet = StreamInlet(streams[0], max_buflen=360, max_chunklen=1, recover=True)

        if self.display_relax:
            streams = resolve_byprop("name", globals.STREAM_NAME_CLASSIFIED_SIGNAL, minimum=1, timeout=3)
            if len(streams) < 1:
                print("Missing LSL stream")
                sys.exit()
            self.class_lsl_inlet = StreamInlet(streams[0], max_buflen=360, max_chunklen=1, recover=True)

        self.lsl_stream_info = StreamInfo(
            globals.STREAM_NAME_FEEDBACK_STATES,
            'mixed',
            2, #self.NUM_OUTPUT_CHANNELS,
            globals.FEEDBACK_FRAMERATE,
            'float32', # self.CHANNEL_FORMAT,
            globals.STREAM_NAME_FEEDBACK_STATES+str(random.randint(100000, 999999))
        )
        LSLStreamInfoInterface.add_channel_names(self.lsl_stream_info, self.OUTPUT_CHANNEL_NAMES)
        LSLStreamInfoInterface.add_parameters(self.lsl_stream_info, self.parameters)

        self.lsl_outlet = StreamOutlet(self.lsl_stream_info, chunk_size=10)

        # data handling threads
        self.data_thread = Thread(target=self.data_handler, daemon=True)
        self.data_thread.start()

        if self.display_relax:
            self.class_data_thread = Thread(target=self.class_data_handler, daemon=True)
            self.class_data_thread.start()

        self.setWindowTitle("BeamBCI Feedback App")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) if frameless else None
        self.move(left, top)

        # create a main widget with black background
        self.mainwidget = QWidget()
        self.mainwidget.setStyleSheet("QWidget{ background-color: #000000; }")
        self.setCentralWidget(self.mainwidget)

        # create pacman widgets
        # self.pacman_left = PacmanWidget()
        # self.pacman_right = PacmanWidget(180)

        # create relax widget
        if self.display_relax:
            self.relax_widget = RelaxFeedbackWidget()

        # create text display widget
        self.text_widget = TextWidget()
        self.text_widget.setText("")



        # create a grid layout and set all rows and columns to have equal size
        lay = QGridLayout()
        for i in range(10):
            lay.setColumnStretch(i, 1)
            lay.setRowStretch(i, 1)

        # add widgets to the layout
        lay.addWidget(self.text_widget, 8, 1, 2, 8)
        #if self.display_pacman:
        #    lay.addWidget(self.pacman_left, 2, 3, 4, 4) if self.side == Side.LEFT else None
        #    lay.addWidget(self.pacman_right, 2, 3, 4, 4) if self.side == Side.RIGHT else None
        if self.display_relax:
            lay.addWidget(self.relax_widget, 2, 3, 4, 4)



        # use the layout for the main widget
        self.mainwidget.setLayout(lay)

        # setup redraw timer at 60Hz
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.trigger_update)
        self.timer.start(int(round(1000/self.fps)))
        self.lastUpdate = time.time()

        # open the window
        if fullscreen:
            self.showFullScreen()
        elif maximized:
            self.showMaximized()
        else:
            self.resize(width, height)
            self.show()

        # create beam widgets
        pacman_angle = 0
        if self.side == Side.RIGHT:
            pacman_angle = 180

        debug = False
        self.beam_widget_upper_arm = BeamWidget(default_angle=90, debug=debug)
        self.beam_widget_forearm = BeamWidget(debug=debug)
        self.pa = PacmanWidget1(rotation=pacman_angle, radius=100, debug = debug)

        lay.addWidget(self.beam_widget_upper_arm, 0, 0, 10, 10)
        lay.addWidget(self.beam_widget_forearm, 0, 0, 10, 10)
        lay.addWidget(self.pa, 0, 0, 10, 10)

        self.hand_closed_percent = 0
        self.arm_closed_percent = 0

        self.exo_state = ExoState.STOP

        self.lastT = None


    # function to trigger a redraw
    def trigger_update(self):

        # if closing the window was requested externally, close the window
        if self.close_sheduled:
            print("close requested")
            self.close()
            return

        t_now = clock()
        if self.lastT is not None:
            dT = t_now - self.lastT
        else:
            dT = 1 / globals.FEEDBACK_FRAMERATE
        self.lastT = t_now

        if self.exo_state == ExoState.OPEN or self.exo_state == ExoState.HIDE_OPEN:
            self.hand_closed_percent -= dT * 100 / self.time_open_hand

        elif self.exo_state == ExoState.CLOSE or self.exo_state == ExoState.HIDE_CLOSE:
            self.hand_closed_percent += dT * 100 / self.time_close_hand

        if self.exo_state == ExoState.OPEN_ARM or self.exo_state == ExoState.HIDE_OPEN_ARM:
            self.arm_closed_percent -= dT * 100 / self.time_open_arm

        elif self.exo_state == ExoState.CLOSE_ARM or self.exo_state == ExoState.HIDE_CLOSE_ARM:
            self.arm_closed_percent += dT * 100 / self.time_close_arm


        self.hand_closed_percent = min(100, max(0, self.hand_closed_percent))
        self.arm_closed_percent = min(100, max(0, self.arm_closed_percent))


        # update the GUI
        self.update()

        # after GUI was updated, push the displayed pacman positions to LSL stream
        self.lsl_outlet.push_sample([self.hand_closed_percent, self.arm_closed_percent])

        w = self.beam_widget_upper_arm.size().width()
        h = self.beam_widget_upper_arm.size().height()
        s = h

        x_offset = int( (w-h) / 2 )
        y_offset = 0

        if w < h:
            s = w
            x_offset = 0
            y_offset = int( (h-w) / 2 )

        x1 = x_offset + round(0.15 * s)
        if self.side == Side.RIGHT:
            x1 = x_offset + round((1-0.15) * s)

        l1 = round(0.40*s)
        w1 = round(0.27*s)

        l2 = round(0.45*s)
        w2 = round(0.2*s)

        if self.side == Side.LEFT:
            arm_angle = 90 - self.arm_closed_percent * 0.9
        else:
            arm_angle = 90 + self.arm_closed_percent * 0.9

        self.beam_widget_upper_arm.update_geometry(x1, y_offset-round(w1/2), l1, w1, 0)

        self.beam_widget_forearm.update_geometry(self.beam_widget_upper_arm.end_x, self.beam_widget_upper_arm.end_y, l2, w2, arm_angle)

        self.pa.x = self.beam_widget_forearm.pivot2_x + self.beam_widget_forearm.radius + self.pa.r + round(0.015*s)
        if self.side == Side.RIGHT:
            self.pa.x = self.beam_widget_forearm.pivot2_x - self.beam_widget_forearm.radius - self.pa.r - round(0.015*s)
        self.pa.y = self.beam_widget_forearm.pivot2_y
        self.pa.r = round(0.15*s)

        self.pa.closed_percent = self.hand_closed_percent



    # function to be executed in a separate thread -> fetches LSL data and updates GUI states
    def data_handler(self):

        # is started as daemon -> while true is ok.
        while True:

            # try to pull a sample from lsl stream
            sample, timestamp = self.lsl_inlet.pull_sample(timeout=1)

            # if successful, process information
            if sample is not None:
                
                self.state_display_text = int(sample[0])

                if not (int(sample[0]) == Cue.RELAX.value and self.display_relax == False):
                    self.text_widget.setText(DisplayText[int(sample[0])])
                elif (int(sample[0]) == Cue.RELAX.value):
                    self.text_widget.setText(DisplayText[int(sample[0])])

                if self.display_relax:
                    self.relax_widget.state = int(sample[0])

                if self.side == Side.LEFT:
                    self.exo_state = ExoState(int(sample[1]))
                else:
                    self.exo_state = ExoState(int(sample[2]))

            else:
                print("No samples received within 1s.")

    # function to be executed in a separate thread -> fetches LSL data and updates GUI states
    def class_data_handler(self):

        # is started as daemon -> while true is ok.
        while True:

            # try to pull a sample from lsl stream
            sample, timestamp = self.class_lsl_inlet.pull_sample(timeout=1)

            # if successful, process information
            if sample is not None:

                if self.side == Side.RIGHT:
                    norm_val = int(sample[0]) # normalized c3 sample
                    thresh = float(
                        self.class_lsl_inlet.info().desc() \
                            .child('parameters').child('ThresholdC3') \
                            .child_value()
                    )
                elif self.side == Side.LEFT:
                    norm_val = int(sample[1]) # normalized c4 sample
                    thresh = float(
                        self.class_lsl_inlet.info().desc() \
                            .child('parameters').child('ThresholdC4') \
                            .child_value()
                    )
                else:
                    norm_val = 0.5 * int(sample[0]) + int(sample[1])
                    thresh_right = float(
                        self.class_lsl_inlet.info().desc() \
                            .child('parameters').child('ThresholdC3') \
                            .child_value()
                    )   
                    thresh_left = float(
                        self.class_lsl_inlet.info().desc() \
                            .child('parameters').child('ThresholdC4') \
                            .child_value()
                    )
                    thresh = 0.5 * (thresh_right + thresh_left)

                # use negated thresh since thresh is stored as positive value
                self.relax_widget.relax_value = 1 - (norm_val/-thresh)

            else:
                print("No samples received within 1s.")


def demo_thread():

    stream_info = StreamInfo(
        globals.STREAM_NAME_TASK_EVENTS,
        'mixed',
        3, #self.NUM_OUTPUT_CHANNELS,
        10, #self.OUTPUT_SAMPLING_RATE,
        'int16', # self.CHANNEL_FORMAT,
        globals.STREAM_NAME_TASK_EVENTS+str(random.randint(100000, 999999))
    )

    outlet = StreamOutlet(stream_info, chunk_size=1)
    print("Demo Outlet created")

    time.sleep(2)

    outlet.push_sample([0, 0, 0])
    time.sleep(1)

    # start in 5 seconds
    outlet.push_sample([3, 0, 0])
    time.sleep(2)
    outlet.push_sample([0, 0, 0])
    time.sleep(3)

    # close hand
    outlet.push_sample([1, 2, 2])
    time.sleep(2.5)
    outlet.push_sample([0, 0, 0])
    time.sleep(2.5)

    # open hand
    outlet.push_sample([2, 1, 1])
    time.sleep(2.5)
    outlet.push_sample([0, 0, 0])
    time.sleep(2.5)

    # close arm
    outlet.push_sample([1, 22, 22])
    time.sleep(2.5)
    outlet.push_sample([0, 0, 0])
    time.sleep(2.5)

    # open arm
    outlet.push_sample([2, 11, 11])
    time.sleep(2.5)
    outlet.push_sample([0, 0, 0])
    time.sleep(2.5)

    # end
    outlet.push_sample([4, 0, 0])
    time.sleep(2)

    outlet.push_sample([0, 0, 0])
    time.sleep(1)

    print("Demo finished.")

    global window
    window.close_sheduled = True
    time.sleep(1)


if __name__ == "__main__":

    app = QApplication(sys.argv)


    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--maximized', type=int, default=1)
    parser.add_argument('--frameless', type=int, default=0)
    parser.add_argument('--stay_on_top', type=int, default=0)
    parser.add_argument('--width', type=int, default=1000)
    parser.add_argument('--height', type=int, default=700)
    parser.add_argument('--left', type=int, default=0)
    parser.add_argument('--top', type=int, default=0)
    parser.add_argument('--side', type=str, required=True)
    parser.add_argument('--showpacman', type=int, required=True)
    parser.add_argument('--showopen', type=int, required=True)
    parser.add_argument('--time_open_hand', type=float, default=0.5)
    parser.add_argument('--time_close_hand', type=float, default=2.0)
    parser.add_argument('--time_open_arm', type=float, default=1.5)
    parser.add_argument('--time_close_arm', type=float, default=3.0)
    parser.add_argument('--fps', type=int, default=0)
    parser.add_argument('--demo', type=int, default=0)

    args = parser.parse_args()

    maximized = bool(args.maximized)
    frameless = bool(args.frameless)
    stay_on_top = bool(args.stay_on_top)


    side = Side.RIGHT if args.side.upper() == "RIGHT" else Side.LEFT
    show_open = bool(args.showopen)
    show_pacman = bool(args.showpacman)


    # Search in command line arguments for demo argument
    demo = args.demo == 1

    if demo:
        t = Thread(target=demo_thread, daemon=True)
        t.start()


    # create Desktop-Object to determine number of available screens and resolution
    desktopObject = app.desktop()
    num_screens = desktopObject.screenCount()
    
    # if there is only one screen available, start in windowed mode
    if num_screens == 1:
        left = desktopObject.screenGeometry(0).left()
        top = desktopObject.screenGeometry(0).top()

        if not maximized:
            left += args.left
            top += args.top

        window = SinglePacmanFeedbackApp(
            left, top, width=args.width, height=args.height,
            maximized=maximized, fullscreen=False, frameless=frameless, stay_on_top=stay_on_top, fps=args.fps,
            side=side,
            display_pacman=show_pacman,
            display_relax=show_open,
            time_open_hand=args.time_open_hand, time_close_hand=args.time_close_hand,
            time_open_arm=args.time_open_arm, time_close_arm=args.time_close_arm
        )

    # if there is more than one screen, start in fullscreen mode on second screen
    elif num_screens > 1:
        left = desktopObject.screenGeometry(1).left()
        top = desktopObject.screenGeometry(1).top()

        if not maximized:
            left += args.left
            top += args.top

        window = SinglePacmanFeedbackApp(
            left, top, width=args.width, height=args.height,
            maximized=maximized, fullscreen=maximized, frameless=True, stay_on_top=stay_on_top, fps=args.fps,
            side=side,
            display_pacman=show_pacman,
            display_relax=show_open,
            time_open_hand=args.time_open_hand, time_close_hand=args.time_close_hand,
            time_open_arm=args.time_open_arm, time_close_arm=args.time_close_arm
        )

    sys.exit(app.exec_())
