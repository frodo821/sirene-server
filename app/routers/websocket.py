from starlette.websockets import WebSocket
from fastapi import APIRouter
from threading import Thread
from asyncio import sleep

from app.repositories.initialization import player

router = APIRouter()


@router.websocket('/ws')
async def connect_websocket(ws: WebSocket):
  await ws.accept()

  try:
    while True:
      if player.music and not player.paused:
        await ws.send_json({
            "notes": player.playing_notes,
            "time": player.playback_time
        })
      await sleep(0.1)
  except:
    await ws.close()
