from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from backend.controllers.auth_controller.auth import Auth
from backend.security.auth_dependency import get_current_user

AuthRoute=APIRouter(prefix="/auth", tags=["Authentication"])

class RegisterBody(BaseModel):
    username:str
    email:str
    password:str

class LoginBody(BaseModel):
    email:str
    password:str

@AuthRoute.post("/register")
def register(data:RegisterBody):
    return Auth.register(data.username,data.email,data.password)

@AuthRoute.post("/login")
def login(data:LoginBody):
    result=Auth.login(data.email,data.password)
    if not result:
        raise HTTPException(401,"Invalid credentials")
    return result

@AuthRoute.get("/me")
def me(user=Depends(get_current_user)):
    return user

@AuthRoute.post("/logout")
def logout():
    return {"message":"logged out"}
