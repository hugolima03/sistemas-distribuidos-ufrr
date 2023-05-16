import socket
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5058
SECRET_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

fernet = Fernet(SECRET_KEY)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
mensagem_decodificada = 'adsasdada'.encode()
mensagem_codificada = fernet.encrypt(mensagem_decodificada)

s.sendall(mensagem_codificada)
data = s.recv(1024)
print(f'Resposta do servidor: {data.decode()}')
s.close()
