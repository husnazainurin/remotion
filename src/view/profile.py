import streamlit as st
# from database.patients import update_patient_referral_code
# from database.therapists import get_therapist_for_patient, get_therapist_by_referral_code

if "user" in st.session_state and st.session_state["user"] is not None:

    # Get user currently in the session state
    user = st.session_state["user"]

    # Welcoming message
    st.title(f"Hello, {user['username']}!")
    st.markdown(
                """
                Welcome to ReMOTION! 
                Are your ready to start your journey?
                """)
    st.divider()

    # <SECTION TO CHOOSE EXERCISE TYPE>
    st.subheader("Choose Rehabilitation Session:")
    left_col, right_col = st.columns(2, gap="large")

    # Hand strengthening
    with left_col:
        with st.container(border=True):
            st.image(
                "https://cdn.aarp.net/content/dam/aarpe/en/home/health/healthy-living/exercises-prevent-arthritis/_jcr_content/root/container_main/container_body_main/container_body3/container_body_cf/body_three_cf_one/par6/articlecontentfragme/cfimage.coreimg.50.932.jpeg/content/dam/aarp/health/conditions_treatments/2021/12/1140-finger-spread.jpg",
                use_container_width=True,
            )
            st.markdown("### Hand Strengthening")
            st.caption("Full-hand opening and closing movement to improve finger flexion and grip strength.")
            if st.button("Start Hand Strengthening", use_container_width=True):
                st.switch_page("view/hand-strengthening.py")

    # Hand opposition
    with right_col:
        with st.container(border=True):
            st.image(
                "https://www.aarp.org/content/dam/aarp/health/conditions_treatments/2021/12/1140-finger-touch.jpg",
                use_container_width=True,
            )
            st.markdown("### Hand Opposition")
            st.caption("Thumb-to fingertip touch sequence to restore fine motor coordination and dexterity.")
            if st.button("Start Hand Opposition", use_container_width=True):
                st.switch_page("view/hand-opposition.py")

    st.divider()
    # st.subheader("My Physiotherapist & Care Team")

    # therapist_col, privacy_col = st.columns([3, 2], gap="large")

    # with therapist_col:
    #     with st.container(border=True):
    #         therapist = get_therapist_for_patient(user["user_id"])

    #         if therapist:
    #             st.markdown(f"#### :material/medical_services: {therapist['therapist_name']}")
    #             st.markdown(f"**Referral Code:** `{therapist['referral_code']}`")
    #             st.success("Progress Synced: Your quantitative exercise scores and repetitions are shared with your physiotherapist.")
    #         else:
    #             st.markdown("#### :material/person_off: No Assigned Physiotherapist")
    #             st.caption("You are currently practicing in independent home-rehabilitation mode.")

    #             with st.form("link_therapist_form"):
    #                 new_code = st.text_input("Have a therapist referral code? Enter it here:", placeholder="e.g., PHY676767")
    #                 if st.form_submit_button("Link Physiotherapist", use_container_width=True):
    #                     matched = get_therapist_by_referral_code(new_code)
    #                     if matched:
    #                         update_patient_referral_code(user["user_id"], new_code)
    #                         st.session_state["user"]["referral_code"] = new_code.strip()
    #                         st.rerun()
    #                     else:
    #                         st.error("Invalid referral code. Please check with your physiotherapist.")
    # with privacy_col:
    #     with st.container(border=True):
    #         st.markdown("#### :material/shield_lock: Data & Privacy")
    #         st.caption(
    #             "Your webcam feed is processed locally in real time for hand-landmark tracking and is **not** stored as video. "
    #             "Only your quantitative exercise scores and repetition counts are saved for rehabilitation tracking."
    #         )
        

else:
    st.error("An error has occured. Please log in again :(")