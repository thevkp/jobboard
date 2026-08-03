from fastapi import FastAPI

from app.api.routers import (
    user,
    companies,
    jobs,
    applications,
    skills,
    saved_jobs,
    root,
    auth
)


app = FastAPI()

app.include_router(root.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(companies.router)
app.include_router(jobs.router)
app.include_router(skills.router)
app.include_router(applications.router)
app.include_router(saved_jobs.router)