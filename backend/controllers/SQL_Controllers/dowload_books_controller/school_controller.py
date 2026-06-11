import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection)

class School:
    data = [
        {"element_name": "school_id",      "element_row": 0},
        {"element_name": "school_name",    "element_row": 1},
        {"element_name": "school_address", "element_row": 2},
        {"element_name": "school_level",   "element_row": 3},
        {"element_name": "school_picture", "element_row": 4}
    ]
    
    def create_school(school_name: str, address: str, level: str, pic: str):
        query = """
            INSERT INTO school(school_name, school_address, school_level, school_picture)
            VALUES (%(school_name)s, %(address)s, %(level)s, %(pic)s)
        """
        values = {
            "school_name": school_name,
            "address": address,
            "level": level,
            "pic": pic
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_school():
        query = """
            SELECT * FROM school
            ORDER BY school_name ASC
        """
        response = execute_query_on_connection(nodes=nodes, query=query, value_return=True, returned_element=data)
        return response
    
    def read_school_by_id(id: str):
        query = """
            SELECT * FROM school
            WHERE school_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_school_by(search_by: str, search: str):
        ok: bool = True
        query: str
        if search_by == "school_name":
            query = """
                SELECT * FROM school
                WHERE school_name = %(search)s
                ORDER BY school_name ASC
            """
        elif search_by == "school_address":
            query = """
                SELECT * FROM school
                WHERE school_address = %(search)s
                ORDER BY school_name ASC
            """
        elif search_by == "school_level":
            query = """
                SELECT * FROM school
                WHERE school_level = %(search)s
                ORDER BY school_name ASC
            """
        else:
            ok = False
        if ok:
            values = {"search": search}
            response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
            return response
        else:
            return "INVALID SEARCH QUERY!"
        
    def update_school(id: str, school_name: str, address: str, level: str, pic: str):
        query = """
            UPDATE school SET
            school_name = %(school_name)s,
            school_address = %(address)s,
            school_level = %(level)s,
            school_picture = %(pic)s
            WHERE school_id = %(id)s
        """
        values = {
            "school_name": school_name,
            "address": address,
            "level": level,
            "pic": pic,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
        
    def delete_school(id: str):
        query = """
            DELETE FROM school
            WHERE school_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response