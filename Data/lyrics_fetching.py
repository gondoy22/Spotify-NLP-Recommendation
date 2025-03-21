import lyricsgenius
import requests

#Get your own access token from Genius API
ACCESS_TOKEN = 'ACCES_TOKEN_HERE'

genius = lyricsgenius.Genius(ACCESS_TOKEN)

lyrics_fetched_count = 0

def fetch_lyrics(song_title, artist_name):
    global lyrics_fetched_count 
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_fetched_count += 1
            print(f"Fetched lyrics for: {song_title} by {artist_name}. Total lyrics fetched: {lyrics_fetched_count}")
            return song.lyrics
        else:
            print(f"Song {song_title} by {artist_name} not found.")
            return None
    except requests.exceptions.RequestException as e:
        print('Error Fetching')
        return None
