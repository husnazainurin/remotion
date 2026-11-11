import streamlit as st
from pathlib import Path
from database.users import get_user_by_username

st.set_page_config(page_title='Log In', layout='wide', page_icon=":raised_hand:")


def load_css(file_name):
    '''Load styling CSS sheet for log in page'''
    css_path = Path(__file__).parent.parent.parent / "css" / file_name
    if css_path.exists():
        with open(css_path, "r") as f:
            st.html(f"<style>{f.read()}</style>")

# Load CSS stylesheet
load_css("logIn.css")

# Define page column
col1, col2 = st.columns(2)

# Branding decoration
with col1:
    st.header('Your journey begins here.')

# Form
with col2:
    with st.form('login'):
        st.header('ReMOTION')

        _username = st.text_input('Username')
        _password = st.text_input('Password', type='password')

        login_button = st.form_submit_button('LOG IN', use_container_width=True)
    signup_button = st.button("Don't have an account? Sign up instead.")


# Credentials check
if login_button:
    errors = []

    # Check for missing input fields
    if not _username.strip() or not _password.strip():
        errors.append("Please enter all required fields.")

    # All fields are filled
    else:

        # Fetch account in database
        user = get_user_by_username(_username)

        # Check if username exists
        if not user:
            errors.append(f"No existing account found with username '{_username.strip()}'.")

        # Check password only if username exists
        else:
            if _password.strip() != user['password']:
                errors.append("Incorrect password.")

    # Show result
    with col2:
        if errors:
            for error in errors:
                st.error(error)
        else:
            # User is an admin
            if user['role_id'] == 1:
                st.switch_page('view/dashboard.py')

            # User is a patient
            else:
                st.switch_page('view/profile.py')
            st.cache_data.clear()

# Redirect to sign up form
if signup_button:
    st.switch_page("view/signUp.py")
