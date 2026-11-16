import streamlit as st

if "user" in st.session_state and st.session_state["user"] is not None:
    user = st.session_state["user"]
    st.title(f"Hello, {user['username']}!")
    st.markdown(
                """
                Welcome to ReMOTION! 
                Are your ready to start yout journey?
                """)
    
    left_col, right_col = st.columns(2, gap="large")

    with left_col:
        with st.container(border=True):
            st.image(
                "https://cdn.aarp.net/content/dam/aarpe/en/home/health/healthy-living/exercises-prevent-arthritis/_jcr_content/root/container_main/container_body_main/container_body3/container_body_cf/body_three_cf_one/par6/articlecontentfragme/cfimage.coreimg.50.932.jpeg/content/dam/aarp/health/conditions_treatments/2021/12/1140-finger-spread.jpg",
                use_container_width=True,
            )
            st.subheader("Hand Strengthening")
            if st.button("Start Hand Strengthening", use_container_width=True):
                st.switch_page("view/hand-strengthening.py")

    with right_col:
        with st.container(border=True):
            st.image(
                "https://www.aarp.org/content/dam/aarp/health/conditions_treatments/2021/12/1140-finger-touch.jpg",
                use_container_width=True,
            )
            st.subheader("Hand Opposition")
            if st.button("Start Hand Opposition", use_container_width=True):
                st.switch_page("view/hand-opposition.py")

else:
    st.error("No user found in session_state.")
    st.write("Current session_state:", st.session_state)