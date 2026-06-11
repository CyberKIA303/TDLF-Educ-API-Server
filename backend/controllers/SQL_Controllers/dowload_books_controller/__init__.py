import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .. import (nodes, execute_query_on_connection, letters)
from .author_controller import Author
from .book_authors_controller import Book_Authors
from .book_availability_controller import Book_Availability
from .book_controller import Book
from .school_controller import School