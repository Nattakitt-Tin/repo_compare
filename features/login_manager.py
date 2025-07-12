from datetime import datetime, timedelta
import json
import os
import streamlit as st
import pyrebase

SESSION_DURATION_MINUTES = 30


def _init_firebase():
    """Load Firebase config and initialize the app."""
    if "firebase_app" in st.session_state:
        return st.session_state.firebase_app

    cfg_path = os.getenv("FIREBASE_CONFIG", "firebase_config.json")
    try:
        with open(cfg_path, "r") as f:
            config = json.load(f)

        required = [
            "apiKey",
            "authDomain",
            "databaseURL",
            "projectId",
            "storageBucket",
            "messagingSenderId",
            "appId",
        ]
        missing = [k for k in required if k not in config]
        if missing:
            raise KeyError(
                "Missing keys in firebase_config.json: " + ", ".join(missing)
            )

        firebase = pyrebase.initialize_app(config)
    except FileNotFoundError:
        st.error(
            f"Firebase config not found at '{cfg_path}'. Create it from firebase_config_template.json"
        )
        firebase = None
    except Exception as e:
        st.error(f"Failed to initialize Firebase: {e}")
        firebase = None
    st.session_state.firebase_app = firebase
    return firebase


def _get_auth():
    app = _init_firebase()
    return app.auth() if app else None


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
            auth = _get_auth()
            if not auth:
                return
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.logged_in = True
                st.session_state.login_time = datetime.now()
                st.session_state.user = user
                st.success("Logged in successfully")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")
        else:
            st.error("Please provide both email and password")


def require_login() -> bool:
    """Ensure the user is logged in before accessing a page."""
    if not is_logged_in():
        st.error("Session expired or not logged in. Please login from Home page.")
        return False
    return True
