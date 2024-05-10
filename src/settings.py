import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../.env', 
        env_file_encoding='utf-8'
    )
    GEODB_DESTINY: str = os.environ['GEODB_DESTINY']
    FEATURE_URL: str = os.environ['FEATURE_URL']
