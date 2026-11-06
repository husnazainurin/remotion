import streamlit as st

home_page = st.Page("view/home.py", title="Home", icon=":material/home:", default=True)
logIn_page = st.Page("view/logIn.py", title="Login", icon=":material/login:")
faqs_page = st.Page("view/faqs.py", title="FaQs")
dashboard_page = st.Page("view/dashboard.py", title="Dashboard", icon=":material/dashboard:")

#navigation structure 
pg = st.navigation(
    [
        home_page,
        logIn_page,
        faqs_page,
        dashboard_page
    ],
    position="top"
)

st.set_page_config(page_title="Remotion", page_icon=":raised_hand:", layout="wide")
pg.run()