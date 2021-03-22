from fastapi import APIRouter, Query
from typing import List, Optional

router = APIRouter(prefix='/notes')


@router.get('')
def play_note(n: int = Query(...), p: Optional[str] = Query(None)):
  pass


@router.delete('')
def delete_playing_note(p: List[str] = Query([])):
  pass
