import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from functions import letters
from ..connection import nodes
from .SQL_Controllers import (
    Author, Book_Authors, Book_Availability, Book, School,
    Course, Quiz, Quiz_Content,
    User_Info, My_Course
)