import streamlit as st
import pyodbc

@st.cache_resource
def init_connection():
    conn_str = (
        f"DRIVER={st.secrets['azure_sql']['driver']};"
        f"SERVER={st.secrets['azure_sql']['server']};"
        f"DATABASE={st.secrets['azure_sql']['database']};"
        f"UID={st.secrets['azure_sql']['username']};"
        f"PWD={st.secrets['azure_sql']['password']};"
        "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )
    return pyodbc.connect(conn_str)
