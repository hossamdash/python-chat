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

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Server Ip and Port
IP = "127.0.0.1"
PORT = 55555

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client_socket.connect((IP, PORT))


# Listening to Server and Sending Nickname
def receive():
    global receive_state
    while receive_state:
        # Receive Message From Server
        # If 'Nickname?' Send Nickname
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'Nickname?':
            client_socket.send(nickname.encode('utf-8'))
        else :
            print(message)
            print('{}{} : {}'.format(bcolors.OKGREEN, nickname, bcolors.ENDC))


# Sending Messages To Server
def write():
    global receive_state
    while True:
        message_content = input('{}{} : {}'.format(bcolors.OKGREEN, nickname, bcolors.ENDC))
        message = '\n{}{}{}: {}{}'.format(bcolors.OKBLUE, bcolors.BOLD, nickname, bcolors.ENDC, message_content)
        client_socket.send(message.encode('utf-8'))
        if "!exit" in message_content:
            print("You exited the chat!")
            receive_state = False
            client_socket.close()
            sys.exit()
            break

receive_state = True
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()