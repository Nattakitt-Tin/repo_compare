from datetime import datetime, timedelta
import streamlit as st

SESSION_DURATION_MINUTES = 30


def is_logged_in() -> bool:
    """Check login state and session timeout."""
    logged_in = st.session_state.get("logged_in", False)
    login_time = st.session_state.get("login_time")
    if not logged_in or not login_time:
        return False
    if datetime.now() - login_time > timedelta(minutes=SESSION_DURATION_MINUTES):
        st.session_state.logged_in = False
        return False
    return True


def login_form():
    """Render login form and handle submission."""
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email and password:
            st.session_state.logged_in = True
            st.session_state.login_time = datetime.now()
            st.success("Logged in successfully")
            st.experimental_rerun()
        else:
            st.error("Please provide both email and password")


def require_login() -> bool:
    """Ensure the user is logged in before accessing a page."""
    if not is_logged_in():
        st.error("Session expired or not logged in. Please login from Home page.")
        return False
    return True
