from modules.module import Module

from typing import List
import os
import time
import numpy as np
import pyxdf
import pylsl
from threading import Thread

import logging
logger = logging.getLogger("pythonbci.modules.src.XDFPlayerModule")

from PyQt5 import QtGui, QtCore, QtWidgets

class CheckableComboBox(QtWidgets.QComboBox):
    # once there is a checkState set, it is rendered
    # here we assume default Unchecked
    def addItem(self, item, checked=False):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)

    def itemChecked(self, i):
        item = self.model().item(i,0)
        return item.checkState() == QtCore.Qt.Checked


class XDFPlayerModule(Module):

    # make this a runnable descendant of the module-class
    MODULE_RUNNABLE: bool = True

    MODULE_NAME: str = "XDF Player Module"
    MODULE_DESCRIPTION: str = ""

    PARAMETER_DEFINITION = [
        {
            'name': 'skip_seconds',
            'displayname': 'skip first .. seconds',
            'description': '',
            'type': float,
            'unit': 's',
            'default': 0.0
        },
        {
            'name': 'xdf_file',
            'displayname': 'XDF File',
            'description': '',
            'type': str,
            'unit': '',
            'default': ''
        }
    ]

    def __init__(self):
        super(XDFPlayerModule, self).__init__()

        self.setStatus(Module.Status.STOPPED)

        self.player: XDFPlayer = None

        self.file_loaded = False


    def initGui(self):

        Module.initGui(self)

        row: int = self.layout.rowCount()

        self.button_select = QtWidgets.QPushButton("select")
        self.button_select.clicked.connect(self.select_file)

        self.button_load = QtWidgets.QPushButton("load")
        self.button_load.clicked.connect(self.load_file)

        if self.getParameter("xdf_file") is None or self.getParameter("xdf_file").strip() == '':
            self.button_load.setDisabled(True)


        self.text_selected_file = QtWidgets.QLabel("No file selected")

        self.stream_select_box = CheckableComboBox()

        self.stream_select_box.setDisabled(True)

        #self.layout.addWidget(QtWidgets.QLabel("XDF File:"), row + 0, 0, 1, 1)
        self.layout.addWidget(self.button_select, row + 0, 1, 1, 2)
        self.layout.addWidget(self.button_load, row+0, 3, 1, 2)

        #self.layout.addWidget(self.text_selected_file, row+1, 1, 1, 3)

        self.layout.addWidget(QtWidgets.QLabel("Streams:"), row + 2, 0, 1, 1)
        self.layout.addWidget(self.stream_select_box, row + 2, 1, 1, 4)


    def select_file(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(filter="XDF Files (*.xdf)")
        self.button_load.setDisabled(False)
        self.stream_select_box.clear()
        self.stream_select_box.setDisabled(True)

        # Only put the filename into the text box below the select button to avoid resizing
        self.parameters["xdf_file"].input.setText(filepath)

        self.setParameter("xdf_file", filepath)

        self.file_loaded = False

    def load_file(self):
        if self.getParameter("xdf_file") is None or self.getParameter("xdf_file") == '':
            logger.error("Please select a file before loading")
            self.file_loaded = False
            return

        streams = pyxdf.resolve_streams(self.getParameter("xdf_file"))

        for stream in streams:
            self.stream_select_box.addItem(stream['name'] + " " + str(stream['channel_count']) + " Ch @ " + str(stream['nominal_srate']) + 'Hz', True)

        logger.info(f"Loaded {os.path.basename(self.getParameter('xdf_file'))} containing {len(streams)} streams")

        self.stream_select_box.setDisabled(False)

        self.file_loaded = True


    def start(self):

        self.setStatus(Module.Status.STARTING)

        if self.getParameter("xdf_file") is None or self.getParameter("xdf_file") == '':
            logger.error("Please select and load an xdf-file first")
            self.setStatus(Module.Status.STOPPED)
            return

        if self.getParameter("xdf_file") is not None and not self.file_loaded:
            logger.info("Automatically loading selected .xdf-file. Playing all contained streams")
            self.load_file()

        if not self.file_loaded:
            logger.info("Automatic loading failed. Please select correct file")

        channel_mask = [self.stream_select_box.itemChecked(i) for i in range(self.stream_select_box.count())]

        self.player = XDFPlayer(self.getParameter("xdf_file"), channel_mask, skip_seconds=self.getParameter('skip_seconds'))

        self.player.start()

        self.setStatus(Module.Status.RUNNING)
        logger.success(f"XDFPlayer running with streams {[stream['info']['name'][0] for stream in self.player.streams]}")

    def stop(self):

        self.setStatus(Module.Status.STOPPING)

        self.player.stop()

        self.setStatus(Module.Status.STOPPED)

    def restart(self):

        self.stop()
        time.sleep(0.5)
        self.start()


class XDFPlayer(object):

    def __init__(self, xdf_path, channel_mask = None, skip_seconds: float = 0.0, f_update: int = 100):

        self.xdf_path = xdf_path
        self.f_update: int = f_update
        self.start_clock = 0
        self.worker: Thread = None
        self.running = False
        self.streamers: List[StreamPlayer] = None

        self.streams, self.header = pyxdf.load_xdf(self.xdf_path, dejitter_timestamps=True)

        # remove streams that are not selected by channel mask
        if channel_mask is not None:

            selected_streams = []

            for i in range(len(channel_mask)):

                if channel_mask[i]:
                    selected_streams.append(self.streams[i])

            self.streams = selected_streams



        # collect the first timestamp of all streams which contain at least 1 timestamp
        first_timestamps = []
        for s in self.streams:
            if len(s['time_stamps']) > 0:
                first_timestamps.append(s['time_stamps'][0])

        # set the lowest timestamp as the offset for all timestamps
        offset = np.min(first_timestamps)

        # offset all timestamps
        for s in self.streams:
            s['time_stamps'] -= offset


        # remove first seconds
        for s in self.streams:

            new_start_index = 0


    def start(self):

        self.streamers = []
        for s in self.streams:
            self.streamers.append(StreamPlayer(s))

        self.start_clock = pylsl.local_clock()

        self.worker = Thread(target=self.work_func, daemon=True)
        self.running = True
        self.worker.start()

    def stop(self):

        self.running = False
        time.sleep(2.0/self.f_update)
        self.streamers = None

    def work_func(self):

        while self.running:

            clock_now = pylsl.local_clock() - self.start_clock

            for player in self.streamers:

                player.update(clock_now, self.start_clock)

            time.sleep(1.0/self.f_update)

class StreamPlayer(object):

    def __init__(self, stream):

        self.time_stamps = stream['time_stamps']
        self.time_series = stream['time_series']
        self.n_samples = len(self.time_stamps)
        self.finished = self.n_samples == 0

        stream_name = stream['info']['name'][0]
        stream_type = stream['info']['type'][0]
        channel_count = int(stream['info']['channel_count'][0])
        nominal_srate = float(stream['info']['nominal_srate'][0])
        source_id = stream['info']['source_id'][0]
        channel_format = stream['info']['channel_format'][0]
        chunk_size = int(nominal_srate/50)

        info = pylsl.StreamInfo(stream_name, stream_type, channel_count, nominal_srate, channel_format, source_id)

        # add manufacturer information
        try:
            manufacturer = stream['info']['desc'][0]['manufacturer'][0]
            info.desc().append_child_value("manufacturer", manufacturer)
        except TypeError:
            logger.debug(f"Manufacturer info not available in description of stream '{stream_name}'")
        except Exception:
            logger.error(f"Could not add manufacturer to stream '{stream_name}'.")

        # add channels information
        try:
            chns = info.desc().append_child("channels")

            for chan in stream['info']['desc'][0]['channels'][0]['channel']:

                ch = chns.append_child("channel")

                for k in chan.keys():

                    val = chan[k][0]

                    ch.append_child_value(k, val)

        except Exception:
            print("Could not add channels metadata to stream '" + stream_name + "'.")

        self.outlet: pylsl.StreamOutlet = pylsl.StreamOutlet(info, chunk_size=chunk_size, max_buffered=360)

        self.next_index = 0

        if self.n_samples == 0:
            self.finished = True

    def update(self, clock, clock_offset = 0):

        while not self.finished and clock >= self.time_stamps[self.next_index]:

            self.outlet.push_sample(self.time_series[self.next_index], self.time_stamps[self.next_index] + clock_offset)
            self.next_index += 1

            if self.next_index >= self.n_samples:
                self.finished = True
