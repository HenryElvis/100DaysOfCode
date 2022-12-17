import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

URL = "https://www.amazon.fr/Console-Nintendo-Switch-avec-rouge/dp/B0BHDDH5W1/ref=sr_1_1?keywords=nintendo%2Bswitch&qid=1671307132&sprefix=%2Caps%2C58&sr=8-1&th=1"

EMAIL = "your email"
PASSWORD = "your password"

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml");

price = soup.find(class_="a-offscreen").get_text().split("€")[0]

price = float(price.replace(",", "."))

if price < 200:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Amazon Price Alert\n\nThe price of the Nintendo Switch has dropped below 200€. Check the link: https://www.amazon.fr/Console-Nintendo-Switch-avec-rouge/dp/B0BHDDH5W1/ref=sr_1_1?keywords=nintendo%2Bswitch&qid=1671307132&sprefix=%2Caps%2C58&sr=8-1&th=1")