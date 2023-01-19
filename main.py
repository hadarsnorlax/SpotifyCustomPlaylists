from api.spotify_api import SpotifyApi

if __name__ == "__main__":
  spotify = SpotifyApi()
  PLAYLIST_NAME = "all_songs"
  songs = spotify.get_playlist_songs(PLAYLIST_NAME)
  print(songs)
