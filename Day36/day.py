import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEW_API_KEY = os.environ.get("API_KEY_NEWSAPI")
KEY = os.environ.get("API_KEY_ALPHA_AVANTAGE")

PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": KEY
}

ACCOUNT_SID = "ACd7b9aab0b9f3548d1077c4d18fd5a99f"
AUTH_TOKKEN = os.environ.get("AUTH_TOKKEN_TWILLIO")
TEL = "+16187643829"

request = requests.get(url=STOCK_ENDPOINT, params=PARAMS)
request.raise_for_status()

data = request.json()["Time Series (Daily)"]

data_list = [value for key, value in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = (abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))) / float(yesterday_closing_price) * 100

if difference > 2:
    PARAMS = {
        "apiKey": NEW_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    request = requests.get(url=NEWS_ENDPOINT, params=PARAMS)
    request.raise_for_status()

    articles = request.json()["articles"][:3]

    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}.\nURL: {article['url']}." for article in articles]

    client = Client(ACCOUNT_SID, AUTH_TOKKEN)
    
    for article in formatted_articles:
        message = client.messages \
            .create(
                body= article,
                from_=TEL,
                to="+33 7 68 94 94 89"
            )

        print(message.status)