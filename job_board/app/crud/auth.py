from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserCreate
from app.auth.security import hash_password

def register_user(db: Session, user: UserCreate) -> User:
    hashed = hash_password(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user