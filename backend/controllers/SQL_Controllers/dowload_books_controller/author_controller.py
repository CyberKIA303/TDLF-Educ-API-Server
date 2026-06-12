import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection, letters)
import uuid

data: list = [
    {"element_name": "author_id",   "element_row": 0},
    {"element_name": "author_name", "element_row": 1}
]

class Author:
    def create_author(name: str):
        u_id = str(uuid.uuid4())
        name = letters.camelcase(name)
        osn: str = letters.uppercase(name)
        query = """
            INSERT INTO author(author_id, author_name, osn)
            VALUES (%(u_id)s, %(name)s, %(osn)s)
        """
        values = {"u_id": u_id, "name": name, "osn": osn}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_author(page: int = None):
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM author
            ORDER BY author_name ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_author_by_id(id: str):
        query = """
            SELECT * FROM author
            WHERE author_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_author_by(search: str, page: int = None):
        osn: str = f"%{letters.uppercase(search)}%"
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM author
            WHERE osn ILIKE %(osn)s
            ORDER BY author_name ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"osn": osn, "offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_author(id: str, name: str):
        osn: str = letters.uppercase(name)
        query = """
            UPDATE author SET
            author_name = %(name)s,
            osn = %(osn)s
            WHERE author_id = %(id)s
        """
        values = {
            "name": name,
            "osn": osn,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_author(id: str):
        query = """
            DELETE FROM author
            WHERE author_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response