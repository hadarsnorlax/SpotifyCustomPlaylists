import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config

class SpotifyApi:
  def __init__(self):
    self.credentials = SpotifyClientCredentials(
      client_id=config.CLIENT_ID,
      client_secret=config.CLIENT_SECRET)
    self.spotify = spotipy.Spotify(client_credentials_manager=self.credentials)
    self.scope = "playlist-modify-public"

  def _get_playlist_id(self, playlist_name):
    if playlist_name not in config.PLAYLIST_IDS:
      raise(f"Invalid playlist name: {playlist_name}, playlist ID not in config")

    return config.PLAYLIST_IDS[playlist_name]

  def get_playlist_length(self, playlist_name):
    try:
      playlist_data = self.spotify.playlist(self._get_playlist_id(playlist_name))
      return playlist_data["tracks"]["total"]
    except Exception as err:
      raise(f"Failed to get playlist length: {playlist_name}, error: {err}")

  def get_playlist_songs(self, playlist_name):
    try:
      playlist_length = self.get_playlist_length(playlist_name)
      songs_limit = 100
      songs_offset = 0
      songs = []

      while (songs_offset < playlist_length):
        new_songs = self.spotify.playlist_tracks(self._get_playlist_id(playlist_name), 
                                                limit=songs_limit, 
                                                offset=songs_offset)
        songs.extend(new_songs["items"])
        songs_offset += songs_limit
      
      return songs

    except Exception as err:
      raise(f"Failed to retreive songs from playlist: {playlist_name}, error: {err}")
