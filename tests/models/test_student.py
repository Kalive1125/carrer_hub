from sqlalchemy.orm import Session

from src.models.account import Account
from src.models.student import Student


class TestStudent:
    def test_student_deve_criar_account(self, session: Session, acc_alice):
        Student.create_student(acc_alice, session)

        getAccount = (
            session.query(Account).filter_by(email=acc_alice['email']).first()
        )

        assert getAccount

        getStudent = session.query(Student).filter_by(id=getAccount.id).first()

        assert getStudent

        assert getAccount.id == getStudent.id

    def test_deletear_student_deve_deletar_account(
        self, session: Session, acc_alice
    ):
        Student.create_student(acc_alice, session)

        getAccount = (
            session.query(Account).filter_by(email=acc_alice['email']).first()
        )

        Student.delete_student(getAccount.id)
        ...
