import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

response = requests.get("https://www.timeout.com/film/best-anime-movies")
response = response.text
soup = BeautifulSoup(response, "html.parser")

animes = soup.select("h3")
anime = [anime.getText() for anime in animes]

ID = os.environ.get("SPOTIFY_ID")
SECRET = os.environ.get("SPOTIFY_SECRET")

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Enter a date in the format YYYY-MM-DD: ")
response = requests.get(URL + date)

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs = [song.getText().strip("\n\t") for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback/",
        client_id=ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

sounds = []
year = date.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        sounds.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard {len(sounds)}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=sounds)

print(playlist)