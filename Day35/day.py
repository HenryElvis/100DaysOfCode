import requests
from twilio.rest import Client

KEY = "59709b06b30ca6984f3d7a9ad8da18a5"

ACCOUNT_SID = "ACd7b9aab0b9f3548d1077c4d18fd5a99f"
AUTH_TOKKEN = "506158a7f21d7b1674001c58fbc81b09"
TEL = "+16187643829"

LNG = 2.3488
LAT = 48.8534

PARAMS = {
    "lat": LAT,
    "lon": LNG,
    "exclude": "current,minutely,daily",
    "appid": KEY
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMS)
request.raise_for_status()

hourly_hour = request.json()["hourly"][:13]

array_weather_id = [hourly_hour[id]["weather"][0]["id"] for id in range(12)]

for id in array_weather_id:
    if int(id) < 700:
        client = Client(ACCOUNT_SID, AUTH_TOKKEN)

        message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an umbrella.",
                from_=TEL,
                to="+33 7 68 94 94 89"
            )
        
        print(message.status)
    break
