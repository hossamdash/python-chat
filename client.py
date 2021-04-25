import socket
import threading
import sys


# ANSI Colors
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


class SocketChat():
    def __init__(self):
        self.nickname = "Hossam"
        # Server Ip and Port
        self.IP = "127.0.0.1"
        self.PORT = 55555
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.connection = True


    # Listening to Server and Sending Nickname
    def receive(self):
        while self.connection:
            # Receive Message From Server
            # If 'Nickname?' Send Nickname
            message = self.client_socket.recv(1024).decode('utf-8')
            if message == 'Nickname?':
                self.client_socket.send(self.nickname.encode('utf-8'))
            else:
                print(message)
                print('{}{} : {}'.format(bcolors.OKGREEN, self.nickname, bcolors.ENDC))


    # Sending Messages To Server
    def write(self):
        while True:
            message_content = input('{}{} : {}'.format(bcolors.OKGREEN, self.nickname, bcolors.ENDC))
            message = '\n{}{}{}: {}{}'.format(bcolors.OKBLUE, bcolors.BOLD, self.nickname, bcolors.ENDC, message_content)
            self.client_socket.send(message.encode('utf-8'))
            if "!exit" in message_content:
                self.terminateConnection()


    def beginConnection(self):
        self.client_socket.connect((self.IP, self.PORT))
        receive_thread = threading.Thread(target=self.receive, args=(self,))
        receive_thread.start()

        write_thread = threading.Thread(target=self.write, args=(self,))
        write_thread.start()
    
    def terminateConnection(self):
        print("You exited the chat!")
        self.connection = False
        self.client_socket.close()
        sys.exit()

if __name__ == "__main__":
    chat = SocketChat()
    chat.beginConnection()