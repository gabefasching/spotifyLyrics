from lib2to3.pgen2 import token
import os 
import json
import time
import spotipy
import lyricsgenius as lg


spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_UPI']
genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

scope = "user-read-currently-playing"

oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id, 
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_uri,
                                    scope=scope)


token_dict = oauth_object.get_cached_token()
token = token_dict['access_token']  

#  the spotify object
spotify_object = spotipy.Spotify(auth=token)                                

# the genius object
genius = lg.Genius(genius_access_token)

current = spotify_object.currently_playing()

artist_name = current['item']['album']['artists'][0]['name']
song_title = current['item']['name']

song = genius.search_song(title=song_title, artist=artist_name)
lyrics = song.lyrics
print(lyrics)
