from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import skill as skill_crud
from app.schemas.skill import SkillRead, SkillCreate
from app.api.deps import get_db

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("/", response_model=SkillRead)
def create_skill(payload: SkillCreate, db: Session = Depends(get_db)):
    existing = skill_crud.get_all_skill_by_name(db, payload.name)
    print("ka ho")

    if existing:
        raise HTTPException(status_code=400, detail="Skill already exists")
    return skill_crud.create_skill(db, payload)
    


@router.get("/{skill_id}", response_model=SkillRead)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = skill_crud.get_skill_by_id(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill

@router.get("/", response_model=list[SkillRead])
def read_all_skills(db: Session = Depends(get_db)):
    return skill_crud.get_all_skills(db)