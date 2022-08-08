import os
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):

    KEYCLOAK_SERVER_ADDRESS: str = os.getenv('KEYCLOAK_SERVER_ADDRESS')
    KEYCLOAK_USER: str = os.getenv('KEYCLOAK_USER')
    KEYCLOAK_PASSWORD: str = os.getenv('KEYCLOAK_PASSWORD')
    KEYCLOAK_CLIENT: str = os.getenv('KEYCLOAK_CLIENT')
    KEYCLOAK_REALM_NAME: str = os.getenv('KEYCLOAK_REALM_NAME')
    KEYCLOAK_CLIENT_SECRET_KEY: str = os.getenv('KEYCLOAK_CLIENT_SECRET_KEY')

    AVATAR_DB: str = os.getenv('AVATAR_DB')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings
