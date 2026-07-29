from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
# from app.crud import saved_job as saved_job_crud
from app.crud.saved_jobs import (
    save_job_for_user,
    get_saved_jobs_for_user,
    unsave_job_for_user,
)
from app.schemas.job import JobRead

router = APIRouter(prefix="/users/{user_id}/saved-jobs", tags=["saved-jobs"])


@router.post("/{job_id}", status_code=status.HTTP_201_CREATED)
def save_job(user_id: int, job_id: int, db: Session = Depends(get_db)):
    ok = save_job_for_user(db, user_id, job_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User or job not found")
    return {"message": "Job saved"}


@router.get("/", response_model=list[JobRead])
def get_saved_jobs(user_id: int, db: Session = Depends(get_db)):
    return get_saved_jobs_for_user(db, user_id)


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def unsave_job(user_id: int, job_id: int, db: Session = Depends(get_db)):
    ok = unsave_job_for_user(db, user_id, job_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Job unsaved"}