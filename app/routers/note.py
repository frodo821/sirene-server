from fastapi import APIRouter, Query
from typing import List, Optional

from app.repositories.initialization import player

router = APIRouter(prefix='/notes')


@router.get('')
def play_note(n: int = Query(...), p: str = Query(None)):
  player.playNote(port=p, note=n)
  return True


@router.delete('')
def delete_playing_note(p: List[str] = Query([])):
  if not p:
    player.stopNote()
    return True
  for port in p:
    player.playNote(port=port, note=28)
  return True
