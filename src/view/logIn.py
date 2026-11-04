import streamlit as st

st.title("User Login")

# Initialize session state for user login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Show status if already logged in
if st.session_state["logged_in"]:
    st.success(f"Welcome back, **{st.session_state['username']}**!")
    
    if st.button("Log Out"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.rerun()

else:
    # Login Form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Log In", use_container_width=True)

        if submit:
            # Replace with real database validation logic
            if username.strip() != "" and password == "12345":
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("Log in successful!")
                st.rerun()
            else:
                st.error("Invalid username or password (try password: `12345`).")