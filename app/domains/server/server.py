# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from pydantic import BaseModel
from typing import List, Optional


class Port(BaseModel):
  port: str


class ServerStatus(BaseModel):
  playing: bool
  connectedPorts: List[Port]
  playingMusic: Optional[str]
