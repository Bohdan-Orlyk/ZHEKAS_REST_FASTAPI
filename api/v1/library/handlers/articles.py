from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from database.db import get_session

from api.v1.library.schemas.schemas import ArticleRead, ArticleCreate
from api.v1.library.services import crud_service, auth_service


articles = APIRouter(prefix="/articles", tags=["Articles"])


@articles.get("/", response_model=List[ArticleRead])
def get_articles(session=Depends(get_session)):
    all_articles = crud_service.get_articles(session=session)

    return all_articles


@articles.get("/by-user/", response_model=List[ArticleRead])
def get_article_by_authors_id(authed_user=Depends(auth_service.get_auth_user),
                              session=Depends(get_session)):
    all_articles = crud_service.get_articles_by_author(session=session, authors_id=authed_user.id)

    return all_articles


@articles.post("/", response_model=ArticleRead, status_code=status.HTTP_201_CREATED)
def create_article(article: ArticleCreate,
                   session=Depends(get_session),
                   authed_user=Depends(auth_service.get_auth_user)):
    new_article = crud_service.create_article(session=session, article=article, user_id=authed_user.id)

    return new_article


@articles.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(article_id: int, session=Depends(get_session), authed_user=Depends(auth_service.get_auth_user)):
    is_deleted = crud_service.delete_article(session=session, article_id=article_id, user_email=authed_user.email)

    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
