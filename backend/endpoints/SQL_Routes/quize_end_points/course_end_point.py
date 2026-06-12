import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Course

CourseRoute = APIRouter(prefix="/course", tags=["Course"])

class course_body(BaseModel):
    name: str = None
    details: str = None
    limit: int = None
    grade_availability: list = {
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

@CourseRoute.post("/")
async def create_course(data: course_body):
    try:
        response = await run_in_threadpool(Course.create_course,
            data.name, data.details, data.limit, data.grade_availability
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.get("/")
async def read_course(page: int = None):
    try:
        response = await run_in_threadpool(Course.read_course, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.get("/id")
async def read_course_by_id(id: int):
    try:
        response = await run_in_threadpool(Course.read_course_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.get("/by")
async def read_course_by(search_by: str, str_search: str = None, num_search: int = None, page: int = None):
    try:
        response = await run_in_threadpool(Course.read_course_by,
            search_by, str_search, num_search, page
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.put("/")
async def update_course(id: int, data: course_body):
    try:
        response = await run_in_threadpool(Course.update_course,
            id, data.name, data.details, data.limit, data.grade_availability
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.delete("/")
async def delete_course(id: int):
    try:
        response = await run_in_threadpool(Course.update_course, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")