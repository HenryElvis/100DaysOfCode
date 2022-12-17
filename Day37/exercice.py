import requests
from datetime import datetime as time

today = time.now()

USERNAME = "elvishenry"
TOKKEN = "pixelauserelvis"

GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PUT_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20220902"
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20220902"

PIXELA_PARAMS = {
    "token": TOKKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

GRAPHS_PARAMS = {
    "id": GRAPH_ID,
    "name": "100DaysOfCode",
    "unit": "commit",
    "type": "float",
    "color": "momiji"
}

POST_PARAMS = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

PUT_PARAMS = {
    "quantity": "10"
}

HEADER = {
    "X-USER-TOKEN": TOKKEN
}

# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMS)
# print(response.text)

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPHS_PARAMS, headers=HEADER)
# print(response.text)

# response = requests.post(url=POST_ENDPOINT, json=POST_PARAMS, headers=HEADER)
# print(response.text)

# response = requests.put(url=PUT_ENDPOINT, json=PUT_PARAMS, headers=HEADER)
# print(response.text)

response = requests.delete(url=DELETE_ENDPOINT, headers=HEADER)
print(response.text)