from typing import List

from pydantic import BaseModel, EmailStr


class ReadUser(BaseModel):
    name: str
    surname: str
    email: EmailStr
    articles: List["ArticleRead"]


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
    user_id: int


class ArticleRead(ArticleCreate):
    id: int
