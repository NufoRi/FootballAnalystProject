import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------
# AUTH FUNCTIONS
# ---------------------------
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


# ---------------------------
# MAIN APP
# ---------------------------
def main():
    st.title("Premier League Analyst")

    # Initialize session
    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    # If logged in → show sidebar navigation
    if st.session_state.user_id:
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Home", "Standings", "Logout"])

        if page == "Home":
            st.subheader("Welcome to the Dashboard!")
            st.write("Select a page from the sidebar.")

        elif page == "Standings":
            from pages.standings import main as standings_page
            standings_page()

        elif page == "Logout":
            st.session_state.user_id = None
            st.rerun()

        return

    # ---------------------------
    # LOGIN / REGISTER SCREEN
    # ---------------------------
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            resp = login(username, password)
            if resp.status_code == 200:
                st.session_state.user_id = resp.json()["user_id"]
                st.success("Logged in successfully!")
                st.rerun()
            else:
                try:
                    st.error(resp.json().get("detail", "Unknown error"))
                except:
                    st.error("Backend returned non-JSON response: " + resp.text)

    with tab2:
        username = st.text_input("New Username", key="reg_user")
        password = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register"):
            resp = register(username, password)
            if resp.status_code == 200:
                st.success("Account created! You can now log in.")
            else:
                try:
                    st.error(resp.json().get("detail", "Unknown error"))
                except:
                    st.error("Backend returned non-JSON response: " + resp.text)


if __name__ == "__main__":
    main()
