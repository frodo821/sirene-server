from sys import exc_info
from traceback import print_exception
from threading import Thread
from time import sleep, time
from typing import List, Optional

from app.domains.midi import MidiFile
from app.infra.serial_connector import SerialConnector
from fastapi.exceptions import HTTPException
from pretty_midi import Note


class MidiPlayer:
  def __init__(self, resolution: int, *, use_experimental_arduino_driver=False, debuging_virtual_devices=0):
    self.connectors: List[SerialConnector] = SerialConnector.scanPorts(
        use_experimental_arduino_driver=use_experimental_arduino_driver,
        debuging_virtual_devices=debuging_virtual_devices
    )
    self.music: Optional[MidiFile] = None
    self.running: bool = True
    self.__paused: bool = False
    self.worker: Thread = Thread(target=self.run)
    self.ticks: int = 0
    self.indices: List[int] = [0] * len(self.connectors)
    self.playing_notes: List[int] = [-1] * len(self.connectors)
    self.resolution = resolution
    self.__loop: bool = False

    self.worker.start()

  @property
  def resolution(self) -> int:
    return self.__resolution

  @property
  def tick_dur(self) -> float:
    return self.__tick_dur

  @property
  def paused(self) -> bool:
    return self.__paused

  @property
  def tracks(self) -> Optional[int]:
    if self.music is None:
      return None
    return len(self.music.midi.instruments)

  @resolution.setter
  def resolution(self, value: int):
    self.__resolution = value
    self.__tick_dur = 1 / value

  @property
  def playback_time(self) -> float:
    return self.__tick_dur * self.ticks

  @playback_time.setter
  def playback_time(self, value: float):
    self.ticks = int(value / self.__tick_dur)

  def close(self):
    self.running = False

    for connector in self.connectors:
      connector.close()

  def reset(self):
    if not self.running:
      raise RuntimeError("Worker already died")

    self.music: Optional[MidiFile] = None
    self.ticks = 0
    self.indices = [0] * len(self.connectors)
    self.playing_notes = [-1] * len(self.connectors)
    self.__paused = False

    for connector in self.connectors:
      connector.write(28)

  def tick(self):
    for idx, inst in enumerate(self.music.midi.instruments):
      if not self.connectors[idx:]:
        break

      if inst.is_drum or self.indices[idx] == -1:
        continue

      if not inst.notes[self.indices[idx]:]:
        self.indices[idx] = -1
        continue

      note: Note = inst.notes[self.indices[idx]]

      if abs(note.end - self.ticks * self.__tick_dur) < self.tick_dur:
        self.connectors[idx].write(27)
        self.indices[idx] += 1
        self.playing_notes[idx] = -1

      if abs(note.start - self.ticks * self.__tick_dur) < self.tick_dur:
        pitch = note.pitch - 60
        self.connectors[idx].write(pitch)
        self.playing_notes[idx] = pitch

  def playNote(self, port: str, note: int):
    if self.music and not self.__paused:
      raise HTTPException(409, {"error": "server currently playing a music. pause or stop performance first."})

    conn = [conn for conn in self.connectors if conn.connector.port == port]

    if not conn:
      raise HTTPException(404, {"error": f"port {port} is not connected."})

    conn[0].write(note)

  def stopNote(self):
    if self.music and not self.__paused:
      raise HTTPException(409, {"error": "server currently playing a music. pause or stop performance first."})

    for conn in self.connectors:
      conn.write(27)

  def pause(self):
    self.__paused = True

    for connector in self.connectors:
      connector.write(27)

  def resume(self):
    self.__paused = False

  def loop(self):
    self.__loop = True

  def unloop(self):
    self.__loop = False

  @property
  def looping(self) -> bool:
    return self.__loop

  def run(self):
    while self.running:
      try:
        frame_start_time = time()

        if not (self.__paused or self.music is None):
          self.tick()
          self.ticks += 1

        if all(i == -1 for i in self.indices[:self.tracks]):
          if self.__loop:
            music: MidiFile = self.music
            self.reset()
            self.music = music
          else:
            self.reset()

        sleep_start = time()
        while (max(self.tick_dur - (sleep_start - frame_start_time), 0)) > (time() - sleep_start):
          sleep(0)

      except:
        print_exception(*exc_info())
