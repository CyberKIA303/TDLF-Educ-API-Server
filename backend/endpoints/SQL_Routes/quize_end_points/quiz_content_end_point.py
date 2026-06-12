import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Quiz_Content

QuizContentRoute = APIRouter(prefix="/quiz_content", tags=["Quiz Content"])

class quiz_content_body(BaseModel):
    initial: str
    content: str
    quiz_id: int = None
    
@QuizContentRoute.post("/")
async def create_quiz_content(data: quiz_content_body):
    try:
        response = await run_in_threadpool(Quiz_Content.create_quiz_content,
            data.initial, data.content, data.quiz_id
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizContentRoute.get("/")
async def read_quiz_content(quiz_id: int):
    try:
        response = await run_in_threadpool(Quiz_Content.read_quiz_content, quiz_id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizContentRoute.get("/id")
async def read_quiz_content_by_id(id: int):
    try:
        response = await run_in_threadpool(Quiz_Content.read_quiz_content_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizContentRoute.put("/")
async def update_quiz_content(id: int, data: quiz_content_body):
    try:
        response = await run_in_threadpool(Quiz_Content.update_quiz_content,
            id, data.initial, data.content
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizContentRoute.delete("/")
async def delete_quiz_content(id: int):
    try:
        response = await run_in_threadpool(Quiz_Content.delete_quiz_content, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")