import streamlit as st
from pathlib import Path
import sys

# Get project root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Add project root to Python module search path
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from database.users import get_user_by_username

home_page = st.Page("view/home.py", title="Home", icon=":material/home:", default=True)
logIn_page = st.Page("view/logIn.py", title="Login", icon=":material/login:")
faqs_page = st.Page("view/faqs.py", title="FaQs")
dashboard_page = st.Page("view/dashboard.py", title="Dashboard", icon=":material/dashboard:", visibility= "hidden")
profile_page = st.Page('view/profile.py', title = 'Profile', icon = ':material/person:', visibility='hidden')
signUp_page = st.Page("view/signUp.py", title="Sign Up", visibility= "hidden")

#navigation structure 
pg = st.navigation(
    [
        home_page,
        logIn_page,
        signUp_page,
        faqs_page,
        profile_page,
        dashboard_page
    ],
    position="top"
)

st.set_page_config(page_title="Remotion", page_icon=":raised_hand:", layout="wide")
pg.run()