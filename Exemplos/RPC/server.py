import grpc
import my_service_pb2
import my_service_pb2_grpc
from  concurrent import futures

class MyService(my_service_pb2_grpc.MyServiceServicer):
    def SayHello(self, request, context):
        return my_service_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()