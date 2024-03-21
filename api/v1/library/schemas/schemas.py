from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ReadUser(BaseModel):
    name: str
    surname: str
    email: EmailStr


class CreateUser(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str


class ReadCreatedUser(BaseModel):
    id: int
    name: str


class ArticleCreate(BaseModel):
    name: str
    content: str


class ArticleRead(ArticleCreate):
    id: int
    user_id: int


class ReadUserWithArticles(BaseModel):
    id: int
    name: str
    surname: Optional[str]
    email: EmailStr

    articles: List[ArticleRead]

