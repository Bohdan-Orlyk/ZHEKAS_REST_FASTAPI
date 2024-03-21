from typing import Annotated

from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.v1.library.models import User
from api.v1.library.services import crud_service


from database.db import get_session

security = HTTPBasic()


def get_auth_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)], session=Depends(get_session)):
    user: User = crud_service.get_auth_user(session=session, user_email=credentials.username)

    if not user or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    return user
