import socket
from cryptography.fernet import Fernet

# Chave secreta compartilhada entre o cliente e o servidor
# Certifique-se de usar a mesma chave secreta utilizada no servidor
chave_secreta = b'chave_secreta_aqui'

HOST = 'localhost'
PORT = 5000

def enviar_mensagem(mensagem):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Criando um objeto Fernet com a chave secreta
    fernet = Fernet(chave_secreta)

    # Codificando a mensagem
    mensagem_codificada = fernet.encrypt(mensagem.encode())

    s.sendall(mensagem_codificada)

    data = s.recv(1024)
    print(f'Resposta do servidor: {data.decode()}')
    s.close()

mensagem = 'Olá, servidor!'
enviar_mensagem(mensagem)
