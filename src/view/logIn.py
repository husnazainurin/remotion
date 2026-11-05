import streamlit as st

st.set_page_config(page_title='Log In', layout='wide')

st.html(
    """
    <style>

        /* 1. Completely hide Streamlit's top UI */
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
        }

        /* 2. Remove the reserved top spacing */
        [data-testid="stMainBlockContainer"] {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            margin-top: 0 !important;
        }

        .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            height: 100vh !important;
        }

        /* 3. Lock the app to viewport height */
        html, body, 
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            height: 100vh !important;
            max-height: 100vh !important;
            overflow: hidden !important;
        }

        /* 4. Make columns fill the entire viewport */
        [data-testid="stHorizontalBlock"] {
            height: 100vh !important;
            gap: 0 !important;
        }

        [data-testid="stColumn"] {
            height: 100vh !important;
            padding: 3rem !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: center !important;
        }

        /* 5. Column 1 styling */
        [data-testid="stColumn"]:nth-child(1) {
            background-color: #111111;
            color: #ffffff;
        }

        /* 6. Button styling */
        [data-testid="stButton"] > button {
            background-color: #ffc694;
            color: #000000;
            border: none;
        }

        /* Remove all horizontal page margins and padding */
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        .main,
        .main .block-container {
            padding-left: 0 !important;
            padding-right: 0 !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            max-width: 100% !important;
            width: 100% !important;
        }

        /* Ensure columns stretch across the full width */
        [data-testid="stHorizontalBlock"] {
            width: 100% !important;
            gap: 0 !important;
            margin: 0 !important;
        }

        /* Remove default column margins */
        [data-testid="stColumn"] {
            margin: 0 !important;
        }

    </style>
    """
)

col1, col2 = st.columns(2)

with col1:
    st.header('Your journey begins here.')

with col2:
    st.header('ReMOTION')
    _username = st.text_input('Username')
    _password = st.text_input('Password', type='password')
    st.button('SIGN UP', use_container_width=True)
    st.write('Already have an account? Log in instead.')