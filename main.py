from api.spotify_api import SpotifyApi

if __name__ == "__main__":
  spotify = SpotifyApi()
  PLAYLIST_NAME = "all_songs"
  songs = spotify.get_playlist_songs(PLAYLIST_NAME)
  top_songs = spotify.get_top_songs()
  print(top_songs)
