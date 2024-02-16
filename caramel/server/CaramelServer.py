from http.server import HTTPServer, SimpleHTTPRequestHandler
from caramel.server.handler.CaramelRequestHandler import CaramelRequestHandler
from caramel.com.Response import Response

response_instance = Response()

class CaramelServer():
    def __init__(self, server_address):
        self.server_version = "CaramelServer/0.1"
        self.sys_version = ""
        self.protocol_version = "HTTP/1.1"
        self.server_name = "CaramelServer/0.1"
        self.server_address = server_address
        self.server = HTTPServer(self.server_address, CaramelRequestHandler)

    def start(self):
        print(f"Server started at {self.server_address[0]}:{self.server_address[1]}")
        self.server.serve_forever()

    

    