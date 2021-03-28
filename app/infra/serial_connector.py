from serial import Serial, PARITY_NONE, EIGHTBITS, STOPBITS_ONE
from typing import List


class SerialConnector:
  TYPE_UNKNOWN = 0
  TYPE_SOPRANO = 1
  TYPE_ALTO = 2

  SIGNATURE_SOPRANO = 0x0b
  SIGNATURE_ALTO = 0xbe

  def __init__(self, port: str, *, use_experimental_arduino_driver=False):
    self.connector: Serial = Serial(
        port,
        baudrate=9600,
        parity=PARITY_NONE,
        bytesize=EIGHTBITS,
        stopbits=STOPBITS_ONE,
        timeout=5)

    self.kind = SerialConnector.TYPE_UNKNOWN

    if use_experimental_arduino_driver:
      self.connector.write(b'\x00\x00')
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
      self.connector.write(bytes([1, num]))

    self.connector.flushInput()
    self.connector.flushOutput()

  def close(self):
    self.connector.close()

  @classmethod
  def scanPorts(cls, *, use_experimental_arduino_driver=False) -> List['SerialConnector']:
    ports = []
    for i in range(256):
      port = f"COM{i}"

      try:
        ports.append(cls(port, use_experimental_arduino_driver=use_experimental_arduino_driver))
      except:
        continue

    return ports
