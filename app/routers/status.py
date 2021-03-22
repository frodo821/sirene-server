from fastapi import APIRouter, Body
from app.usecases.get_server_status import GetServerStatus
from app.repositories.server import ServerRepository, ServerStatus
from app.repositories.initialization import player, lookup
from app.domains.play_music_params import PlayMusicParam

router = APIRouter(prefix='/status')


@router.get('', response_model=ServerStatus)
def get_status():
  status = GetServerStatus(
      ServerRepository(player, lookup)
  ).execute()
  return dict(status)


@router.get('/play')
def get_playing_music():
  pass


@router.post('/play')
def post_playing_music(play_params: PlayMusicParam = Body(...)):
  pass


@router.delete('/play')
def stop_playing_music():
  pass
