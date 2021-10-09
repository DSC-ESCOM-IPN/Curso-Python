from os import getenv

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    db_url = getenv("DATABASE_URL", default="")


settings = Settings()
