import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------
# AUTH FUNCTIONS
# ---------------------------
def login(username, password):
    return requests.post(
        f"{API_URL}/auth/login",
        json={"username": username, "password": password},
        timeout=15
    )


def register(username, password):
    return requests.post(
        f"{API_URL}/auth/register",
        json={"username": username, "password": password},
        timeout=5
    )



# ---------------------------
# MAIN APP
# ---------------------------
def main():
    st.set_page_config(
        page_title="Premier League Analyst",
        page_icon="⚽",
        layout="wide"
    )

    st.title("⚽ Premier League Analyst")

    # Session init
    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    # ---------------------------
    # LOGGED IN VIEW
    # ---------------------------
    if st.session_state.user_id is not None:
        st.sidebar.title("📂 Navigation")

        page = st.sidebar.radio(
            "Go to",
            ["Home", "Standings", "Teams", "Matches", "Top Players", "Logout"],
            key="main_navigation"
        )

        if page == "Home":
            st.subheader("🏠 Home")
            st.write("Welcome to your Premier League analysis dashboard.")
            st.info("Choose a section from the sidebar.")

        elif page == "Standings":
            from pages.standings import main as standings_page
            standings_page()

        elif page == "Teams":
            from pages.teams import main as teams_page
            teams_page()

        elif page == "Matches":
            from pages.matches import main as matches_page
            matches_page()

        elif page == "Top Players":
            from pages.players import main as players_page
            players_page()

        elif page == "Logout":
            st.session_state.user_id = None
            st.success("Logged out successfully.")
            st.rerun()

        return

    # ---------------------------
    # LOGIN / REGISTER VIEW
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
                except Exception:
                    st.error("Backend error: " + resp.text)

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
                except Exception:
                    st.error("Backend error: " + resp.text)


if __name__ == "__main__":
    main()
