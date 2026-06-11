import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ....controllers import (User_Info, My_Course)
from .my_course_end_point import MyCourseRoute
from .user_info_end_point import UserInfoRoute
