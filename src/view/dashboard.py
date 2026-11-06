import streamlit as st
import pandas as pd
import numpy as np

st.title("Analytics Dashboard")

# Optional access control notice
if not st.session_state.get("logged_in", False):
    st.warning("⚠️ You are currently in preview mode. Log in from the Login page to unlock editing.")

# Dashboard Filters
col_filter1, col_filter2 = st.columns([2, 1])
with col_filter1:
    category = st.selectbox("Select Category", ["All Products", "Electronics", "Clothing", "Software"])
with col_filter2:
    time_frame = st.selectbox("Timeframe", ["7 Days", "30 Days", "90 Days"])

st.divider()

# Sample data generation
np.random.seed(42)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Sales", "Leads", "Conversions"]
)

# Visualizations Layout
st.subheader(f"Performance Metrics — {category} ({time_frame})")
st.line_chart(chart_data)

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Summary Table")
    st.dataframe(chart_data.describe(), use_container_width=True)

with col_right:
    st.subheader("Category Breakdown")
    st.bar_chart(chart_data.mean())