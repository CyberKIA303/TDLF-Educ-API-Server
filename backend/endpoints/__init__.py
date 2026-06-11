import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .SQL_Routes import get_all_routes
from .auth_endpoints import AuthRoute

old_get_all_routes = get_all_routes

def get_all_routes():
    routes = old_get_all_routes()
    routes.append(AuthRoute)
    return routes