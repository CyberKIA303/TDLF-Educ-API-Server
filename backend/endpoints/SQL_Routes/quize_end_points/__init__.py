import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ....controllers import (Course, Quiz, Quiz_Content)
from .course_end_point import CourseRoute
from .quiz_end_point import QuizRoute
from .quiz_content_end_point import QuizContentRoute
