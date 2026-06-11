import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection, letters)

class My_Course:
    data = [
        {"element_name": "my_course_id", "element_row": 0},
        {"element_name": "user_info_id", "element_row": 1},
        {"element_name": "course_id",    "element_row": 2}
    ]
    
    def create_my_course(user: str, course: str):
        query = """
            INSERT INTO my_course(user_info_id, course_id)
            VALUES (%(user)s, %(course)s)
        """
        values = {
            "user": user,
            "course": course
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_my_course(user: str, page: int = None):
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM my_course
            WHERE user_info_id = %(user)s
            ORDER BY course_id ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {
            "user": user,
            "offset": offset
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_my_course_by_id(id: str):
        query = """
            SELECT * FROM my_course
            WHERE my_course_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def delete_my_course(id: str):
        query = """
            DELETE FROM my_course
            WHERE my_course_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response