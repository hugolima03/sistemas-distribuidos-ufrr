import os
import socket
import threading

SERVER_ADDRESS = "localhost"
SERVER_PORT = 5055

pid = os.getpid()
print('Número do processo', pid)

_1ByteMessage = b'\x00'
_512ByteMessage = b'\x00' * 512
_1024ByteMessage = b'\x00' * 1024


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


def receibe_message(client_socket):
    while True:
        msg = client_socket.recv(2048).decode('utf-8')
        print(msg+'\n')


def send_message(client_socket):
    while True:
        print('enviou')
        message = _1024ByteMessage
        client_socket.send(message)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    for i in range(1, 10001):
        sender_thread = threading.Thread(target=send_message, args=(client_socket,))
        receiver_thread = threading.Thread(target=receibe_message, args=(client_socket,))
        sender_thread.start()
        receiver_thread.start()
