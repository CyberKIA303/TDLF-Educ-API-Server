import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection)
import uuid

data = [
    {"element_name": "book_authors_id", "element_row": 0},
    {"element_name": "book_id",         "element_row": 1},
    {"element_name": "author_id",       "element_row": 2}
]
    
class Book_Authors:
    def create_book_authors(book_id: str, author_id: str):
        u_id = str(uuid.uuid4())
        query = """
            INSERT INTO book_authors(book_authors_id, book_id, author_id)
            VALUES (%(u_id)s, %(book_id)s, %(author_id)s)
        """
        values = {
            "u_id": u_id,
            "book_id": book_id,
            "author_id": author_id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_book_authors():
        query = """
            SELECT * FROM book_authors
            ORDER BY book_id ASC
        """
        response = execute_query_on_connection(nodes=nodes, query=query, value_return=True, returned_element=data)
        return response
    
    def read_book_authors_by_id(id: str):
        query = """
            SELECT * FROM book_authors
            WHERE book_authors_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_book_authors_by(search_by: str, search: str = None):
        ok: bool = True
        query: str
        if search_by == "book_id":
            query = """
                SELECT * FROM book_authors
                WHERE book_id = %(search)s
                ORDER BY book_id ASC
            """
        elif search_by == "author_id":
            query = """
                SELECT * FROM book_authors
                WHERE author_id = %(search)s
                ORDER BY author_id ASC
            """
        else:
            ok = False
        if ok:
            values = {"search": search}
            response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
            return response
        else:
            return "INVALID SEARCH QUERY!"
    
    def update_book_authors(id: str, book_id: str, author_id: str):
        query = """
            UPDATE book_authors SET
            book_id = %(book_id)s,
            author_id = %(author_id)s,
            WHERE book_authors_id = %(id)s
        """
        values = {
            "book_id": book_id,
            "author_id": author_id,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_book_authors(id: str):
        query = """
            DELETE FROM book_authors
            WHERE book_authors_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response