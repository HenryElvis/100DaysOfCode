import requests
from flight_data import FlightData
import os

ENDPOINT = "https://api.tequila.kiwi.com/"
API_KEY = os.environ.get("APIKEY")

HEADERS = {
    "apikey": API_KEY
}

class FlightSearch:
    def GetDestination(self, city):
        query = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=f"{ENDPOINT}/locations/query", headers=HEADERS, params=query)
        response.raise_for_status()
        result = response.json()["locations"]

        return result[0]["code"]

    def CheckFlight(self, origin_city, destination_city, from_time, to_time):
    
        query = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": from_time.strftime("%d%m%Y"),
            "date_to": to_time.strftime("%d%m%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{ENDPOINT}/v2/search", headers=HEADERS, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}")
            return None

        flight_data = FlightData(
            price = data["price"],
            origin_city = data["route"][0]["cityFrom"],
            origin_airport = data["route"][0]["flyFrom"],
            destination_city = data["route"][0]["cityTo"],
            destination_airport = data["route"][0]["flyTo"],
            out_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: {flight_data.price}")
        return flight_data