import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection, letters)
from fastapi import HTTPException
from backend.security.password_handler import hash_password

class User_Info:
    data = [
        {"element_name": "user_info_id",  "element_row": 0},
        {"element_name": "username",      "element_row": 1},
        {"element_name": "user_email",    "element_row": 2},
        {"element_name": "user_status",   "element_row": 4} 
    ]
    
    def create_user_info(name: str, email: str, password: str, status: str):
        ons: str = letters.uppercase(name)
        query = """
            INSERT INTO user_info(username, user_email, user_password, user_status, ons)
            VALUES (%(name)s, %(email)s, %(password)s, %(status)s, %(ons)s)
        """
        values = {
            "name": name,
            "email": email,
            "password": hash_password(password),
            "status": status,
            "ons": ons
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_user_info(page: int = None):
        offset: int = 0
        if page:
            offset = (page - 1) * 10
        query = """
            SELECT * FROM user_info
            ORDER BY username ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_user_info_by_id(id: str):
        query = """
            SELECT * FROM user_info
            WHERE user_info_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_user_info_by(search_by: str, search: str, page: int = None):
        ons: str = f"%{letters.uppercase(search)}%"
        offset: int = 0
        if page:
            offset = (page - 1) * 10
        query: str = """
            SELECT * FROM user_info
            WHERE user_email = %(email)s
        """
        values: dict = {"email": search}
        if search_by == "username":
            query = """
                SELECT * FROM user_info
                WHERE ons ILIKE %(ons)s
                ORDER BY username ASC
                LIMIT 10 OFFSET %(offset)s
            """
            values = {"ons": ons, "offset": offset}
        elif search_by == "user_email":
            query = """
                SELECT * FROM user_info
                WHERE user_email = %(search)s
            """
            values = {"search": search}
        elif search_by == "user_status":
            query = """
                SELECT * FROM user_info
                WHERE user_status = %(search)s
                ORDER BY username ASC
                LIMIT 10 OFFSET %(offset)s
            """
            values = {"search": search, "offset": offset}
        else:
            raise HTTPException(500, "Invalid Input!")
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_user_info(id: str, name: str, email: str, password: str):
        query = """
            UPDATE user_info SET
            username = %(name)s,
            user_email = %(email)s,
            user_password = %(password)s
            WHERE user_info_id = %(id)s
        """
        values = {
            "name": name,
            "email": email,
            "password": hash_password(password),
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_user_info(id: str):
        query = """
            DELETE FROM user_info
            WHERE user_info_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response