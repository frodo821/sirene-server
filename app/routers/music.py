from typing import List

from app.domains.music import Music
from app.repositories.initialization import lookup
from fastapi.routing import APIRouter, HTTPException

router = APIRouter(prefix='/musics')


@router.get('', response_model=List[Music])
def get_music_list():
  return [file.json() for file in lookup.files]


@router.get('/{music_id}', response_model=Music)
def get_music(music_id: int):
  music = lookup.lookup(music_id)

  if music is None:
    raise HTTPException(404)

  return music.json()
