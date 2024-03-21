from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from database.db import get_session

from api.v1.library.schemas.schemas import ArticleRead, ArticleCreate
from api.v1.library.services import crud_service


articles = APIRouter(prefix="/articles", tags=["Articles"])


@articles.get("/", response_model=List[ArticleRead])
def get_articles(session=Depends(get_session)):
    all_articles = crud_service.get_articles(session=session)

    return all_articles


@articles.get("/{authors_id}", response_model=List[ArticleRead])
def get_article_by_authors_id(authors_id: int, session=Depends(get_session)):
    all_articles = crud_service.get_articles_by_author(session=session, authors_id=authors_id)

    if all_articles:
        return all_articles
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@articles.post("/", response_model=ArticleCreate, status_code=status.HTTP_201_CREATED)
def create_article(article: ArticleCreate, session=Depends(get_session)):
    new_article = crud_service.create_article(session=session, article=article)

    return new_article


@articles.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(article_id: int, session=Depends(get_session)):
    is_deleted = crud_service.delete_article(session=session, article_id=article_id)

    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
