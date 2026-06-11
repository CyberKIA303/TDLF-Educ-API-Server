import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ....controllers import (Author, Book_Authors, Book_Availability, Book, School)
from .author_end_point import AuthorRoute
from .book_authors_end_point import BookAuthorsRoute
from .book_availability_end_point import BookAvailabilityRoute
from .book_end_point import BookRoute
from .school_end_point import SchoolRoute
from .search_and_get_link_end_point import GetBookLinkRoute
