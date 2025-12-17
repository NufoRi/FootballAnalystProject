import requests

API_KEY = "53f92680f6e3a2588e7e5e074d7b54fa"
BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_standings():
    url = f"{BASE_URL}/standings?league=39&season=2023"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_top_scorers(season=2023):
    url = f"{BASE_URL}/players/topscorers"
    params = {"league": 39, "season": season}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()


def get_top_assisters(season=2023):
    url = f"{BASE_URL}/players/topassists"
    params = {"league": 39, "season": season}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()


def get_star_performers(season=2023):
    url = f"{BASE_URL}/players/topscorers"
    params = {"league": 39, "season": season}
    r = requests.get(url, headers=HEADERS, params=params, timeout=15).json()

    if "response" not in r:
        return r

    players = r["response"]

    def rating_of(p):
        rating = p["statistics"][0]["games"].get("rating")
        try:
            return float(rating)
        except:
            return 0.0

    players.sort(key=rating_of, reverse=True)
    return {"response": players[:10]}


def get_matches(season=2023, league=39):
    url = f"{BASE_URL}/fixtures"
    params = {
        "league": league,
        "season": season
    }
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def get_teams(season=2023, league=39):
    url = f"{BASE_URL}/teams"
    params = {
        "league": league,
        "season": season
    }
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

