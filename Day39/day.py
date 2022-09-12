import time
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

data_manager = DataManager()
sheety_data = data_manager.GetDataFromSheety()
flight_search = FlightSearch()

ORIGIN_CITY = "CDG"

if sheety_data[0]["iataCode"] == "":
    for row in sheety_data:
        row["iataCode"] = flight_search.GetDestination(row["city"])
    data_manager.data = sheety_data
    data_manager.MakePutRequest()

tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=(6 * 30))

for destination in sheety_data:
    flight = flight_search.CheckFlight(
        origin_city = ORIGIN_CITY,
        destination_city=["iataCode"],
        from_time= tomorrow,
        to_time= six_month
    )