from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobRead
from app.api.deps import get_db
from app.crud import job as job_crud
from app.models.job import Job
from app.auth.dependencies import get_current_user

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User


router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", response_model=JobRead)
def create_job(payload: JobCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> Job:
    if current_user.company_id is None:
        raise HTTPException(status_code=400, detail="Only users associated with a company can post jobs")
    return job_crud.create_job(db, payload, company_id=current_user.company_id)


@router.get("/{job_id}}", response_model=JobRead)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = job_crud.get_job_by_id(db, job_id)

    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return db_job

# @router.get("/", response_model=list[JobRead])
# def read_all_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return job_crud.get_all_jobs(db, skip=skip, limit=limit)

@router.get("/", response_model=list[JobRead])
def get_all_jobs(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    location: str | None = None,
    min_salary: int | None = None,
    skill: str | None = None
) -> list[Job]:
    return job_crud.get_all_jobs(
        db, skip=skip, limit=limit, 
        location=location, 
        min_salary=min_salary,
        skill=skill
        )