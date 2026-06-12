import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import My_Course

MyCourseRoute = APIRouter(prefix="/my_course", tags=["My Course"])

class my_course_body(BaseModel):
    user: str
    course: str
    
@MyCourseRoute.post("/")
async def create_my_course(data: my_course_body):
    try:
        response = await run_in_threadpool(My_Course.create_my_course,
            data.user, data.course
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@MyCourseRoute.get("/")
async def read_my_course(user: str, page: int = None):
    try:
        response = await run_in_threadpool(My_Course.read_my_course,
            user, page
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")

@MyCourseRoute.get("/id")
async def read_my_course_by_id(id: str):
    try:
        response = await run_in_threadpool(My_Course.read_my_course_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")

@MyCourseRoute.delete("/")
async def delete_my_course(id: str):
    try:
        response = await run_in_threadpool(My_Course.delete_my_course, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")