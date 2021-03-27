from starlette.websockets import WebSocket
from fastapi import APIRouter
from threading import Thread
from asyncio import sleep

from app.repositories.initialization import player

router = APIRouter()


@router.websocket('')
async def connect_websocket(ws: WebSocket):
  await ws.accept()

  try:
    while True:
      ws.send_json({
          "notes": player.playing_notes,
          "time": player.playback_time
      })
      await sleep(0.1)
  finally:
    await ws.close()
