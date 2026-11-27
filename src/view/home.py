import base64
from pathlib import Path

import streamlit as st


# ============================================================
# PATH CONFIGURATION
# ============================================================

# Keep this consistent with your existing project structure.
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Styling sheet for home
CSS_PATH = ROOT_DIR / "css" / "home_style.css"

# Image assets location
IMAGE_DIR = ROOT_DIR / "assets" / "images"


# ============================================================
# LOAD CSS
# ============================================================

def load_css(file_path: Path):
    """Load an external CSS file into Streamlit."""

    if file_path.exists():
        css_content = file_path.read_text(encoding="utf-8")

        st.markdown(
            f"<style>{css_content}</style>",
            unsafe_allow_html=True,
        )
    else:
        st.warning(f"CSS file not found: {file_path}")


load_css(CSS_PATH)


# ============================================================
# IMAGE HELPER
# ============================================================

def image_to_base64(image_path: Path):
    """
    Convert a local image into a base64 string.

    This allows local images to be displayed inside
    custom HTML components.
    """

    if not image_path.exists():
        return None

    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    extension = image_path.suffix.lower()

    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }

    mime_type = mime_types.get(extension, "image/jpeg")

    return f"data:{mime_type};base64,{encoded_image}"


def render_image(image_path: Path, alt_text: str = ""):
    """Return an HTML image tag if the image exists."""

    image_data = image_to_base64(image_path)

    if image_data:
        return f"""
            <img
                src="{image_data}"
                alt="{alt_text}"
                class="custom-image"
            >
        """

    return """
        <div class="image-placeholder">
            <span>IMAGE PLACEHOLDER</span>
        </div>
    """


# ============================================================
# BANNER SECTION
# ============================================================

banner_image = render_image(
    IMAGE_DIR / "mainpage_banner.png",
    "ReMOTION rehabilitation application preview",
)

st.html(
    f"""
    <section class="banner-section">

        <div class="banner-content">

            <div class="banner-eyebrow">
                YOUR JOURNEY BEGINS HERE
            </div>

            <h1 class="banner-title">
                Recovery,
                <br>
                <span class="gradient-text">reimagined.</span>
            </h1>

            <div class="banner-caption">
                <span>Because everyone deserves a second chance.</span>
            </div>

            <p class="banner-description">
                ReMOTION is an intelligent rehabilitation platform
                designed to support hand exercise assessment through
                markerless gesture recognition and movement analysis.
            </p>

            <div class="banner-buttons">

                <a href="#about" class="primary-button">
                    Discover ReMOTION
                    <span>↗</span>
                </a>

                <a href="#developers" class="secondary-button">
                    Meet the team
                </a>

            </div>


        </div>

        <div class="banner-visual">

            <div class="visual-glow"></div>

            <div class="banner-image-container">
                {banner_image}
            </div>

            <div class="floating-label label-top">
                <span class="label-icon">✦</span>
                <div>
                    <strong>Intelligent Assessment</strong>
                    <small>Movement analysis</small>
                </div>
            </div>

            <div class="floating-label label-bottom">
                <span class="label-icon peach-icon">↗</span>
                <div>
                    <strong>Progress, visualised</strong>
                    <small>Exercise monitoring</small>
                </div>
            </div>

            <div class="visual-number">
                <span>R</span>
            </div>

        </div>

    </section>
    """
)


# ============================================================
# INTRODUCTION SECTION
# ============================================================

