from bs4 import BeautifulSoup
#import lxml
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

print(page.title.string)
print(page.select_one(selector="a").get("href"))