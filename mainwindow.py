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
            self.menu = self.menuBar().addMenu("&Menu")
            self.menu.addAction('&Exit', self.close)

        def _createToolBar(self):
            tools = QToolBar()
            self.addToolbar(tools)
            tools.addAction('Exit', self.close)

        def _createStatusbar(self):
            status = QStatusBar()
            status.showMessage("I'm the Status Bar")
            self.setStatusbar(status)

if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())