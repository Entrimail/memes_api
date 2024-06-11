from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()


class Settings(BaseSettings):
    bucket_name: str
    endpoint: str
    access_key: str
    secret_key: str


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
