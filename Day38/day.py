import requests
from datetime import datetime
import os

TODAY = datetime.today().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ['SHEEFTY_ENDPOINT']

TEXT = input("Tell me which exercises you did: ")

NUTRI_HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

POST_PARAMS = {
    "query": TEXT,
}

POST_HEADER = {
    "Authorization": f"Bearer {os.environ['AUTH']}"
}

response = requests.post(NUTRI_ENDPOINT, json=POST_PARAMS, headers=NUTRI_HEADER)
response.raise_for_status()

result = response.json()

for res in result["exercises"]:
    SHEETY_PARAMS = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": res["name"].title(),
            "duration": res["duration_min"],
            "calories": res["nf_calories"]
        }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_PARAMS, headers=POST_HEADER)
sheety_response.raise_for_status()

print(sheety_response.text)