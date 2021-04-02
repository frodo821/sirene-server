from starlette.websockets import WebSocket
from fastapi import APIRouter
from threading import Thread
from asyncio import sleep

from app.repositories.initialization import player, config

router = APIRouter()
wait = 1 / config.get('time_resolution', 128)


@router.websocket('/ws')
async def connect_websocket(ws: WebSocket):
  await ws.accept()

  try:
    while True:
      await ws.send_json({
          "notes": player.playing_notes,
          "time": player.playback_time
      })
      await sleep(wait)
  except:
    await ws.close()
