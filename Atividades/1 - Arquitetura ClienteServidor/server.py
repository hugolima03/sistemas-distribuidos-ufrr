import socket
import threading
from cryptography.fernet import Fernet

HOST = ''
PORT = 5058
SECRET_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=' # Critografia simétrica

def handle_connection(conn, addr):
    fernet = Fernet(SECRET_KEY)

    print(f'Conectado por {addr}')
    data = conn.recv(1024)
    mensagem_cifrada = data.decode()
    mensagem_decifrada = fernet.decrypt(mensagem_cifrada)
    print(f'Mensagem recebida: {mensagem_decifrada}')

    conn.sendall('Mensagem recebida com sucesso!'.encode())
    conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f'Servidor escutando na porta {PORT}...')

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()

start_server()
