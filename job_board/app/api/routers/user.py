from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import user as crud_user
from app.schemas.user import(
    # UserCreate, 
    UserRead, UserUpdate
)


router = APIRouter(prefix="/users", tags=["Users"])

# @router.post("/", response_model=UserRead)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     return crud_user.create_user(db, user)


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = crud_user.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user


@router.get("/", response_model=list[UserRead])
def get_users(
    db: Session = Depends(get_db),
):
    return crud_user.get_all_users(db)


@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    updated = crud_user.update_user(
        db,
        user_id,
        user,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return updated


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    success = crud_user.delete_user(db, user_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "message": "User deleted successfully"
    }