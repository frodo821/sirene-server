from app.domains.server.server_repository_interface import ServerRepositoryInterface
from app.infra.file_lookup import FileLookup
from app.infra.player import MidiPlayer


class ServerRepository(ServerRepositoryInterface):
  def __init__(self, player: MidiPlayer, lookup: FileLookup):
    self.player = player
    self.lookup = lookup

  def get_current_status(self):
    self.player
