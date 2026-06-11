import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .. import (nodes, execute_query_on_connection, letters)
from .course_controller import Course
from .quiz_controller import Quiz
from .quiz_content_controller import Quiz_Content