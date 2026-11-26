import streamlit as st
import time

user = st.session_state.get("user")
is_logged_in = user is not None
is_therapist = is_logged_in and user.get("role_id") == 1

if is_logged_in:
    # Double confirm with user
    st.write('Are you sure you want to log out?')
    cancel_button = st.button('Cancel')
    confirm_button = st.button('Confirm')

    if confirm_button:
        # Remove user from current session
        st.session_state.pop("user", None)

        # Give feedback to user
        st.write('You have been successfully logged out and will be redirected to homepage...')
        time.sleep(2.5)

        st.switch_page('view/home.py')

    if cancel_button:
        if is_therapist:
            st.switch_page('view/dashboard.py')
        else:  
            st.switch_page('view/profile.py')

else:
    st.error('An error has occured :(')