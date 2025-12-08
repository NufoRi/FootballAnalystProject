import requests
import os

API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_standings():
    url = f"{BASE_URL}/standings?league=39&season=2025"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_teams():
    url = f"{BASE_URL}/teams?league=39&season=2025"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_fixtures():
    url = f"{BASE_URL}/fixtures?league=39&season=2025"
    response = requests.get(url, headers=HEADERS)
    return response.json()
