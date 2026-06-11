import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .. import (nodes, execute_query_on_connection, letters)
from .user_info_controller import User_Info
from .my_course_controller import My_Course