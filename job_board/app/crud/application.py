from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.application import Application
from app.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
)


def create_application(db: Session, application: ApplicationCreate) -> Application:
    db_application = Application(**application.model_dump())


    try:
        db.add(db_application)
        db.commit()
        db.refresh(db_application)
    except:
        db.rollback()
        raise

    return db_application

def get_application_by_id(db: Session, application_id: int) -> Application | None:
    stmt = select(Application).where(Application.id == application_id)

    return db.scalars(stmt).first()

def get_applicatons_for_user(db: Session, user_id: int) -> list[Application]:
    stmt = (
        select(Application)
        .where(Application.user_id == user_id)
        .options(joinedload(Application.job), joinedload(Application.user))
    )

    return list(db.scalars(stmt).all())


def get_job_applications(db: Session, job_id: int) -> list[Application]:
    stmt = select(Application).where(Application.job_id == job_id)

    return list(db.scalars(stmt).all())


def update_application(db: Session, application_id: int, application_update: ApplicationUpdate) -> Application | None:
    db_application = get_application_by_id(db, application_id)

    if db_application is None: 
        return None

    update_data = application_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_application, field, value)

    db.commit()
    db.refresh(db_application)

    return db_application

def delete_application(db: Session, application_id: int) -> bool:
    db_application = get_application_by_id(
        db,
        application_id,
    )

    if db_application is None:
        return False

    db.delete(db_application)
    db.commit()

    return True