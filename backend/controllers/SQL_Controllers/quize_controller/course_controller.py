import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from . import (nodes, execute_query_on_connection, letters)
from fastapi import HTTPException

class Course:
    data = [
        {"element_name": "course_id",      "element_row": 0},
        {"element_name": "course_name",    "element_row": 1},
        {"element_name": "course_details", "element_row": 2},
        {"element_name": "passing_score",  "element_row": 3},
        {"element_name": "kinder",         "element_row": 4},
        {"element_name": "grade_1",        "element_row": 5},
        {"element_name": "grade_2",        "element_row": 6},
        {"element_name": "grade_3",        "element_row": 7},
        {"element_name": "grade_4",        "element_row": 8},
        {"element_name": "grade_5",        "element_row": 9},
        {"element_name": "grade_6",        "element_row":10},
        {"element_name": "grade_7",        "element_row":11},
        {"element_name": "grade_8",        "element_row":12},
        {"element_name": "grade_9",        "element_row":13},
        {"element_name": "grade_10",       "element_row":14},
        {"element_name": "grade_11",       "element_row":15},
        {"element_name": "grade_12",       "element_row":16},
        {"element_name": "college",        "element_row":17}
    ]
    
    def create_course(name: str = "New Course", details: str = "N/A", limit: int = 50, grade_availability: list = {"None"}):
        if "None" in grade_availability:
            grade_availability = {
                "kinder": False,
                "grade_1": False,
                "grade_2": False,
                "grade_3": False,
                "grade_4": False,
                "grade_5": False,
                "grade_6": False,
                "grade_7": False,
                "grade_8": False,
                "grade_9": False,
                "grade_10": False,
                "grade_11": False,
                "grade_12": False,
                "college": False
            }
        ga = grade_availability
        osn: str = letters.uppercase(name)
        query = """
            INSERT INTO course(
                course_name, course_details, passing_score, osn, kinder,
                grade_1, grade_2, grade_3, grade_4, grade_5, grade_6, grade_7,
                grade_8, grade_9, grade_10, grade_11, grade_12, college
            )
            VALUES (
                %(name)s, %(details)s, %(limit)s, %(osn)s, %(kd)s,
                %(g1)s, %(g2)s, %(g3)s, %(g4)s, %(g5)s, %(g6)s, %(g7)s,
                %(g8)s, %(g9)s, %(g10)s, %(g11)s, %(g12)s, %(clg)s
            )
        """
        values = {
            "name": name,
            "details": details,
            "limit": limit,
            "osn": osn,
            "kd": ga["kinder"],
            "g1": ga["grade_1"],
            "g2": ga["grade_2"],
            "g3": ga["grade_3"],
            "g4": ga["grade_4"],
            "g5": ga["grade_5"],
            "g6": ga["grade_6"],
            "g7": ga["grade_7"],
            "g8": ga["grade_8"],
            "g9": ga["grade_9"],
            "g10": ga["grade_10"],
            "g11": ga["grade_11"],
            "g12": ga["grade_12"],
            "clg": ga["college"]
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def read_course(page: int = None):
        offset: int = 0
        if page:
            offset = page * 10
        query = """
            SELECT * FROM course
            ORDER BY course_name ASC
            LIMIT 10 OFFSET %(offset)s
        """
        values = {"offset": offset}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_course_by_id(id: str):
        query = """
            SELECT * FROM course
            WHERE course_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def read_course_by(search_by: str, search: str = None, page: int = None):
        year_levels = {
            "kinder", "grade_1", "grade_2", "grade_3", "grade_4", "grade_5", "grade_6",
            "grade_7", "grade_8", "grade_9", "grade_10", "grade_11", "grade_12", "college"
        }
        osn: str = f"%{search}%"
        offset: int = 0
        if page:
            offset = page * 10
        query: str = None
        values: list = {}
        if search_by == "course_name" and str_search:
            query = """
                SELECT * FROM course
                WHERE osn ILIKE %(osn)s
                ORDER BY course_name ASC
                LIMIT 10 OFFSET %(offset)s
            """
            values = {"osn": osn, "offset": offset}
        elif search_by == "passing_score" and search:
            query = """
                SELECT * FROM course
                WHERE passing_score = %(search)s
                ORDER BY course_name ASC
                LIMIT 10 OFFSET %(offset)s
            """
            values = {"search": search, "offset": offset}
        elif search_by in year_levels:
            query = f"""
                SELECT * FROM course
                WHERE {search_by} = TRUE """ + """
                ORDER BY course_name ASC
                LIMIT 10 OFFSET %(offset)s
            """
            values = {"offset": offset}
        else:
            raise HTTPException(500, "Invalid Input!")
        response = execute_query_on_connection(nodes=nodes, query=query, values=values, value_return=True, returned_element=data)
        return response
    
    def update_course(id: str, name: str, details: str, limit: int, grade_availability: list):
        osn = letters.uppercase(name)
        query = """
            UPDATE course SET
            course_name = %(name)s,
            course_details = %(details)s,
            passing_score = %(limit)s,
            kinder = %(kd)s,
            grade_1 = %(g1)s,
            grade_2 = %(g2)s,
            grade_3 = %(g3)s,
            grade_4 = %(g4)s,
            grade_5 = %(g5)s,
            grade_6 = %(g6)s,
            grade_7 = %(g7)s,
            grade_8 = %(g8)s,
            grade_9 = %(g9)s,
            grade_10 = %(g10)s,
            grade_11 = %(g11)s,
            grade_12 = %(g12)s,
            college = %(clg)s,
            osn = %(osn)s
            WHERE course_id = %(id)s
        """
        values = {
            "name": name,
            "details": details,
            "limit": limit,
            "kd": grade_availability["kinder"],
            "g1": grade_availability["grade_1"],
            "g2": grade_availability["grade_2"],
            "g3": grade_availability["grade_3"],
            "g4": grade_availability["grade_4"],
            "g5": grade_availability["grade_5"],
            "g6": grade_availability["grade_6"],
            "g7": grade_availability["grade_7"],
            "g8": grade_availability["grade_8"],
            "g9": grade_availability["grade_9"],
            "g10": grade_availability["grade_10"],
            "g11": grade_availability["grade_11"],
            "g12": grade_availability["grade_12"],
            "clg": grade_availability["college"],
            "osn": osn,
            "id": id
        }
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response
    
    def delete_course(id: str):
        query = """
            DELETE FROM course
            WHERE course_id = %(id)s
        """
        values = {"id": id}
        response = execute_query_on_connection(nodes=nodes, query=query, values=values)
        return response