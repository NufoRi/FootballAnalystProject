import streamlit as st
import requests

API_URL = "http://localhost:8000"

def main():
    st.title("Premier League Standings")

    try:
        response = requests.get(f"{API_URL}/standings")
        data = response.json()

        st.table(data)

    except Exception as e:
        st.error(f"Error loading standings: {e}")
