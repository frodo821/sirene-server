from starlette.websockets import WebSocket
from fastapi import APIRouter
from threading import Thread
from asyncio import sleep

from app.repositories.environment import Environment

router = APIRouter()


@router.websocket('/ws')
async def connect_websocket(ws: WebSocket):
  env = Environment.get_instance()
  wait = 1 / env.config.time_resolution

  await ws.accept()

  try:
    while True:
      await ws.send_json({
        "notes": env.player.playing_notes,
        "time": env.player.playback_time,
      })
      await sleep(wait)
  except:
    await ws.close()
