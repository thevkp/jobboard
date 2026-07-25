from sqlalchemy import (
    create_engine
)
from app.core.config import settings

from sqlalchemy.orm import (
    DeclarativeBase, sessionmaker
)


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass



def get_db():
    db = SessionLocal()  # 1. create the session

    try:
        yield db # 2. hand it out, PAUSE here
    finally:
        db.close() # 3. resume here later, and clean up