from fastapi import FastAPI

from .routes import auth, company, inscription, job, student

app = FastAPI()


app.include_router(auth.router, prefix='/api')
app.include_router(company.router, prefix='/api')
app.include_router(job.router, prefix='/api')
app.include_router(student.router, prefix='/api')
app.include_router(inscription.router, prefix='/api')
