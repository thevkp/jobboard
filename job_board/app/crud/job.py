from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload


from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate


def create_job(db: Session, job: JobCreate) -> Job:
    db_job = Job(**job.model_dump())

    db.add(db_job)
    db.commit()
    db.refresh(db_job)


    return db_job


def get_job_by_id(db: Session, job_id: int) -> Job | None:
    stmt = (
        select(Job)
        .where(Job.id == job_id)
        .options(joinedload(Job.company), selectinload(Job.skills))
    )

    return db.scalars(stmt).first()

def get_all_jobs(db: Session, skip: int = 0, limit: int = 10) -> list[Job]:
    stmt = (
        select(Job)
        .options(joinedload(Job.company), selectinload(Job.skills))
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(stmt).all())

def update_job(db: Session, job_id: int, job_update: JobUpdate) -> Job | None:
    db_job = get_job_by_id(db, job_id)

    if db_job is None:
        return None

    update_data = job_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_job, field, value)

    db.commit()
    db.refresh(db_job)

    return db_job


def delete_job(db: Session, job_id: int) -> bool:
    db_job = get_job_by_id(db, job_id)

    if db_job is None:
        return False

    db.delete(db_job)
    db.commit()


    return True


def get_jobs_by_company(db: Session, company_id: int) -> list[Job]:
    stmt = select(Job).where(Job.company_id == company_id)

    return list(db.scalars(stmt).all())


def get_jobs_by_location(db: Session, location: str) -> list[Job]:

    stmt = (
        select(Job)
        .where(Job.location == location)
    )

    return list(db.scalars(stmt).all())

def search_jobs(db: Session, keyword: str) -> list[Job]:
    stmt = (
        select(Job)
        .where(Job.title.ilike(f"%{keyword}%"))
    )

    return list(db.scalars(stmt).all())


def add_skill_to_job(db: Session, job_id: int, skill_id: int) -> Job | None:
    from app.models.skill import Skill

    job = db.get(Job, job_id)
    skill = db.get(Skill, skill_id)
    if job is None or skill is None:
        return None

    job.skills.append(skill)
    db.commit()
    db.refresh(job)
    return job

