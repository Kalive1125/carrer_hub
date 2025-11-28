import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models.base import Base


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')

    Base.metadata.create_all(engine)

    with Session(engine) as s:
        yield s

    Base.metadata.drop_all(engine)


@pytest.fixture
def acc_alice():
    return {
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'alice_secret',
    }
