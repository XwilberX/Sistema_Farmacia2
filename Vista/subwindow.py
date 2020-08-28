from PyQt5.QtWidgets import QMdiSubWindow, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore

class SubWindow(QMdiSubWindow):
    def createSubWindow(self):
        parent = None
        super(SubWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.resize(500,400)
