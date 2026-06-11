import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection)

class Book_Availability:
    data = [
        {"element_name": "book_availability_id", "element_row": 0},
        {"element_name": "school_id",            "element_row": 1},
        {"element_name": "book_id",              "element_row": 2}
    ]
    
    def create_book_availability(school_id: str, book_id: str):
        query = """
            INSERT INTO book_availability(school_id, book_id)
            VALUES (%(school_id)s, %(book_id)s)
        """
        values = {"school_id": school_id, "book_id": book_id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_book_availability():
        query = """
            SELECT * FROM book_availability
            ORDER BY book_id ASC
        """
        response = execute_query_on_connection(nodes=nodes, query=query, value_return=True, returned_element=data)
        return response
    
    def read_book_availability_by_id(id: str):
        query = """
            SELECT * FROM book_availability
            WHERE book_availability_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_book_availability_by(search_by: str, search: str):
        ok: bool = True
        query: str
        if search_by == "school_id":
            query = """
                SELECT * FROM book_availability
                WHERE school_id = %(search)s
                ORDER BY book_id ASC
            """
        elif search_by == "book_id":
            query = """
                SELECT * FROM book_availability
                WHERE book_id = %(search)s
                ORDER BY book_id ASC
            """
        else:
            ok = False
        if ok:
            values = {"search": search}
            response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
            return response
        else:
            return "INVALID SEARCH QUERY!"
        
    def update_book_availability(id: str, school_id: str, book_id: str):
        query = """
            UPDATE book_availability SET
            school_id = %(school_id)s,
            book_id = %(book_id)s
            WHERE book_availability_id = %(id)s
        """
        values = {
            "school_id": school_id,
            "book_id": book_id,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_book_availability(id: str):
        query = """
            DELETE FROM book_availability
            WHERE book_availability_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response