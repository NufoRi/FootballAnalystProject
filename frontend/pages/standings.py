import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def fetch_standings():
    response = requests.get(f"{API_URL}/standings")
    return response.json()

def main():
    st.title("🏆 Premier League Standings 2025/26")

    standings = fetch_standings()

    if "error" in standings:
        st.error("Failed to load standings.")
        return

    # Build table rows
    table = []
    for team in standings:
        table.append([
            team["rank"],
            team["team"]["name"],
            team["all"]["played"],
            team["all"]["win"],
            team["all"]["draw"],
            team["all"]["lose"],
            team["goalsDiff"],
            team["points"]
        ])

    st.dataframe(
        {
            "Pos": [row[0] for row in table],
            "Team": [row[1] for row in table],
            "MP": [row[2] for row in table],
            "W": [row[3] for row in table],
            "D": [row[4] for row in table],
            "L": [row[5] for row in table],
            "GD": [row[6] for row in table],
            "Pts": [row[7] for row in table],
        },
        hide_index=True
    )

if __name__ == "__main__":
    main()
