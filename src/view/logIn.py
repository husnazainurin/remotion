import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.header('Your journey begin here.')

with col2:

    st.header('ReMOTION')
    _username = st.text_input('Username')
    _password = st.text_input('Password')

    st.button('SIGN UP')

