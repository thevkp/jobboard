from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.job import Job
# from app.models.user import User
from app.models.association import saved_jobs



def save_job_for_user(db: Session, user_id: int, job_id: int) -> bool:
    stmt = select(saved_jobs).where(
        saved_jobs.c.user_id == user_id
    ).where(
        saved_jobs.c.job_id == job_id
    )
    if db.execute(stmt).first() is not None:
        return False
    
    stmt = saved_jobs.insert().values(user_id=user_id, job_id=job_id)
    db.execute(stmt)
    db.commit()
    return True

def get_saved_jobs_for_user(db: Session, user_id: int) -> list[Job]:
    stmt = (
        select(Job)
        .select_from(saved_jobs.join(Job, saved_jobs.c.job_id == Job.id))
        .where(saved_jobs.c.user_id == user_id)
    )
    result = db.execute(stmt).scalars().all()
    return list(result)

def unsave_job_for_user(db: Session, user_id: int, job_id: int) -> bool:
    stmt = (
        saved_jobs.delete()
        .where(saved_jobs.c.user_id == user_id)
        .where(saved_jobs.c.job_id == job_id)
    )
    db.execute(stmt)
    db.commit()
    return True