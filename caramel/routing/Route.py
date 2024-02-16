from caramel.routing.RoutePath import RoutePath

class Route:

    # static dict to hold all the routes
    # path as key and handler and method as value
    routes = {}

    @staticmethod
    def get(path, handler):
        # Route.routes['GET'].append({'path': RoutePath(path), 'handler': handler})
        # check if 'get' is in keys
        # if not, add it and set it to an empty list
        # then append the new route to the list
        if 'GET' not in Route.routes:
            Route.routes['GET'] = []
        
        Route.routes['GET'].append({'path': RoutePath(path), 'handler': handler})

    @staticmethod
    def post(path, handler):
        Route.routes['POST'] = {'path': RoutePath(path), 'handler': handler}
    
    @staticmethod
    def resolve(method, path):

        # remove trailing slash
        if path.endswith("/"):
            path = path[:-1]

        # check if method is in routes
        if method not in Route.routes:
            print("Method not found")
            return None
        
        # get the routes for the method
        routes = Route.routes[method]
        # iterate through the routes
        for route in routes:
            # get the path
            route_path = route['path']
            # check if the path matches
            params = route_path.match(path)
            if params is not None:
                return {'handler': route['handler'], 'params': params}
        
        print("Route not found")
        return None

        
            

        