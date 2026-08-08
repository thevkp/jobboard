from fastapi import APIRouter, status, HTTPException, Depends
from typing import Any
from sqlalchemy.orm import Session
from app.schemas.user import UserRead
from app.crud import user as crud_user
from app.crud.auth import register_user
from app.schemas.auth import UserCreate, UserLogin, Token
from app.auth.security import verify_password
from app.auth.jwt import create_access_token
from app.core.database import get_db
from job_board.app.auth.dependencies import get_current_user
from app.models.user import User


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)) -> dict[str, Any]:
    return {"id": current_user.id, "email": current_user.email}

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = crud_user.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return register_user(db, user)

@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, credentials.email)

    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    token = create_access_token({"sub": user.email})
    return Token(access_token=token, token_type="bearer")
    