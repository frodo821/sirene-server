# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class MusicPlayingState(str, Enum):
  play = "play"
  paused = "paused"


class PlayMusicParam(BaseModel):
  id: int
  play_at: Optional[float]
  play_device_ports: Optional[List[str]]
  state: MusicPlayingState
