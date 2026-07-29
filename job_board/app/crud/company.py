from sqlalchemy import select
from sqlalchemy.orm import Session


from app.models.company import Company
from app.models.job import Job
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, company: CompanyCreate) -> Company:
    db_company = Company(**company.model_dump())

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company

def get_company_by_id(db: Session, company_id: int) -> Company | None:
    stmt = select(Company).where(
        Company.id == company_id
    )

    return db.scalars(stmt).first() 

def get_company_by_name(db: Session, name: str) -> Company | None:
    stmt = select(Company).where(
        Company.title == name
    )

    return db.scalar(stmt)


def get_all_companies(db: Session) -> list[Company]:
    stmt = select(Company)

    return list(db.scalars(stmt).all())

def update_company(db: Session, company_id: int, company_update: CompanyUpdate) -> Company | None:
    db_company = get_company_by_id(db, company_id)
    if db_company is None:
        return None

    update_data = company_update.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_company, field, value)


    db.commit()
    db.refresh(db_company)

    return db_company


def delete_company(db: Session, company_id: int) -> bool:
    db_company = get_company_by_id(db, company_id)

    if db_company is None:
        return False

    db.delete(db_company)
    db.commit()


    return True

def get_company_jobs(db: Session, company_id: int) -> list[Job]:
    company = get_company_by_id(db, company_id)
    if company is None:
        return []

    return company.jobs