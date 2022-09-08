import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv("../../EnvVar/.env.txt")

Client_ID = os.getenv("CLIENT_ID")
Client_Secret = os.getenv("CLIENT_SECRET")
Redirect_Url = os.getenv("REDIRECT_URL")

date = input("Billboard Hot 100 Date (YYYY-MM-DD in this format): ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("li h3", class_="c-title")

song_list = [song.getText().strip() for song in songs]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=Client_ID,
        client_secret=Client_Secret,
        redirect_uri=Redirect_Url,
        scope="playlist-modify-private"))

user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_uris = []

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"In Spotify {song} doesn't exist.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
