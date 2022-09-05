from misc.timing import clock
import logging
from logging import DEBUG, INFO, WARNING, ERROR

from PyQt5.QtGui import QColor

SUCCESS = 25


LOGGER_BASENAME = 'pythonbci'

# Defines in which color the log levels should be displayed
LogColors = {
    DEBUG: QColor("#000000"),
    SUCCESS: QColor("#00FF00"),
    INFO: QColor("#000000"),
    WARNING: QColor("#997700"),
    ERROR: QColor("#990000")
}

class PythonbciLogHandler(logging.StreamHandler):
    # This is a custom StreamHandler which collects the LogRecords coming from all instances
    # For proper display of the time in which a log arrived it needs to know a starting time (supplied by MainProgram)
    def __init__(self, start_clock):
        super().__init__()

        self.start_clock = start_clock
        self.records = []

    def emit(self, record: logging.LogRecord) -> None:
        # Receives a LogRecord, adds a time (how long pythonbci has been running (in [s])) and appends it to the records
        record.time = clock() - self.start_clock

        self.records.append(record)

    def get_records(self):
        # Returns the list of new records since last query
        records = self.records.copy()
        self.records = []
        return records

def initialize_logger(start_clock, level=logging.DEBUG) -> PythonbciLogHandler:
    logging.SUCCESS = SUCCESS
    logging.addLevelName(SUCCESS, "SUCCESS")

    # Adding a method for logging "success" to the logging library
    # Adapted from https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility/13638084#13638084
    def success(self, msg, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        self._log(SUCCESS, msg, args, **kws)

    logging.Logger.success = success

    # Configure a logger instance which can be found by all modules
    # It is started with the base name, each module should create its own subname
    logger = logging.getLogger(LOGGER_BASENAME)
    logger.setLevel(level=level)

    # Add a StreamHandler which logs all log-messages to the console
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(level)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s - %(levelname)s: %(funcName)s - %(message)s'))
    logger.addHandler(consoleHandler)

    # Add our StreamHandler which collects the log messages for display in the GUI
    pbciLogHandler = PythonbciLogHandler(start_clock=start_clock)
    pbciLogHandler.setLevel(level)
    logger.addHandler(pbciLogHandler)

    return pbciLogHandler

def getLogger(name):
    return logging.getLogger(f"{LOGGER_BASENAME}.{name}")