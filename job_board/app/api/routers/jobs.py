from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobRead
from app.api.deps import get_db
from app.crud import job as job_crud


router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", response_model=JobRead)
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    return job_crud.create_job(db, payload)


@router.get("/{job_id}}", response_model=JobRead)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = job_crud.get_job_by_id(db, job_id)

    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return db_job

@router.get("/", response_model=list[JobRead])
def read_all_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return job_crud.get_all_jobs(db, skip=skip, limit=limit)

