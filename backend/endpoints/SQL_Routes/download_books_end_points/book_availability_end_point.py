import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Book_Availability

book_availability: Book_Availability
BookAvailabilityRoute = APIRouter(prefix="/book_availability", tags=["Book Availability"])

class book_availability_body(BaseModel):
    school_id: int
    book_id: int

@BookAvailabilityRoute.post("/")
async def create_book_availability(data: book_availability_body):
    try:
        response = await run_in_threadpool(book_availability.create_book_availability,
            data.school_id, data.book_id
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAvailabilityRoute.get("/")
async def read_book_availability():
    try:
        response = await run_in_threadpool(book_availability.read_book_availability)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAvailabilityRoute.get("/id")
async def read_book_availability_by_id(id: str):
    try:
        response = await run_in_threadpool(book_availability.read_book_availability_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAvailabilityRoute.get("/by")
async def read_book_availability_by(search_by: str, search: str):
    try:
        response = await run_in_threadpool(book_availability.read_book_availability_by,
            search_by, search
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAvailabilityRoute.put("/")
async def update_book_availability(id: str, data: book_availability_body):
    try:
        response = await run_in_threadpool(book_availability.update_book_availability,
            id, data.school_id, data.book_id
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@BookAvailabilityRoute.delete("/")
async def delete_book_availability(id: str):
    try:
        response = await run_in_threadpool(book_availability.delete_book_availability, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")