from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from PySide2 import QtCore, QtWidgets, QtGui
import socket
import threading
import sys
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QLineEdit("Enter your nickname", )
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        # self.text.setText(random.choice(self.hello) + " " + str(self.edit.text()))
        self.text.setText("Connect")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    # widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())