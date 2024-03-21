from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(nullable=False)
    surname: str = Field(nullable=True)
    email: str = Field(nullable=False, index=True, unique=True)
    password: str = Field(nullable=False)

    articles: List["Article"] = Relationship(back_populates="user")
