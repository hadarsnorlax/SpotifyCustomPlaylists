import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config

class SpotifyApi:
  def __init__(self):
    self.credentials = SpotifyClientCredentials(
      client_id=config.CLIENT_ID,
      client_secret=config.CLIENT_SECRET)
    self.spotify = spotipy.Spotify(client_credentials_manager=self.credentials, 
                                  auth=config.AUTH_TOKEN)

  def _get_playlist_id(self, playlist_name):
    if playlist_name not in config.PLAYLIST_IDS:
      raise Exception(f"Invalid playlist name: {playlist_name}, playlist ID not in config")

    return config.PLAYLIST_IDS[playlist_name]

  def get_playlist_length(self, playlist_name):
    try:
      playlist_data = self.spotify.playlist(self._get_playlist_id(playlist_name))
      return playlist_data["tracks"]["total"]
    except Exception as err:
      raise Exception(f"Failed to get playlist length: {playlist_name}, error: {err}")

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
      raise Exception(f"Failed to retreive songs from playlist: {playlist_name}, error: {err}")

  def get_top_songs(self):
    try:
      songs_limit = 50
      songs_offset = 0
      top_songs = []

      while True:
        songs = self.spotify.current_user_top_tracks(limit=songs_limit,
                                                    offset=songs_offset,
                                                    time_range="long_term")
        top_songs.extend(songs["items"])
        songs_offset += songs_limit

        if not songs["next"]:
          break
      
      return top_songs

    except Exception as err:
      raise Exception(f"Failed to retreive top songs for the user: {config.USERNAME}, error: {err}")
