import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Book

BookRoute = APIRouter(prefix="/book", tags=["Book"])

class book_body(BaseModel):
    book_name: str
    link: str
    pic_link: str

@BookRoute.post("/")
async def create_book(data: book_body):
    try:
        response = await run_in_threadpool(Book.create_book,
            data.book_name, data.link, data.pic_link
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookRoute.get("/")
async def read_book(page: int = None):
    try:
        response = await run_in_threadpool(Book.read_book, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookRoute.get("/id")
async def read_book_by_id(id: str):
    try:
        response = await run_in_threadpool(Book.read_book_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookRoute.get("/by")
async def read_book_by(search_name: str, page: int = None):
    try:
        response = await run_in_threadpool(Book.read_book_by, search_name, page)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookRoute.put("/")
async def update_book(id: str, data: book_body):
    try:
        response = await run_in_threadpool(Book.update_book,
            id, data.book_name, data.link, data.pic_link
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookRoute.delete("/")
async def delete_book(id: str):
    try:
        response = await run_in_threadpool(Book.delete_book, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")