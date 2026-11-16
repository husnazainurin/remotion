import streamlit as st
from pathlib import Path
import sys

st.set_page_config(page_title="ReMOTION", page_icon=":raised_hand:", layout="wide")


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

user = st.session_state.get("user")
is_logged_in = user is not None
is_admin = is_logged_in and user.get("role_id") == 1


home_page = st.Page("view/home.py", title="Home", icon=":material/home:", default=True)
logIn_page = st.Page(
    "view/logIn.py",
    title="Login",
    icon=":material/login:",
    visibility="hidden" if is_logged_in else "visible",
)
signUp_page = st.Page("view/signUp.py", title="Sign Up", visibility="hidden")
faqs_page = st.Page("view/faqs.py", title="FAQs", icon=":material/help:")
dashboard_page = st.Page(
    "view/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
    visibility="visible" if is_admin else "hidden",
)
profile_page = st.Page(
    "view/profile.py",
    title="Profile",
    icon=":material/person:",
    visibility="visible" if (is_logged_in and not is_admin) else "hidden",
)
hand_strengthening_page = st.Page(
    "view/hand-strengthening.py",
    title="Hand Strengthening",
    visibility="hidden",
)
hand_oppostion_page = st.Page(
    "view/hand-oppostion.py:",
    title="Hand Opposition",
    visibility="hiddden", 
)

pg = st.navigation(
    [
        home_page,
        logIn_page,
        signUp_page,
        profile_page,
        dashboard_page,
        hand_strengthening_page,
        faqs_page,
    ],
    position="top",
)

pg.run()