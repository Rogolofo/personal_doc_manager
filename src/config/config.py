from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str
    APP_VERSION: str
    APP_DESCRIPTION: str = "API for managing documents"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    STORAGE_PATH: str = "./storage"
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
