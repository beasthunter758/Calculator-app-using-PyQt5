import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('This is the main window title')
        self.setCentralWidget(QLabel("This is the main widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusbar()

        def _createMenu(self):
            