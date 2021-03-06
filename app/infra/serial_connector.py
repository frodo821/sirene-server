import pysinewave
from serial import Serial
from typing import List
from time import sleep
from warnings import warn
from pysinewave import SineWave


class MockingConnector:
  __debugging = 0

  class MockingPort:
    def __init__(self, i) -> None:
      self.port = f"DEBUG {i}"

  def __init__(self) -> None:
    self.sw = SineWave(pitch=0, pitch_per_second=1000, decibels_per_second=1000)
    self.connector = MockingConnector.MockingPort(MockingConnector.__debugging)
    self.playing = False
    MockingConnector.__debugging += 1
    self.sw.play()
    self.sw.sinewave_generator.amplitude = 0.0

  def write(self, num: int):
    if num in (27, 28):
      self.sw.sinewave_generator.amplitude = 0.0
      self.playing = False
      return

    if not self.playing:
      self.sw.sinewave_generator.amplitude = 1.0
      self.playing = True
    self.sw.set_pitch(num)

  def close(self):
    self.sw.stop()


class SerialConnector:
  TYPE_UNKNOWN = 0
  TYPE_SOPRANO = 1
  TYPE_ALTO = 2

  SIGNATURE_SOPRANO = 0x0b
  SIGNATURE_ALTO = 0xbe

  def __init__(self, port: str, *, use_experimental_arduino_driver=False):
    self.connector: Serial = Serial(
        port,
        baudrate=19200,
        timeout=1)

    self.kind = SerialConnector.TYPE_UNKNOWN

    if use_experimental_arduino_driver:
      # 始めに1.6秒以上のウェイトがないとなぜか読み書きがうまくいかない
      sleep(1.6)
      self.connector.write(b'\0\0')
      data = self.connector.read()

      if not data:
        self.connector.close()
        raise RuntimeError("Unknown or broken device.")

      if data[0] == SerialConnector.SIGNATURE_SOPRANO:
        self.kind = SerialConnector.TYPE_SOPRANO

      elif data[0] == SerialConnector.SIGNATURE_ALTO:
        self.kind = SerialConnector.TYPE_ALTO

      else:
        self.connector.close()
        raise RuntimeError("Invalid response from arduino")

  def write(self, num: int):
    if self.kind == SerialConnector.TYPE_UNKNOWN:
      self.connector.write(f'{num}.'.encode('ascii'))
    else:
      if 0 <= num <= 255:
        self.connector.write(bytes([1, num]))
      else:
        warn(f"Out of bound note: {num}, it may be skipped.", RuntimeWarning)

    self.connector.flushInput()
    self.connector.flushOutput()

  def close(self):
    self.connector.close()

  @classmethod
  def scanPorts(cls, *, use_experimental_arduino_driver=False, debuging_virtual_devices=0) -> List['SerialConnector']:
    ports = []
    for i in range(debuging_virtual_devices):
      ports.append(MockingConnector())

    for i in range(256):
      port = f"COM{i}"

      try:
        ports.append(cls(port, use_experimental_arduino_driver=use_experimental_arduino_driver))
      except RuntimeError as err:
        print(err)
        continue
      except:
        pass

    return ports
