import grpc
import remote_control_pb2
import remote_control_pb2_grpc
from  concurrent import futures

import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, filename='cmds.log', filemode='w', format='%(process)d - [%(asctime)s] : %(levelname)s -> %(message)s')

users = [
    {"name": "Hugo", "password": "RPC"},
    {"name": "Leandro Balico", "password": "ufrr"},
]

def verify_user(username, password, user_list):
    for user in user_list:
        if user["name"] == username and user["password"] == password:
            logging.debug(f'Username: {username} Autheticated')
            return True
    print('Login failed')
    return False

class RemoteControl(remote_control_pb2_grpc.RemoteControlServicer):
    def ExecCmd(self, request, context):
        if (verify_user(request.client, request.passwd, users)):
            result = subprocess.run(request.cmd.split(), capture_output=True)
            resultDecoded = result.stdout.decode()
            logging.debug(f"[{request.client}] INPUT: {request.cmd}")
            logging.debug(f"[{request.client}] OUTPUT: {resultDecoded}")
            return remote_control_pb2.CmdResponse(cmd=resultDecoded, error="0")
        else:
            return remote_control_pb2.CmdResponse(cmd='Null', error="1")

def serve():
    logging.debug(f'Iniciando servidor...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControl(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()