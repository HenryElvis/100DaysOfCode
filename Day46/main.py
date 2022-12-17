import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.timeout.com/film/best-anime-movies")
response = response.text
soup = BeautifulSoup(response, "html.parser")

animes = soup.select("h3")
anime = [anime.getText() for anime in animes]

#for i in range(len(anime)):
#    print(anime[i])

#date = input("Enter a date in the format YYYY-MM-DD: ")

date = "2000-12-02"

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs = [song.getText().strip("\n\t") for song in songs]

for i in range(len(songs)):
    print(songs[i])
