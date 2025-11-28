from datetime import UTC, datetime, timedelta

from jwt import encode

from ..security.enviroment import env_settings


def create_token(payload: dict):
    delta = timedelta(minutes=env_settings['ACCESS_TOKEN_EXPIRE_MINUTES'])
    expire = datetime.now(UTC) + delta

    payload['exp'] = expire

    token = encode(
        payload=payload,
        algorithm=env_settings['ALGORITHM'],
        key=env_settings['JWT_SECRET_KEY'],
    )

    return token
