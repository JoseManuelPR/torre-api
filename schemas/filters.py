from pydantic import BaseModel, Field #pylint: disable=no-name-in-module

class FiltersValidate(BaseModel):
  offset: str = Field(2, max_length=10)
  size: str = Field(20, max_length=30)
  aggregate: str = Field(5, max_length=10)