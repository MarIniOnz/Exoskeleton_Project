from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QMessageBox
from threading import Thread

# runs the given function in a new Thread
def fireoffFunction(func):
    t = Thread(daemon=True, target=func)
    t.start()


# displays a MessageBox with given text
def alert(text: str):

    msg = QMessageBox()
    msg.setWindowTitle("Message:")
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Close)
    msg.exec_()


# helper class for QLabel with Bold text
class BoldLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("QLabel{ font-weight: bold; }")


# helper class for QLabel to be used as headline
class HeadlineLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("QLabel { font-weight: 300; font-size: 16pt; }")
