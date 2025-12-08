import streamlit as st
import requests

API_URL = "http://localhost:8000"

def login(username, password):
    response = requests.post(f"{API_URL}/auth/login", json={
        "username": username,
        "password": password
    })
    return response

def register(username, password):
    response = requests.post(f"{API_URL}/auth/register", json={
        "username": username,
        "password": password
    })
    return response


def main():
    st.title("Premier League Analyst - Login")

    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    if st.session_state.user_id:
        st.success(f"Logged in as user ID {st.session_state.user_id}")
        st.write("Continue to the dashboard →")
        return

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            resp = login(username, password)
            if resp.status_code == 200:
                st.session_state.user_id = resp.json()["user_id"]
                st.success("Logged in successfully!")
                st.experimental_rerun()
            else:
                st.error(resp.json()["detail"])

    with tab2:
        username = st.text_input("New Username", key="reg_user")
        password = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register"):
            resp = register(username, password)
            if resp.status_code == 200:
                st.success("Account created! You can now log in.")
            else:
                st.error(resp.json()["detail"])


if __name__ == "__main__":
    main()