st.html(
    """
    <section class="about-section reveal" id="about">

        <div class="section-label">
            <span class="section-number">01</span>
            <span>ABOUT THE PROJECT</span>
        </div>

        <div class="about-grid">

            <div class="about-heading">
                <h2>
                    Movement is more
                    <span class="gradient-text">than motion.</span>
                </h2>
            </div>

            <div class="about-content">

                <p class="about-lead">
                    A smarter approach to rehabilitation,
                    built around meaningful movement.
                </p>

                <p class="about-description">
                    [Insert your project introduction here.]

                    ReMOTION aims to make rehabilitation exercise
                    assessment more accessible through intelligent
                    movement tracking and automated feedback.

                    Replace this paragraph with your project's
                    objectives, motivation, and key contributions.
                </p>

                <div class="feature-list">

                    <div class="feature-item">
                        <span class="feature-index">01</span>
                        <span>Markerless hand tracking</span>
                        <span class="feature-arrow">↗</span>
                    </div>

                    <div class="feature-item">
                        <span class="feature-index">02</span>
                        <span>Intelligent movement assessment</span>
                        <span class="feature-arrow">↗</span>
                    </div>

                    <div class="feature-item">
                        <span class="feature-index">03</span>
                        <span>Progress monitoring</span>
                        <span class="feature-arrow">↗</span>
                    </div>

                </div>

            </div>

        </div>

    </section>
    """
)


# ============================================================
# DEVELOPERS SECTION
# ============================================================

st.html(
    """
    <section class="developers-section reveal" id="developers">

        <div class="section-label">
            <span class="section-number">02</span>
            <span>THE PEOPLE BEHIND REMOTION</span>
        </div>

        <div class="section-heading-row">

            <div>
                <h2 class="section-title">
                    Meet the <span class="gradient-text">team.</span>
                </h2>

                <p class="section-subtitle">
                    Two minds. One shared vision.
                </p>
            </div>

            <div class="team-count">
                <span>03</span>
                <small>DEVELOPERS</small>
            </div>

        </div>

    </section>
    """
)


# Developer information.
# Replace the names, roles, and images below.

developers = [
    {
        "name": "Nurul Husna binti Zainurin",
        "role": "Final Year Student, KICT, IIUM, Gombak",
        "image": "dev_husna.png",
        "number": "01",
    },
    {
        "name": "Norhanim Fatihah binti Ahmad",
        "role": "Final Year Student, KICT, IIUM, Gombak",
        "image": "image.png",
        "number": "02",
    },

    
]


dev_columns = st.columns(4, gap="large")
fill_column = [dev_columns[1], dev_columns[2]]

for column, developer in zip(fill_column, developers):
    with column:

        developer_image = render_image(
            IMAGE_DIR / developer["image"],
            developer["name"],
        )

        st.html(
            f"""
            <div class="developer-card reveal">

                <div class="developer-image-wrapper">
                    {developer_image}

                    <span class="developer-number">
                        {developer["number"]}
                    </span>
                </div>

                <div class="developer-information">

                    <div>
                        <h3>{developer["name"]}</h3>
                        <p>{developer["role"]}</p>
                    </div>

                    <span class="developer-arrow">↗</span>

                </div>

            </div>
            """,
        )


# ============================================================
# COLLABORATORS SECTION
# ============================================================

collaborator_image = render_image(
    IMAGE_DIR / "collaborators.png",
    "ReMOTION collaborators",
)

st.html(
    f"""
    <section class="collaborators-section reveal" id="collaborators">

        <div class="section-label">
            <span class="section-number">03</span>
            <span>OUR COLLABORATORS</span>
        </div>

        <div class="collaborator-container">

            <div class="collaborator-text">

                <h2>
                    Better together.
                </h2>

                <p>
                    [Insert information about your collaborators,
                    research partners, institutions, or supporting
                    organisations here.]
                </p>

                <div class="collaborator-caption">
                    COLLABORATION &nbsp; / &nbsp; RESEARCH &nbsp; / &nbsp; IMPACT
                </div>

            </div>

            <div class="collaborator-visual">
                {collaborator_image}
            </div>

        </div>

    </section>
    """,
)


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <footer class="home-footer">

        <div class="footer-brand">
            <span class="footer-symbol">R</span>
            <span>ReMOTION</span>
        </div>

        <p>
            Designed with purpose. Built for better movement.
        </p>

        <span class="footer-year">
            © ReMOTION
        </span>

    </footer>
    """
)
