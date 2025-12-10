import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

BASE_URL = "https://api-football-v1.p.rapidapi.com/v3"

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

def get_standings():
    url = f"{BASE_URL}/standings?league=39&season=2025"
    print("Requesting:", url)
    response = requests.get(url, headers=HEADERS)
    print("STATUS:", response.status_code)
    print("RAW:", response.text)
    return response.json()
