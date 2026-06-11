import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .endpoints import get_all_routes
from functions import letters
from .database import create_tables