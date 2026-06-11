import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import School

school: School
SchoolRoute = APIRouter(prefix="/school", tags=["School"])

class school_body(BaseModel):
    school_name: str
    address: str
    level: str
    pic: str
    
@SchoolRoute.post("/")
async def create_school(data: school_body):
    try:
        response = await run_in_threadpool(school.create_school,
            data.school_name, data.address, data.level, data.pic
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@SchoolRoute.get("/")
async def read_school():
    try:
        response = await run_in_threadpool(school.read_school)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")

@SchoolRoute.get("/id")
async def read_school_by_id(id: str):
    try:
        response = await run_in_threadpool(school.read_school_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@SchoolRoute.get("/by")
async def read_school_by(search_by: str, search: str):
    try:
        response = await run_in_threadpool(school.read_school_by,
            search_by, search
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@SchoolRoute.put("/")
async def update_school(id: str, data: school_body):
    try:
        response = await run_in_threadpool(school.update_school,
            id, data.school_name, data.address, data.level, data.pic
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@SchoolRoute.delete("/")
async def delete_school(id: str):
    try:
        response = await run_in_threadpool(school.delete_school, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")