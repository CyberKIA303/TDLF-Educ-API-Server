import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection)
import uuid

data = [
    {"element_name": "quiz_content_id", "element_row": 0},
    {"element_name": "initial",         "element_row": 1},
    {"element_name": "content",         "element_row": 2},
    {"element_name": "quiz_id",         "element_row": 3}
]
    
class Quiz_Content:
    def create_quiz_content(initial: str, content: str, quiz_id: str):
        u_id = str(uuid.uuid4())
        query = """
            INSERT INTO quiz_content(quiz_content_id, initial, content, quiz_id)
            VALUES (%(u_id)s, %(initial)s, %(content)s, %(quiz_id)s)
        """
        values = {
            "u_id": u_id,
            "initial": initial,
            "content": content,
            "quiz_id": quiz_id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_quiz_content(quiz_id: str):
        query = """
            SELECT * FROM quiz_content
            WHERE quiz_id = %(quiz_id)s
            ORDER BY initial ASC
        """
        values = {"quiz_id": quiz_id}
        response = execute_query_on_connection(nodes=nodess, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_quiz_content_by_id(id: str):
        query = """
            SELECT * FROM quiz_content
            WHERE quiz_content_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodess, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_quiz_content(id: str, initial: str, content: str):
        query = """
            UPDATE quiz_content SET
            initial = %(initial)s,
            content = %(content)s
            WHERE quiz_content_id = %(id)s
        """
        values = {
            "initial": initial,
            "content": content,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodess, query=query, values=values)
        return response
    
    def delete_quiz_content(id: str):
        query = """
            DELETE FROM quiz_content
            WHERE quiz_content_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodess, query=query, values=values)
        return response
    