import socket
import threading
from cryptography.fernet import Fernet

# Chave secreta compartilhada entre o cliente e o servidor
chave_secreta = b'chave_secreta_aqui'

HOST = ''
PORT = 7000

def handle_client(conn, addr):
    print(f'Conectado por {addr}')
    
    # Criando um objeto Fernet com a chave secreta
    fernet = Fernet(chave_secreta)

    data = conn.recv(1024)
    mensagem_cifrada = data.decode()
    mensagem_decifrada = fernet.decrypt(mensagem_cifrada.encode())
    print(f'Mensagem recebida: {mensagem_decifrada.decode()}')

    conn.sendall('Mensagem recebida com sucesso!'.encode())
    conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)  # Aumentamos o número máximo de conexões simultâneas

    print(f'Servidor escutando na porta {PORT}...')

    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

start_server()
