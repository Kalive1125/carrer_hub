from sqlalchemy.orm import Session

from .settings import engine


def getSession():
    with Session(engine) as session:
        yield session
