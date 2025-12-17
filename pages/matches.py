import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def main():
    st.header("📅 Premier League Matches (2023)")

    r = requests.get(f"{API_URL}/matches").json()
    fixtures = r.get("response", [])

    if not fixtures:
        st.warning("No matches found.")
        st.write(r)
        return

    rows = []
    for f in fixtures:
        rows.append({
            "Date": f["fixture"]["date"][:10],
            "Home": f["teams"]["home"]["name"],
            "Away": f["teams"]["away"]["name"],
            "Score": f'{f["goals"]["home"]} - {f["goals"]["away"]}',
            "Status": f["fixture"]["status"]["short"]
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)
