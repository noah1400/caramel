import json as json_module
from http.server import BaseHTTPRequestHandler
from caramel.session.Session import Session

class Response:

    def __init__(self):
        self.status_code = 200
        self.data = None
        self.headers = {}

    def json(self, data):
        self.data = json_module.dumps(data)
        self.headers["Content-Type"] = "application/json"
        return self
    
    def text(self, data, status_code=200):
        self.status_code = status_code
        self.data = data
        self.headers["Content-Type"] = "text/plain"
        return self
    
    def error(self, status_code, message):
        self.status_code = status_code
        self.data = message
        self.headers["Content-Type"] = "text/plain"
        return self
    
    def redirect(self, location):
        self.status_code = 302
        self.headers["Location"] = location
        return self
    
    def set_cookie(self, key, value, max_age=None, expires=None, path="/", domain=None, secure=False, httponly=False, samesite=None):
        cookie = f"{key}={value}"
        if max_age:
            cookie += f"; Max-Age={max_age}"
        if expires:
            cookie += f"; Expires={expires}"
        if path:
            cookie += f"; Path={path}"
        if domain:
            cookie += f"; Domain={domain}"
        if secure:
            cookie += "; Secure"
        if httponly:
            cookie += "; HttpOnly"
        if samesite:
            cookie += f"; SameSite={samesite}"
        self.headers["Set-Cookie"] = cookie
        return self
    
    def add_content_length(self):
        self.headers["Content-Length"] = str(len(self.data.encode("utf-8").decode("utf-8")))
        return self
    
    def send(self, request_handler: BaseHTTPRequestHandler):

        self.add_content_length()

        if Session().started and Session().id is not None:
            self.set_cookie("session_id", Session().id)
            Session().serialize()
            Session().clear() # clear session data for next request
        else:
            # clear cookie exists
            self.set_cookie("session_id", "", max_age=0)

        request_handler.send_response(self.status_code)
        for key, value in self.headers.items():
            request_handler.send_header(key, value)
        request_handler.end_headers()
        if self.data is not None:
            request_handler.wfile.write(self.data.encode("utf-8"))
        return self
    
    def clear(self):
        self.status_code = 200
        self.data = None
        self.headers = {}
        return self
