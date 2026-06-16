from fastapi import APIRouter
from pydantic import BaseModel
from database import supabase

router = APIRouter(prefix="/auth", tags=["Authentication"])

class UserCredentials(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user_data: UserCredentials):
    return supabase.auth.sign_up({'email': user_data.email, 'password': user_data.password})

@router.post("/login")
def login(user_data: UserCredentials):
    return supabase.auth.sign_in_with_password({'email': user_data.email, 'password': user_data.password})