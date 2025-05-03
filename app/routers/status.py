from typing import Optional

from app.domains.music import Music
from app.domains.play_music_params import MusicPlayingState, PlayMusicParam
from app.repositories.environment import Environment
from app.repositories.server import ServerRepository, ServerStatus
from app.usecases.get_server_status import GetServerStatus
from fastapi import APIRouter, Body, HTTPException

router = APIRouter(prefix='/status')


@router.get('', response_model=ServerStatus)
def get_status():
  env = Environment.get_instance()
  status = GetServerStatus(
      ServerRepository(env.player, env.lookup)
  ).execute()
  return dict(status)


@router.get('/play', response_model=Optional[Music])
def get_playing_music():
  env = Environment.get_instance()
  if env.player.music is None:
    return None
  return env.player.music.json()


@router.post('/play')
def post_playing_music(play_params: PlayMusicParam = Body(...)):
  env = Environment.get_instance()
  if play_params.loop_play and not env.player.looping:
    env.player.loop()

  if not play_params.loop_play and env.player.looping:
    env.player.unloop()

  if play_params.id is None:
    if play_params.state == MusicPlayingState.play:
      env.player.resume()
    else:
      env.player.pause()
    return True

  if env.player.music is None:
    music = env.lookup.lookup(play_params.id)

    if music is None:
      raise HTTPException(404)

    env.player.music = music
    env.player.resume()
    return True

  if env.player.music.id == play_params.id:
    if play_params.state == MusicPlayingState.play:
      env.player.resume()
    else:
      env.player.pause()
    return True

  env.player.reset()
  music = env.lookup.lookup(play_params.id)

  if music is None:
    raise HTTPException(404)

  if play_params.state == MusicPlayingState.play:
    env.player.resume()
  else:
    env.player.pause()

  env.player.music = music
  return True


@router.delete('/play')
def stop_playing_music():
  Environment.get_instance().player.reset()
  return True
