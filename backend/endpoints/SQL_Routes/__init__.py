import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .download_books_end_points import (AuthorRoute, BookAuthorsRoute, BookAvailabilityRoute, BookRoute, SchoolRoute, GetBookLinkRoute)
from .quize_end_points import (CourseRoute, QuizRoute, QuizContentRoute)
from .user_lab_end_points import (UserInfoRoute, MyCourseRoute)

def get_all_routes():
    return [
        AuthorRoute, BookAuthorsRoute, BookAvailabilityRoute, BookRoute, SchoolRoute, GetBookLinkRoute,
        CourseRoute, QuizRoute, QuizContentRoute,
        UserInfoRoute, MyCourseRoute
    ]