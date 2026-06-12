import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import User_Info

UserInfoRoute = APIRouter(prefix="/user_info", tags=["User Info"])

class user_info_body(BaseModel):
    name: str
    email: str
    password: str
    status: str = None
    
@UserInfoRoute.post("/")
async def create_user_info(data: user_info_body):
    try:
        response = await run_in_threadpool(User_Info.create_user_info,
            data.name, data.email, data.password, data.status
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@UserInfoRoute.get("/")
async def read_user_info(page: int = None):
    try:
        response = await run_in_threadpool(User_Info.read_user_info, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@UserInfoRoute.get("/id")
async def read_user_info_by_id(id: str):
    try:
        response = await run_in_threadpool(User_Info.read_user_info_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@UserInfoRoute.get("/by")
async def read_user_info_by(search_by: str, search: str, page: int = None):
    try:
        response = await run_in_threadpool(User_Info.read_user_info_by,
            search_by, search, page
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@UserInfoRoute.put("/")
async def update_user_info(id: str, data: user_info_body):
    try:
        response = await run_in_threadpool(User_Info.update_user_info,
            data.name, data.email, data.password
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@UserInfoRoute.delete("/")
async def delete_user_info(id: str):
    try:
        response = await run_in_threadpool(User_Info.delete_user_info, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")