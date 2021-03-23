from app.domains.server.server_repository_interface import ServerRepositoryInterface
from app.infra.file_lookup import FileLookup
from app.infra.player import MidiPlayer
from app.domains.server.server import ServerStatus


class ServerRepository(ServerRepositoryInterface):
  def __init__(self, player: MidiPlayer, lookup: FileLookup):
    self.player = player
    self.lookup = lookup

  def get_current_status(self):
    playing = bool(self.player.music) and not self.player.paused
    connectedPorts = [{"port": conn.connector.port} for conn in self.player.connectors]

    if self.player.music is None:
      return ServerStatus(
          playing=playing,
          connectedPorts=connectedPorts,
          playingMusic=None
      )

    music = self.player.music.json()
    music['playback_time'] = self.player.playback_time

    return ServerStatus(
        playing=playing,
        connectedPorts=connectedPorts,
        playingMusic=music)
