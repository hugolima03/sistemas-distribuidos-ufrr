import grpc
import remote_control_pb2
import remote_control_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        name = input('Digite seu nome\n')
        passwd = input('Digite sua senha\n')
        while True:
            cmd = input('Enter a command to server:\n')
            stub = remote_control_pb2_grpc.RemoteControlStub(channel)
            response = stub.ExecCmd(remote_control_pb2.CmdRequest(cmd=cmd, client=name, passwd=passwd))
            if (int(response.error) == 1):
                print('Senha ou usuário inválidos')
                break
            print('[localhost:50051] OUTPUT: ', response.cmd)

if __name__ == "__main__":
    run()