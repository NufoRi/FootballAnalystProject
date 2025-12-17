import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def main():
    st.header("🏟️ Premier League Teams (2023)")

    r = requests.get(f"{API_URL}/teams").json()
    teams = r.get("response", [])

    if not teams:
        st.warning("No teams found")
        st.write(r)
        return

    # grid layout
    cols = st.columns(4)

    for i, t in enumerate(teams):
        with cols[i % 4]:
            st.image(
                t["team"]["logo"],
                width=80
            )
            st.markdown(f"**{t['team']['name']}**")
            st.caption(t["venue"]["name"])
