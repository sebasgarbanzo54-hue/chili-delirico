from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_url: str = "mongodb://localhost:27017"
    db_name: str = "chili_delirico"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    class Config:
        env_file = ".env"

settings = Settings()
