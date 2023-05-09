import time
import socket
import threading

SERVER_ADDRESS = "localhost"
SERVER_PORT = 12345

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
    connected = True
    while connected:
        message = input("Digite uma mensagem: \n")
        if message == 'quit':
            connected = False
            print(bcolors.WARNING + 'Quitting application... Now you can stop the process' + bcolors.ENDC)
        start_time = time.time()
        client_socket.send(message.encode())
        print("--- Tempo de execução: %s seconds ---" % (time.time() - start_time))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

send_thread = threading.Thread(target=send_message, args=(client_socket,))
send_thread.start()

while True:
    message = client_socket.recv(1024).decode()
    print(bcolors.OKGREEN + "Mensagem recebida do servidor: " + message + bcolors.ENDC)
