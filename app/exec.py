from uvicorn import run
from app import app


def main():
  run(
      app,
      port=8000,
      host="0.0.0.0",
      # log_level="warning",
      access_log=False,
  )
