from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    LOGGING_CONF_FILE: str = 'logging.yml'
    LOGGING_LEVEL: str = 'DEBUG'

    class Config:
        env_file = ".env"


settings = Settings()
