import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def main():
    st.header("🏆 Top Players")

    tab1, tab2, tab3 = st.tabs([
        "⚽ Top Scorers",
        "🎯 Top Assists",
        "⭐ Star Performers"
    ])

    # ---------- TOP SCORERS ----------
    with tab1:
        r = requests.get(f"{API_URL}/players/topscorers").json()
        players = r.get("response", [])

        if not players:
            st.warning("No data returned for top scorers.")
            st.write(r)
        else:
            data = []
            for i, p in enumerate(players, start=1):
                data.append({
                    "Rank": i,
                    "Player": p["player"]["name"],
                    "Team": p["statistics"][0]["team"]["name"],
                    "Goals": p["statistics"][0]["goals"]["total"]
                })

            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df.set_index("Player")["Goals"])

    # ---------- TOP ASSISTS ----------
    with tab2:
        r = requests.get(f"{API_URL}/players/topassists").json()
        players = r.get("response", [])

        if not players:
            st.warning("No data returned for top assists.")
            st.write(r)
        else:
            data = []
            for i, p in enumerate(players, start=1):
                data.append({
                    "Rank": i,
                    "Player": p["player"]["name"],
                    "Team": p["statistics"][0]["team"]["name"],
                    "Assists": p["statistics"][0]["goals"]["assists"]
                })

            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df.set_index("Player")["Assists"])
    # ---------- TOP PERFORMERS -----------
    with tab3:
        r = requests.get(f"{API_URL}/players/star-performers").json()
        players = r.get("response", [])

        rows = []

        for p in players:
            stats = p["statistics"][0]
            rating = stats["games"]["rating"]

            if rating is None:
                continue

            rows.append({
                "Player": p["player"]["name"],
                "Team": stats["team"]["name"],
                "Rating": float(rating),
                "Goals": stats["goals"]["total"],
                "Assists": stats["goals"]["assists"]
            })

        rows = sorted(rows, key=lambda x: x["Rating"], reverse=True)[:10]

        st.dataframe(rows, use_container_width=True)
