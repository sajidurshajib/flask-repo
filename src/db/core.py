from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import List, Union
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Flask-Repo"
    API_V1_STR: str = '/api/v1'
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ALGORITHM: str = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 69 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        os.environ.get("URL_ONE"),
        os.environ.get("URL_TWO"),
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)



settings = Settings()