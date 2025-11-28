import pytest
from sqlalchemy.exc import IntegrityError

from src.models.account import Account


class TestAccount:
    def test_nao_permitir_duas_contas_com_mesmo_email(
        self, session, acc_alice: dict
    ):
        acc_another_alice = acc_alice.copy()

        acc_another_alice['username'] = 'another_alice'

        Account._create_account(acc_alice, session)

        with pytest.raises(IntegrityError):
            Account._create_account(acc_another_alice, session)

    def test_nao_permirit_duas_contas_com_mesmo_username(
        self, session, acc_alice: dict
    ):
        acc_another_alice = acc_alice.copy()

        acc_another_alice['email'] = 'another_alice@example.com'

        Account._create_account(acc_alice, session)

        with pytest.raises(IntegrityError):
            Account._create_account(acc_another_alice, session)
