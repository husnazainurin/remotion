import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Log In', layout='wide')


def load_css(file_name):
    css_path = Path(__file__).parent.parent.parent / "assets" / file_name
    with open(css_path, "r") as f:
        st.html(f"<style>{f.read()}</style>")


load_css("logIn.css")


col1, col2 = st.columns(2)

with col1:
    st.header('Your journey begins here.')

with col2:
    st.header('ReMOTION')
    _username = st.text_input('Username')
    _password = st.text_input('Password', type='password')
    st.button('LOG IN', use_container_width=True)
    st.write('Don\'t have an account? Sign up instead.')