from PySide2 import QtCore, QtWidgets, QLineEdit
import sys
import time


class MyApp(QtWidgets.QWidget):
    receive_state = True

    def __init__(self):
        super().__init__()

        self.edit = QLineEdit("Enter your nickname", )
        self.button = QtWidgets.QPushButton("Connect")
        self.text = QtWidgets.QLabel("Welcome to the simple interactive modular python chat aka S.I.M.P",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.initiateConnection)

    @QtCore.Slot()
    def initiateConnection(self):
        self.text.setText("Connecting...")
        time.sleep(2)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    widget = MyApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
