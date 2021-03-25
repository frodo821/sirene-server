from serial import Serial, PARITY_NONE, EIGHTBITS, STOPBITS_ONE
from typing import List


class SerialConnector:
  def __init__(self, port: str):
    self.connector: Serial = Serial(
        port,
        baudrate=9600,
        parity=PARITY_NONE,
        bytesize=EIGHTBITS,
        stopbits=STOPBITS_ONE,
        timeout=5)

  def write(self, num: int):
    self.connector.write(f'{num}.'.encode('ascii'))
    self.connector.flushInput()
    self.connector.flushOutput()

  def close(self):
    self.connector.close()

  @classmethod
  def scanPorts(cls) -> List['SerialConnector']:
    ports = []
    for i in range(256):
      port = f"COM{i}"

      try:
        ports.append(cls(port))
      except:
        continue

    return ports
