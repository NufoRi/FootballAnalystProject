import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000/standings/"


def main():
    st.title("Premier League Standings (2023)")

    data = requests.get(API_URL).json()

    if "error" in data:
        st.error("Standings could not be loaded.")
        st.json(data)  # debug mode
        return

    rows = []
    for team in data:
        rows.append({
            "Rank": team["rank"],
            "Team": team["team"]["name"],
            "Logo": team["team"]["logo"],
            "Played": team["all"]["played"],
            "W": team["all"]["win"],
            "D": team["all"]["draw"],
            "L": team["all"]["lose"],
            "GF": team["all"]["goals"]["for"],
            "GA": team["all"]["goals"]["against"],
            "GD": team["goalsDiff"],
            "Points": team["points"]
        })

    df = pd.DataFrame(rows)

    def show_logo(url):
        return f"<img src='{url}' width='25'>"

    df["Logo"] = df["Logo"].apply(show_logo)

    df = df[
        ["Rank", "Logo", "Team", "Played", "W", "D", "L", "GF", "GA", "GD", "Points"]
    ]

    st.write(
        df.to_html(escape=False, index=False),
        unsafe_allow_html=True
    )
