from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@db:5432/contracts"
    MINIO_ENDPOINT: str = "minio:9000"
    MINIO_ACCESS_KEY: str = "minio"
    MINIO_SECRET_KEY: str = "minio123"
    MINIO_BUCKET: str = "contracts"
    MINIO_SECURE: bool = False
    SPACY_MODEL: str = "ru_core_news_lg"

    class Config:
        env_file = ".env"

settings = Settings()
