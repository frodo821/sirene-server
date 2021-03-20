from app.infra.serialConnector import SerialConnector
from pretty_midi import Instrument, Note
from app.domains.midi import MidiFile
from typing import List, Optional
from time import sleep
from threading import Thread


class MidiPlayer:
  connectors: List[SerialConnector]
  music: Optional[MidiFile]
  running: bool
  paused: bool
  worker: Thread
  ticks: int

  def __init__(self, resolution: int):
    self.connectors = SerialConnector.scanPorts()
    self.music = None
    self.running = True
    self.paused = False
    self.worker = Thread(target=self.run)
    self.ticks = 0
    self.indices = [0] * len(self.connectors)
    self.resolution = resolution

    self.worker.start()

  @property
  def resolution(self) -> int:
    return self.__resolution

  @property
  def tick_dur(self) -> float:
    return self.__tick_dur

  @resolution.setter
  def set_resolution(self, value: int):
    self.__resolution = value
    self.__tick_dur = 1 / value

  def close(self):
    for connector in self.connectors:
      connector.close()

  def reset(self):
    if not self.running:
      raise RuntimeError("Worker already died")

    self.music = None
    self.ticks = 0
    self.indices = [0] * len(self.connectors)

    for connector in self.connectors:
      connector.write(28)

  def tick(self):
    assert self.music is not None

    for idx, inst in enumerate(self.music.midi.instruments):
      if not self.connectors[idx:]:
        break

      if inst.is_drum:
        continue

      note: Note = inst.notes[self.indices[idx]]

      if abs(note.end - self.ticks / self.resolution) < self.tick_dur:
        self.connectors[idx].write(27)

      elif abs(note.start - self.ticks / self.resolution) < self.tick_dur:
        self.connectors[idx].write(note.pitch - 60)
        self.indices[idx] += 1

  def run(self):
    while self.running:
      if not (self.paused or self.music is None):
        self.tick()
        self.tick_dur += 1

      sleep(self.tick_dur)
