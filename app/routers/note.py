from fastapi import APIRouter, Query
from typing import List, Optional

from app.repositories.environment import Environment

router = APIRouter(prefix='/notes')


@router.get('')
def play_note(n: int = Query(...), p: str = Query(None)):
  Environment.get_instance().player.playNote(port=p, note=n)
  return True


@router.delete('')
def delete_playing_note(p: List[str] = Query([])):
  env = Environment.get_instance()
  if not p:
    env.player.stopNote()
    return True
  for port in p:
    env.player.playNote(port=port, note=28)
  return True
