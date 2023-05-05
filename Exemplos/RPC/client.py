import grpc
import my_service_pb2
import my_service_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_service_pb2_grpc.MyServiceStub(channel)
        response = stub.SayHello(my_service_pb2.HelloRequest(name="Alice"))
        print(response.message)

if __name__ == "__main__":
    run()