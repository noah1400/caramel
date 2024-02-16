# Caramel

Caramel is a web framework. It is not really made for any production use. 
I started this project to learn more and dive deeper into web frameworks and improve my knowledge in python.

## Routing

Register routes:

```python
from caramel.routing.Route import Route
from caramel.com import response_instance as Response # this is not ideal will be fixed probably singleton or something

def getHandler(request):
    return Response.text("getRoute")

def parameterRoute(request, value):
    return Response.text("getRoutewithparameter"+value)

Route.get('/getRoute', getHandler)
Route.get('/routewithparameter/{value:[a-zA-Z]+}', parameterRoute)
```

## Session

```python
from caramel.session.Session import Session

def setSessionHandler(request, value):
    Session().set("value", value)
    return Response.text("Session set", 200)

def getSessionHandler(request)
    value = Session().get("value")
    return Response.text(f"Session value is {value}", 200)

```