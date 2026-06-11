import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from . import Quiz

quiz: Quiz
QuizRoute = APIRouter(prefix="/quiz", tags=["Quiz"])

class quiz_body(BaseModel):
    question: str
    q_type: str = None
    answer: str
    reason: str
    course: int = None

@QuizRoute.post("/")
async def create_quiz(data: quiz_body):
    try:
        response = await run_in_threadpool(quiz.create_quiz,
            data.question, data.q_type, data.answer, data.course, data.reason
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizRoute.get("/")
async def read_quiz(course_id: int, page: int = None):
    try:
        response = await run_in_threadpool(quiz.read_quiz,
            course_id, page
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")

@QuizRoute.get("/id")
async def read_quiz_by_id(id: int):
    try:
        response = await run_in_threadpool(quiz.read_quiz_by_id, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizRoute.get("/by")
async def read_quiz_by_type(search: str, page: int = None):
    try:
        response = await run_in_threadpool(quiz.read_quiz,
            search, page
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")

@QuizRoute.put("/")
async def update_quiz(id: int, data: quiz_body):
    try:
        response = await run_in_threadpool(quiz.update_quiz,
            id, data.question, data.answer, data.reason
        )
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")
    
@QuizRoute.delete("/")
async def delete_quiz(id: int):
    try:
        response = await run_in_threadpool(quiz.delete_quiz, id)
        return response
    except Exception as e:
        raise HTTPException(500, "Bad Request!")