from http.server import BaseHTTPRequestHandler
from functools import cached_property
from http.cookies import SimpleCookie
from urllib.parse import parse_qsl, urlparse
from caramel.routing.Route import Route
from caramel.com import response_instance as Response
from caramel.com.Response import Response as ResponseClass
from caramel.session.Session import Session

class CaramelRequestHandler(BaseHTTPRequestHandler):

    current_method = None

    server_version = "CaramelServer/0.1"
    sys_version = ""
    protocol_version = "HTTP/1.1"
    server_name = "CaramelServer/0.1"
    

    def do_GET(self):
        self.close_connection = True
        response = self.get_response()
        # check if response is instance of Response
        if not isinstance(response, ResponseClass):
            raise ValueError("Response must be an instance of Response")
        
        response.send(self)

        

    def do_POST(self):
        self.do_GET()

    @cached_property
    def url(self):
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        return dict(parse_qsl(self.url.query))

    @cached_property
    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    @cached_property
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode("utf-8")))

    @cached_property
    def cookies(self):
        return SimpleCookie(self.headers.get("Cookie"))
    
    def get_response(self):

        # check if session cookie is set
        session_id = self.cookies.get("session_id")
        if session_id is not None and session_id.value is not None:
            Session().start(session_id.value)
        else:
            Session().start()

        request_data = { "path": self.url.path,"query_data": self.query_data, "post_data": self.post_data.decode("utf-8"), "form_data": self.form_data, "cookies": { name: cookie.value for name, cookie in self.cookies.items()}, "method": self.current_method }
        route = Route.resolve(self.command, self.url.path)
        if route is None:
            return Response.error(404, "Not Found")
        handler = route['handler']
        params = route['params']
        return handler(request_data, **params)
        



    