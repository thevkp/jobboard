from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.api.deps import get_db
from app.crud import application as application_crud
from app.schemas.application import ApplicationCreate, ApplicationRead, ApplicationUpdate



router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=ApplicationRead)
def create_application(payload: ApplicationCreate, db: Session = Depends(get_db)):
    return application_crud.create_application(db, payload)

@router.get("/applications/job", response_model=list[ApplicationRead])
def get_all_applications(job_id: int, db: Session = Depends(get_db)):
    return application_crud.get_job_applications(db, job_id)



@router.get("/user/{user_id}", response_model=list[ApplicationRead])
def read_applications_for_user(user_id: int, db: Session = Depends(get_db)):
    return application_crud.get_applicatons_for_user(db, user_id)

@router.patch("/{application_id}/status", response_model=ApplicationRead)
def update_status(application_id: int, application_update: ApplicationUpdate, db: Session = Depends(get_db)):
    db_app = application_crud.update_application(db, application_id, application_update)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return db_app