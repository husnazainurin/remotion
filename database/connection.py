import os
import streamlit as st

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@st.cache_resource
def get_engine():
    # Read database configurations in secrets.toml
    config = st.secrets['database']

    database_url = URL.create(
        drivername="mysql+pymysql",
        username=config["username"],
        password=config["password"],
        host=config["host"],
        port=int(config["port"]),
        database=config["database"]
    )

    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        pool_recycle=1800,
        pool_size=5,
        max_overflow=10
    )

    return engine


def get_session():
    engine = get_engine()

    Session = sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    return Session()
