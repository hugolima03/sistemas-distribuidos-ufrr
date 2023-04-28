import os
import time
import socket
import random
import threading

SERVER_ADDRESS = "localhost"
SERVER_PORT = 12345

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


def send_message(client_socket):
    for i in range(10):
        message = _1024ByteMessage
        client_socket.send(message)
        time.sleep(random.random() * 5)
    print('Stopping conections')
    client_socket.send('quit'.encode())


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()


if __name__ == '__main__':
    n = int(input('Número de conexões simultaneas: '))
    for i in range(int(n)):
        start_client()
