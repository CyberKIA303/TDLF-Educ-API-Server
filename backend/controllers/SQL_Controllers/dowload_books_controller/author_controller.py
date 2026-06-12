import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection, letters)

data: list = [
    {"element_name": "author_id",   "element_row": 0},
    {"element_name": "author_name", "element_row": 1}
]

class Author:
    def create_author(name: str):
        name = letters.camelcase(name)
        osn: str = letters.uppercase(name)
        query = """
            INSERT INTO author(author_name, osn)
            VALUES (%(name)s, %(osn)s)
        """
        values = {"name": name, "osn": osn}
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
        ons: str = f"%{letters.uppercase(search)}%"
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM author
            WHERE ons ILIKE %(ons)s
            ORDER BY author_name ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"ons": ons, "offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_author(id: str, name: str):
        ons: str = letters.uppercase(name)
        query = """
            UPDATE author SET
            author_name = %(name)s,
            ons = %(ons)s
            WHERE author_id = %(id)s
        """
        values = {
            "name": name,
            "ons": ons,
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