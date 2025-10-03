from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    SECRET_KEY: str
    
    POSTGRES_DRIVER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
