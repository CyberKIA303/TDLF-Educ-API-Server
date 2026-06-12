import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection)
import uuid

data = [
    {"element_name": "quiz_id",        "element_row": 0},
    {"element_name": "question",       "element_row": 1},
    {"element_name": "quiz_type",      "element_row": 2},
    {"element_name": "correct_answer", "element_row": 3},
    {"element_name": "reason",         "element_row": 4},
    {"element_name": "course_id",      "element_row": 5}
]
    
class Quiz:
    def create_quiz(question: str, q_type: str, answer: str, course: int, reason: str = "N/A"):
        u_id = str(uuid.uuid4())
        query = """
            INSERT INTO quiz(quiz_id, question, quiz_type, correct_answer, reason, course_id)
            VALUES (%(u_id)s, %(question)s, %(q_type)s, %(answer)s, %(reason)s, %(course)s)
        """
        values = {
            "u_id": u_id,
            "question": question,
            "q_type": q_type,
            "answer": answer,
            "reason": reason,
            "course": course
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_quiz(course_id: str, page: int = None):
        offset: int = 0
        if page:
            offset = (page - 1) * 10
        query = """
            SELECT * FROM quiz
            WHERE course_id = %(course_id)s
            ORDER BY quiz_id ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {
            "course_id": course_id,
            "offset": offset
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_quiz_by_id(id: str):
        query = """
            SELECT * FROM quiz
            WHERE quiz_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_quiz_by_type(search: str, page: int = None):
        offset: int = 0
        if page:
            offset = (page - 1) * 10
        query = """
            SELECT * FROM quiz
            WHERE quiz_type = %(search)s
            ORDER BY quiz_id ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {
            "search": search,
            "offset": offset 
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_quiz(id: str, question: str, answer: str, reason: str):
        query = """
            UPDATE quiz SET
            question = %(question)s,
            correct_answer = %(answer)s,
            reason = %(reason)s
            WHERE quiz_id = %(id)s
        """
        values = {
            "question": question,
            "answer": answer,
            "reason": reason,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_quiz(id: str):
        query = """
            DELETE FROM quiz
            WHERE quiz_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response