from caramel.Caramel import Caramel
from caramel.routing.Route import Route
from caramel.com import response_instance as Response
from caramel.session.Session import Session

def home(request):
    print("home")
    return Response.text("Hello world", 200)

def homewithid(request, id):
    
    return Response.text(f"Hello world with id {id}", 402)

def setsession(request, value):
    Session().set("value", value)
    return Response.text("Session set", 200)

def getsession(request):
    value = Session().get("value")
    return Response.text(f"Session value is {value}", 200)

Route.get("/home", home)
Route.get("/homewithid/{id:[0-9]+}", homewithid)
Route.get("/setsession/{value}", setsession)
Route.get("/getsession", getsession)


caramelServer = Caramel(("127.0.0.1", 80))