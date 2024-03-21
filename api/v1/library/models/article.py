from typing import Optional

from sqlmodel import Field, SQLModel, Relationship


class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(nullable=False)
    content: str = Field(nullable=False)

    user_id: int = Field(foreign_key="user.id", nullable=False)
    user: "User" = Relationship(back_populates="articles")
