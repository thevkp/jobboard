from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
# from app.core.database import get_db
from app.crud import company as crud_company
from app.schemas.company import (
    CompanyCreate,
    CompanyRead,
    CompanyUpdate,
)

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


@router.post(
    "/",
    response_model=CompanyRead,
    status_code=status.HTTP_201_CREATED,
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    return crud_company.create_company(db, company)


@router.get(
    "/{company_id}",
    response_model=CompanyRead,
)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
):
    company = crud_company.get_company_by_id(db, company_id)

    if company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return company


@router.get(
    "/",
    response_model=list[CompanyRead],
)
def get_all_companies(
    db: Session = Depends(get_db),
):
    return crud_company.get_all_companies(db)


@router.patch(
    "/{company_id}",
    response_model=CompanyRead,
)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db),
):
    updated_company = crud_company.update_company(
        db,
        company_id,
        company,
    )

    if updated_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return updated_company


@router.delete(
    "/{company_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
):
    success = crud_company.delete_company(
        db,
        company_id,
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )


from app.schemas.job import JobRead


@router.get(
    "/{company_id}/jobs",
    response_model=list[JobRead],
)
def get_company_jobs(
    company_id: int,
    db: Session = Depends(get_db),
):
    company = crud_company.get_company_by_id(db, company_id)

    if company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return crud_company.get_company_jobs(
        db,
        company_id,
    )