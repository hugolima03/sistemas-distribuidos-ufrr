import os
import socket
import threading

pid = os.getpid()
print('Número do processo', pid)
# Endereço e porta do servidor
SERVER_ADDRESS = "localhost"
SERVER_PORT = 5055

# Lista de clientes conectados
clients = []
# Função que lida com as mensagens enviadas pelos clientes
def handle_message(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'quit':
                # Remove o cliente da lista quando a conexão é encerrada
                print(f'cliente {address} desconectou')
                clients.remove(client_socket)
                break
            print(f"Mensagem recebida de {address}: {message}")
            # Envia a mensagem de volta para todos os clientes conectados
            for c in clients:
                c.send(message[::-1].encode())
                # if c != client_socket:
                #     c.send(message.encode())
        except:
            # Remove o cliente da lista quando ocorre um erro de conexão
            clients.remove(client_socket)
            break

# Cria o socket do servidor e configura para aceitar conexões de clientes
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen()

print(f"Servidor iniciado em {SERVER_ADDRESS}:{SERVER_PORT}")

# Loop principal que aceita conexões de clientes e cria uma thread para cada conexão
while True:
    client_socket, address = server_socket.accept()
    print(f"Novo cliente conectado: {address}")
    # Adiciona o novo cliente à lista de clientes conectados
    clients.append(client_socket)
    # Cria uma nova thread para lidar com as mensagens do cliente
    message_thread = threading.Thread(target=handle_message, args=(client_socket, address))
    message_thread.start()
