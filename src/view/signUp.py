import streamlit as st

st.title('Sign up')

with st.form('sign-up'):
    # Prompt username
    _username = st.text_input('Create a username')

    # Prompt password and repeat to confirm
    _password1 = st.text_input('Create a password', type = 'password')
    _password2 = st.text_input('Repeat your password', type = 'password')


    signup_button = st.form_submit_button('Sign Up')

if signup_button:
    errors= []

    # Required field check
    required = ['_username', '_password1', '_password2']
    required_name = ['Username, Password', 'Password']
    for i, field in enumerate(required):
        if not field.strip():
            errors.append(f'{required_name[i]} is required.')

    # Password length check
    req_length = 12
    if len(_password1) < req_length:
       errors.append('Password require at least 12 characters.')

    # Password repeat check
    if(_password1 != _password2):
        errors.append('Password do not match.')

    # Check for error. If no error, register account
    if errors:
        for error in errors:
            st.error(error)
    else:
        st.success('Account registered successfully.')