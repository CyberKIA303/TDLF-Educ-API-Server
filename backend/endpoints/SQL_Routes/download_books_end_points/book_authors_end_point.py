import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Book_Authors

BookAuthorsRoute = APIRouter(prefix="/book_authors", tags=["Book Authors"])

class book_authors_body(BaseModel):
    book_id: str
    author_id: str

@BookAuthorsRoute.post("/")
async def create_book_authors(data: book_authors_body):
    try:
        response = await run_in_threadpool(Book_Authors.create_book_authors,
            data.book_id, data.author_id
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAuthorsRoute.get("/")
async def read_book_authors():
    try:
        response = await run_in_threadpool(Book_Authors.read_book_authors)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAuthorsRoute.get("/id")
async def read_book_authors_by_id(id: str):
    try:
        response = await run_in_threadpool(Book_Authors.read_book_authors_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAuthorsRoute.get("/by")
async def read_book_authors_by(search_by: str, search: str):
    try:
        response = await run_in_threadpool(Book_Authors.read_book_authors_by,
            search_by, search
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAuthorsRoute.put("/")
async def update_book_authors(id: str, data: book_authors_body):
    try:
        response = await run_in_threadpool(Book_Authors.update_book_authors,
            id, data.book_id, data.author_id
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAuthorsRoute.delete("/")
async def read_book_authors_by_id(id: str):
    try:
        response = await run_in_threadpool(Book_Authors.delete_book_authors, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")