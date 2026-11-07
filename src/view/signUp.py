import streamlit as st
from sqlalchemy import text

st.set_page_config(
    page_title="Sign Up", layout="wide", page_icon=":raised_hand:"
)

# Connect and fetch user database
conn = st.connection("mysql", type="sql")

# Fetch existing usernames
df_users = conn.query("SELECT username FROM users;")
existing_users = df_users["username"].tolist()


st.title("Sign up")
with st.form("sign-up"):
    # Prompt username
    _username = st.text_input("Create a username")

    # Prompt password and repeat to confirm
    _password1 = st.text_input("Create a password", type="password")
    _password2 = st.text_input("Repeat your password", type="password")

    signup_button = st.form_submit_button("Sign Up")

if signup_button:
    errors = []

    # Required field checks (evaluating actual input variables)
    if not _username.strip():
        errors.append("Username is required.")
    if not _password1.strip():
        errors.append("Password is required.")

    # Check for duplicate username (case-insensitive check added)
    cleaned_username = _username.strip()
    existing_users_lower = [u.lower() for u in existing_users]

    if cleaned_username.lower() in existing_users_lower:
        errors.append("This username already exists.")

    # Password length check
    req_length = 12
    if len(_password1) < req_length:
        errors.append("Password requires at least 12 characters.")

    # Password repeat check
    if _password1 != _password2:
        errors.append("Passwords do not match.")

    # Display errors or register account
    if errors:
        for error in errors:
            st.error(error)
    else:
        # Register new account into database
        with conn.session as session:
            session.execute(
                text(
                    """
                    INSERT INTO users (username, password, role_id) 
                    VALUES (:username, :password, :role_id);
                """
                ),
                {
                    "username": cleaned_username,
                    "password": _password1,
                    "role_id": 2,
                },
            )
            session.commit()

        # Clear Streamlit's connection query cache so newly inserted user is fetched next time
        st.cache_data.clear()

        st.success("Account registered successfully.")