import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Log In', layout='wide', page_icon=":raised_hand:")

# Fetch database connection and users
conn = st.connection('mysql', type='sql')

# Query the user table
users = conn.query('SELECT * FROM users;')
usernames = users['username'].tolist()

def load_css(file_name):
    css_path = Path(__file__).parent.parent.parent / "css" / file_name
    if css_path.exists():
        with open(css_path, "r") as f:
            st.html(f"<style>{f.read()}</style>")

load_css("logIn.css")

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
        st.write("Don't have an account? Sign up instead.")


# Credentials check
if login_button:
    errors = []

    # Check for missing input fields
    if not _username.strip() or not _password.strip():
        errors.append("Please enter all required fields.")

    # Check if username exists
    elif _username.strip() not in usernames:
        errors.append(f"No existing account found with username '{_username.strip()}'.")

    # Check password only if username exists
    else:
        # Get the matching user row safely
        # user_row = users[users['username'] == _username.strip()]
        # stored_password = user_row['password'].values[0]

        if _password.strip() != users[users['username'] == _username.strip()]['password'].iloc[0]:
            errors.append("Incorrect password.")

    # Show result
    with col2:
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success('Logged in successfully.')
            st.cache_data.clear()