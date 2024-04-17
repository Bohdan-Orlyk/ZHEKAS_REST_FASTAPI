from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from database.db import get_session

from api.v1.library.schemas.schemas import CreateUser, ReadCreatedUser, ReadUserWithArticles
from api.v1.library.services import crud_service, auth_service

users = APIRouter(prefix="/users", tags=["Users"])


@users.get("/", response_model=List[ReadCreatedUser])  # TODO admin only
def get_all_users():
    return {"message": "OK!"}


@users.get("/user-articles", response_model=List[ReadUserWithArticles])
def get_user_with_articles(session=Depends(get_session)):
    user_with_articles = crud_service.get_user_with_articles(session=session)

    if not user_with_articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)
    return user_with_articles


@users.post("/register/", status_code=status.HTTP_201_CREATED, response_model=ReadCreatedUser)
def register(user: CreateUser, session=Depends(get_session)):
    new_user = crud_service.create_user(session=session, user_schema=user)

    if new_user:
        return new_user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")


@users.post("/login/")
def login(authed_user=Depends(auth_service.get_auth_user)):
    if authed_user:
        return {"code": status.HTTP_200_OK, "login": "OK"}


@users.post("/logout/", status_code=status.HTTP_401_UNAUTHORIZED)
def logout(authed_user=Depends(auth_service.get_auth_user)):
    pass
