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
