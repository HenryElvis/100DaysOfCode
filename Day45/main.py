from bs4 import BeautifulSoup
import requests

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#print(soup.title.string)
#print(soup.prettify())

first_a = soup.select_one(selector="p a")
#print(first_a)

data = requests.get("https://henryelvis.fr/")
page = BeautifulSoup(data.text, "html.parser")

#print(page.title.string)
#print(page.select_one(selector="a").get("href"))

URL = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = URL.text
soup = BeautifulSoup(website, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in titles]
titles = titles[::-1]

with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for title in range(len(titles)):
        file.write(f"{titles[title]}\n")