import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Course

course: Course
CourseRoute = APIRouter(prefix="/course", tags=["Course"])

class course_body(BaseModel):
    name: str = None
    details: str = None
    limit: int = None
    grade_availability: list = None

@CourseRoute.post("/")
async def create_course(data: course_body):
    try:
        response = await run_in_threadpool(course.create_course,
            data.name, data.details, data.limit, data.grade_availability
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.get("/")
async def read_course(page: int = None):
    try:
        response = await run_in_threadpool(course.read_course, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.get("/id")
async def read_course_by_id(id: int):
    try:
        response = await run_in_threadpool(course.read_course_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.get("/by")
async def read_course_by(search_by: str, str_search: str = None, num_search: int = None, page: int = None):
    try:
        response = await run_in_threadpool(course.read_course_by,
            search_by, str_search, num_search, page
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.put("/")
async def update_course(id: int, data: course_body):
    try:
        response = await run_in_threadpool(course.update_course,
            id, data.name, data.details, data.limit, data.grade_availability
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@CourseRoute.delete("/")
async def delete_course(id: int):
    try:
        response = await run_in_threadpool(course.update_course, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")