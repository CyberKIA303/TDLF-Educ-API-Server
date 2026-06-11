import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection, letters)
import datetime

class Book:
    data = [
        {"element_name": "book_id",      "element_row": 0},
        {"element_name": "book_name",    "element_row": 1},
        {"element_name": "link",         "element_row": 2},
        {"element_name": "book_picture", "element_row": 3}
    ]
    
    def create_book(book_name: str, link: str, pic_link: str):
        uppercase: str = letters.uppercase(book_name)
        query = """
            INSERT INTO book(book_name, link, book_picture, osn)
            VALUES (%(book_name)s, %(link)s, %(pic_link)s, %(uppercase)s)
        """
        values = {
            "book_name": book_name,
            "link": link,
            "pic_link": pic_link,
            "uppercase": uppercase
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_book(page: int = None):
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM book
            ORDER BY book_name ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_book_by_id(id: str):
        query = """
            SELECT * FROM book
            WHERE book_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_book_by(search_name: str, page: int = None):
        osn: str = f"%{letters.uppercase(search_name)}%"
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM book
            WHERE osn ILIKE %(osn)s
            ORDER BY book_name ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"osn": osn, "offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_book(id: str, book_name: str, link: str, pic_link: str):
        osn: str = letters.uppercase(book_name)
        query = """
            UPDATE book SET
            book_name = %(book_name)s,
            link = %(link)s,
            book_picture = %(pic_link)s,
            osn = %(osn)s
            WHERE book_id = %(id)s
        """
        values = {
            "book_name": book_name,
            "link": link,
            "book_picture": book_picture,
            "osn": osn,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_book(id: str):
        query = """
            DELETE FROM book
            WHERE book_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response