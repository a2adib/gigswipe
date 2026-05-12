import os
from pydantic_settings import BaseSettings,SettingsConfigDict



class CustomBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.environ.get("ENV_FILE", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )
