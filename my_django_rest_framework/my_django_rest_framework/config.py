from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    SECRET_KEY: str
    DRIVER: str
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
