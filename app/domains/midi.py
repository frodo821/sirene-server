from pretty_midi import PrettyMIDI


class MidiFile:
  id: int
  name: str
  midi: PrettyMIDI
  duration: float

  def __init__(self, id: int, file: str):
    self.id = id
    self.name = file.rsplit('/', 1)[1].rsplit('.', 1)[0]
    self.midi = PrettyMIDI(file)
    self.duration = self.midi.get_end_time()

  def json(self):
    return {
        "id": self.id,
        "name": self.name,
        "duration": self.duration
    }
