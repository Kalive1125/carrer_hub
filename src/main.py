from fastapi import FastAPI

from .routes import auth, company, inscription, job, student

app = FastAPI()


app.include_router(auth.router)
app.include_router(company.router)
app.include_router(job.router)
app.include_router(student.router)
app.include_router(inscription.router)
