from sqlmodel import create_engine, SQLModel, Session

from api.v1.library import models


sqlite_file_name = "zhekas.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)  # TODO change later to False


def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
