import streamlit as st

home_page = st.Page("view/home.py", title="Home", icon=":material/home:", default=True)
logIn_page = st.Page("view/logIn.py", title="Login", icon=":material/login:")
faqs_page = st.Page("view/faqs.py", title="FaQs")
dashboard_page = st.Page("view/dashboard.py", title="Dashboard", icon=":material/dashboard:")

#navigation structure 
pg = st.navigation(
    {
    "Home :material/home:": [home_page,logIn_page],
    "FaQs": [faqs_page],
    "Dashboard :material/dashboard:": [dashboard_page]
    },
    position= "top"
)

st.set_page_config(page_title="Remotion", page_icon=":guardsman:", layout="wide")
pg.run()