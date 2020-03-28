import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('Basic form sheet')

layout = QFormLayout()
layout.addRow('Name:-', QLineEdit())
layout.addRow('Password:-',QLineEdit())
layout.addRow('Age:-',QLineEdit())

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
