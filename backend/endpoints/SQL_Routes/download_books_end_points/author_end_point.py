import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Author

AuthorRoute = APIRouter(prefix="/author", tags=["Author"])

class author_body(BaseModel):
    name: str
    
@AuthorRoute.post("/")
async def create_author(data: author_body):
    try:
        response = await run_in_threadpool(Author.create_author, data.name)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@AuthorRoute.get("/")
async def read_author(page: int = None):
    try:
        response = await run_in_threadpool(Author.read_author, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@AuthorRoute.get("/id")
async def read_author_by_id(id: str):
    try:
        response = await run_in_threadpool(Author.read_author_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@AuthorRoute.get("/by")
async def read_author_by(search: str, page: int = None):
    try:
        response = await run_in_threadpool(Author.read_author_by, search, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@AuthorRoute.put("/")
async def update_author(id: str, data: author_body):
    try:
        response = await run_in_threadpool(Author.update_author, id, data.name)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@AuthorRoute.delete("/")
async def delete_author(id: str):
    try:
        response = await run_in_threadpool(Author.delete_author, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")