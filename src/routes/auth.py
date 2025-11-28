from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database.session import getSession
from ..models.account import Account
from ..security.encryption import passwd_hash
from ..utils.tokenization import create_token

router = APIRouter(prefix='/api/auth/v1', tags=['auth'])


@router.post('/sign-in', status_code=status.HTTP_201_CREATED)
def signInAccount(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(getSession)],
):
    getAccount = Account.getAccountByEmail(form_data.username, session)

    if passwd_hash.verify(form_data.password, getAccount.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais incorretas!',
        )

    payload = {
        'sub': getAccount.id,
        'role': getAccount.role,
        'token_type': 'Bearer',
    }

    token = create_token(payload)

    return token
