from fastapi import APIRouter
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(username: str):
    # Demo-only, no password verification
    access_token = create_access_token(subject=username)
    return {"access_token": access_token, "token_type": "bearer"}