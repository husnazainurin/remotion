import streamlit as st
from pathlib import Path

from database.users import get_user_by_username


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Log In | ReMOTION",
    page_icon="🤚",
    layout="wide",
)


# ============================================================
# LOAD CSS
# ============================================================

def load_css(file_name):
    """Load an external CSS stylesheet."""

    css_path = (
        Path(__file__).resolve().parent.parent.parent
        / "css"
        / file_name
    )

    if css_path.exists():
        css_content = css_path.read_text(encoding="utf-8")

        st.html(f"<style>{css_content}</style>")

load_css("logIn.css")


# ============================================================
# LOGIN LAYOUT
# ============================================================

left_space, login_column, right_space = st.columns(
    [1, 1.15, 1]
)


with login_column:

    # Welcome heading
    st.html(
        """
        <div class="login-heading">

            <h1>
                <span class="gradient-text">ReMOTION</span>
            </h1>

            <div class="login-eyebrow">
                WELCOME BACK
            </div>

        </div>
        """
    )

    # Box wrapping both the form and the sign-up section
    with st.container(key = 'form', border=True):

        # Login form
        with st.form("login_form", border=False):

            username = st.text_input(
                "Username",
                placeholder="Enter your username",
            )

            password = st.text_input(
                "Password",
                placeholder="Enter your password",
                type="password",
            )

            login_button = st.form_submit_button(
                "Log in",
                use_container_width=True,
            )


        # Sign-up link
        st.html(
            """
            <div class="signup-caption">
                Don't have an account yet?
            </div>
            """
        )

        signup_button = st.button(
            "Create an account",
            use_container_width=True
        )


# ============================================================
# LOGIN VALIDATION
# ============================================================

if login_button:

    errors = []

    # Check required fields
    if not username.strip() or not password:
        errors.append(
            "Please enter your username and password."
        )

    else:

        # Retrieve account
        user = get_user_by_username(username.strip())

        # Username validation
        if not user:
            errors.append(
                "No account found with that username."
            )

        # Password validation
        else:
            if password != user["passkey"]:
                errors.append(
                    "Incorrect password. Please try again."
                )

    # Display errors
    if errors:

        for error in errors:
            st.error(error)

    # Successful login
    else:

        st.session_state["user"] = user

        st.cache_data.clear()

        # Administrator
        if user["role_id"] == 1:

            st.switch_page("view/dashboard.py")

        # Patient
        else:

            st.switch_page("view/profile.py")


# ============================================================
# SIGN-UP REDIRECTION
# ============================================================

if signup_button:

    st.switch_page("view/signUp.py")