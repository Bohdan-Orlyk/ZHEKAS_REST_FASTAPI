from sqlmodel import create_engine, SQLModel, Session
from database.db_config import get_db_config

from api.v1.library import models


# sqlite_file_name = "zhekas.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

db_config = get_db_config()
sqlite_url = f"{db_config.db_url_prefix}{db_config.db_name}"

engine = create_engine(sqlite_url, echo=db_config.db_echo_mode)


def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
