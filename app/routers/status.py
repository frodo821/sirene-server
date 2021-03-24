from typing import Optional

from app.domains.music import Music
from app.domains.play_music_params import MusicPlayingState, PlayMusicParam
from app.repositories.initialization import lookup, player
from app.repositories.server import ServerRepository, ServerStatus
from app.usecases.get_server_status import GetServerStatus
from fastapi import APIRouter, Body, HTTPException

router = APIRouter(prefix='/status')


@router.get('', response_model=ServerStatus)
def get_status():
  status = GetServerStatus(
      ServerRepository(player, lookup)
  ).execute()
  return dict(status)


@router.get('/play', response_model=Optional[Music])
def get_playing_music():
  if player.music is None:
    return None
  return player.music.json()


@router.post('/play')
def post_playing_music(play_params: PlayMusicParam = Body(...)):
  if play_params.loop_play and not player.looping:
    player.loop()

  if not play_params.loop_play and player.looping:
    player.unloop()

  if play_params.id is None:
    if play_params.state == MusicPlayingState.play:
      player.resume()
    else:
      player.pause()
    return True

  if player.music is None:
    music = lookup.lookup(play_params.id)

    if music is None:
      raise HTTPException(404)

    player.music = music
    player.resume()
    return True

  if player.music.id == play_params.id:
    if play_params.state == MusicPlayingState.play:
      player.resume()
    else:
      player.pause()
    return True

  player.reset()
  music = lookup.lookup(play_params.id)

  if music is None:
    raise HTTPException(404)

  if play_params.state == MusicPlayingState.play:
    player.resume()
  else:
    player.pause()

  player.music = music
  return True


@router.delete('/play')
def stop_playing_music():
  player.reset()
  return True
