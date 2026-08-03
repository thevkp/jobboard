from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserCreate
from app.schemas.user import UserUpdate
from sqlalchemy import select


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return db_user

def get_user_by_id(db: Session, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    return db.scalar(stmt)

def get_user_by_email(db: Session, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    return db.scalar(stmt)

def get_all_users(db: Session) -> list[User]:
    stmt = select(User)
    return list(db.scalars(stmt).all())

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User | None:
    db_user = get_user_by_id(db, user_id)

    if db_user is None:
        return None

    update_data = user_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db: Session, user_id: int) -> bool:
    db_user = get_user_by_id(db, user_id)

    if db_user is None:
        return False

    db.delete(db_user)
    db.commit()

    return True