from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.schemas.skill import (
    SkillCreate,
    SkillUpdate,
)


def create_skill(
    db: Session,
    skill: SkillCreate,
) -> Skill:

    db_skill = Skill(**skill.model_dump())

    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)

    return db_skill


def get_skill_by_id(
    db: Session,
    skill_id: int,
) -> Skill | None:

    stmt = (
        select(Skill)
        .where(Skill.id == skill_id)
    )

    return db.scalar(stmt)

def get_all_skill_by_name(db: Session, name: str):
    stmt = (
        select(Skill).where(Skill.name == name)
    )

    return list(db.scalars(stmt).all())


def get_all_skills(
    db: Session,
) -> list[Skill]:

    stmt = select(Skill)

    return list(db.scalars(stmt).all())


def update_skill(
    db: Session,
    skill_id: int,
    skill_update: SkillUpdate,
) -> Skill | None:

    db_skill = get_skill_by_id(
        db,
        skill_id,
    )

    if db_skill is None:
        return None

    update_data = skill_update.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_skill, field, value)

    db.commit()
    db.refresh(db_skill)

    return db_skill



def delete_skill(
    db: Session,
    skill_id: int,
) -> bool:

    db_skill = get_skill_by_id(
        db,
        skill_id,
    )

    if db_skill is None:
        return False

    db.delete(db_skill)
    db.commit()

    return True