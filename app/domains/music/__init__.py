# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from pydantic import BaseModel


class Music(BaseModel):
  id: int
  name: str
  length: float
