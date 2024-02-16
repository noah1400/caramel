from caramel.server.CaramelServer import CaramelServer

class Caramel:

    def __init__(self, server_address):
        self.server = CaramelServer(server_address)
        self.server.start()