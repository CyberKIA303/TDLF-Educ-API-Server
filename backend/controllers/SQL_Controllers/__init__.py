import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .execution import execute_query_on_connection
from .. import (nodes, letters)
from .dowload_books_controller import (Author, Book_Authors, Book_Availability, Book, School)
from .quize_controller import (Course, Quiz, Quiz_Content)
from .user_lab_controllers import (User_Info, My_Course)