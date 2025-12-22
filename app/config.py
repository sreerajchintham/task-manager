from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):

    app_name : str = "Task Manager"
    database_url : str = "sqlite:///./tasks.db"
    debug: bool = False
    model_config = SettingsConfigDict(env_file=".env")

    # class Config:  DOES THE SAME THING AS SETTINGS CPONFIG DICT BUT IS OLDER WAY OF DOING THINGS

@lru_cache
def get_settings() -> Settings:
    """
    Returns cached settings instance.
    Using lru_cache so we don't read .env file on every request.
    """
    return Settings()