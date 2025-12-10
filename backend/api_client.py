import requests

API_KEY = "53f92680f6e3a2588e7e5e074d7b54fa"

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_standings():
    url = f"{BASE_URL}/standings?league=39&season=2023"
    print("Requesting:", url)
    response = requests.get(url, headers=HEADERS)
    print("STATUS:", response.status_code)
    print("RAW:", response.text)
    return response.json()
