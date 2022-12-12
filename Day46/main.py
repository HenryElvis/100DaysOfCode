import requests
from bs4 import BeautifulSoup

requests = requests.get("https://www.timeout.com/film/best-anime-movies")
requests = requests.text
soup = BeautifulSoup(requests, "html.parser")

animes = soup.select("h3")
anime = [anime.getText() for anime in animes]

for i in range(len(anime)):
    print(anime[i])

date = input("Enter a date in the format YYYY-MM-DD: ")

requests = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
requests = requests.text
soup = BeautifulSoup(requests, "html.parser")

