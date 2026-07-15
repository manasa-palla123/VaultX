from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to VaultX"}


@router.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {
        "message": "Welcome!",
        "email": current_user
    }