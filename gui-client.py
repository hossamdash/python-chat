from PySide2 import QtCore, QtWidgets
import sys, threading, socket, time


class SocketChat:
    def __init__(self):
        self.nickname = "Hossam"
        # Server Ip and Port
        self.IP = "127.0.0.1"
        self.PORT = 55555
        self.client_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM
        )
        self.connection = True

    # Listening to Server and Sending Nickname
    def receive(self):
        # Receive Message From Server
        # If 'Nickname?' Send Nickname
        message = self.client_socket.recv(1024).decode("utf-8")
        if message == "/id":
            self.client_socket.send(self.nickname.encode("utf-8"))
        else:
            return message
            # print('{}{} : {}'.format(bcolors.OKGREEN, self.nickname, bcolors.ENDC))

    # Sending Messages To Server
    def write(self, msg: str):
        message = msg
        self.client_socket.send(message.encode("utf-8"))
        if message.startswith("/"):
            self.handleCommand(message[1:])

    def handleCommand(self, command: str):
        if command == "exit":
            return 404  # status code for exit


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.chat_object = SocketChat()
        self.title = QtWidgets.QLabel(
            "Welcome to the simple interactive modular python chat aka S.I.M.P",
            alignment=QtCore.Qt.AlignCenter,
        )
        self.nickname_field = QtWidgets.QLabel("nickname: Hossam")
        self.message_area = QtWidgets.QTextEdit()
        self.input = QtWidgets.QLineEdit("enter message here")
        self.connect_button = QtWidgets.QPushButton("Connect")

        self.layout = QtWidgets.QVBoxLayout()

        # self.top_row = QtWidgets.QHBoxLayout()
        # self.layout.addWidget(self.nickname_label)
        self.layout.addWidget(self.nickname_field)
        self.layout.addWidget(self.message_area)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.connect_button)
        # self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)

        self.connect_button.clicked.connect(self.beginConnection)
        self.input.returnPressed.connect(self.write)

    @QtCore.Slot()
    def beginConnection(self):
        self.connect_button.setText("Connecting...")
        time.sleep(2)
        self.chat_object.client_socket.connect(
            (self.chat_object.IP, self.chat_object.PORT)
        )
        self.connect_button.setText("Connected")

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        # self.edit.setText(self.chat.receive())

    def receive(self):
        while True:
            msg: str = self.chat_object.receive()
            self.message_area.append(msg)

    @QtCore.Slot()
    def write(self):
        msg = self.input.text()
        self.chat_object.write(msg)

    def terminateConnection(self):
        print("You exited the chat!")
        self.connection = False
        self.client_socket.close()
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
