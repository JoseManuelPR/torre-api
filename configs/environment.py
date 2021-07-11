from typing import Any
from pydantic import BaseSettings

class Settings(BaseSettings):
  """ Environments """
  DEBUG: bool = False
  ENV: bool = False
  ERROR_404_HELP: bool = False

  PROJECT_NAME: str = 'API'
  PROJECT_API_VERSION: str = '0.1.0'
  DOCS_URL: str = 'None'
  REDOC_URL: str = 'None'

  class Config:
    env_file = '.env'

Config = Settings()
