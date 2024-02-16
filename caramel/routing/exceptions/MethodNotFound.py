

class MethodNotFound(Exception):
    def __init__(self, method, handler):
        self.method = method
        self.handler = handler
        self.message = f"Method {method} not found in {handler}"

    def __str__(self):
        return self.message