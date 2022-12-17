import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/d70ae35e88903df8584001603f2ba8e4/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.data = {}

    def GetDataFromSheety(self):
        request = requests.get(url=SHEETY_ENDPOINT)
        request.raise_for_status()

        self.data = request.json()["prices"]

        return self.data

    def MakePutRequest(self):
        for city in self.data:
            new_city = {
                "price": {
                    "iataCode": "TESTING"
                }
            }
        
            request = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_city)
            print(request.text)
