import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Calculator using PyQt5')
#window.setGeometry(100,100,280,200)
window.move(60,15)
#window.resizeEvent()
layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout)



#helloMsg = QLabel('<h1>Hey! This is my first PyQt5 design.</h1>', parent=window)
#helloMsg.move(60,15)

window.show()
sys.exit(app.exec_)

