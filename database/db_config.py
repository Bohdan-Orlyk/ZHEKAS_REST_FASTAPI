from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    db_name: str
    db_url_prefix: str
    db_echo_mode: bool = False


def get_db_config() -> DBSettings:
    return DBSettings()
