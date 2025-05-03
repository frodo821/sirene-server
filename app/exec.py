import random
from threading import Thread
from time import sleep
import webbrowser
from uvicorn import run
from app import app


def main():
  port = random.randint(
    10000,
    40000,
  )

  Thread(target=lambda: (sleep(2), webbrowser.open(f"http://localhost:{port}/"))).start()

  run(
    app,
    port=port,
    host="0.0.0.0",
    access_log=False,
    # log_level="warning",
  )
