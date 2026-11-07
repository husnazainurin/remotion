import streamlit as st

from pathlib import Path
import streamlit as st

# --- LOAD EXTERNAL CSS FILE ---
def load_css(file_name):
    # Path locates assets/style.css relative to the project root
    css_path = Path(__file__).parent.parent.parent / "css" / file_name
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply external styles
load_css("home_style.css")



# --- TITLE SECTION ---
st.markdown(
            """
            <div class="title-section">
                <img src="https://images.alphacoders.com/141/thumb-1920-1411319.png" alt="ReMotion">
                <div class="title-overlay"></div>
                <div class="title-text">ReMOTION</div> 
                
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
            """
            <div class="desc-banner">
                AN AUTOMATED ASSESSMENT SYSTEM THAT UTILIZES MARKERLESS HAND-GESTURE RECOGNITION TO TRACK HAND
                STRENGTHENING AND OPPOSITION EXERCISES. AN AUTOMATED ASSESSMENT SYSTEM THAT UTILIZES MARKERLESS HAND-GESTURE
                RECOGNITION TO TRACK HAND STRENGTHENING AND OPPOSITION EXERCISES.
            </div>
            """,
            unsafe_allow_html=True,
        )


# --- BOTTOM SECTION: DEVELOPERS & COLLABORATORS ---
left_col, right_col = st.columns([1.2, 1])

# Left Side: Developers Grid
with left_col:
    st.markdown('<div class="section-header">DEVELOPERS:</div>', unsafe_allow_html=True)
    dev1, dev2, dev3 = st.columns(3)

    with dev1:
        st.markdown(
            """
            <div class="dev-card">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300" alt="Aminah">
                <div class="dev-name">AMINAH BT ABU</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with dev2:
        st.markdown(
            """
            <div class="dev-card">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300" alt="Aminah">
                <div class="dev-name">AMINAH BT ABU</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with dev3:
        st.markdown(
            """
            <div class="dev-card">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300" alt="Aminah">
                <div class="dev-name">AMINAH BT ABU</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Right Side: Collaborators Placeholder Box
with right_col:
    st.markdown('<div class="section-header">COLLABORATORS:</div>', unsafe_allow_html=True)
    st.markdown('<div class="collab-card"></div>', unsafe_allow_html=True)   