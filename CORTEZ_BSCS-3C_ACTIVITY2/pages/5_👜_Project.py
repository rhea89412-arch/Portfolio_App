import streamlit as st

# Page setup
st.set_page_config(page_title="My Portfolio", page_icon="🦋", layout="wide")

# 🎨 CSS DESIGN
st.markdown("""
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(to right, #ffecd2, #fcb69f);
    }

    /* Title */
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
    }

    /* Card */
    .card {
        background-color: blue;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🦋 My Projects</p>', unsafe_allow_html=True)

st.markdown("---")

# PROJECT 1
col1, col2 = st.columns([1, 2])

with col1:
    st.image("CORTEZ_BSCS-3C_ACTIVITY2/pages/Cortez_Picture3.jpegg")

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📘 Slambook Project")
    st.write("A fun interactive slambook using HTML, CSS, and JavaScript.")

    if st.button("View Project 1", key="p1"):
        st.success("Opening Project 1 🚀")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# PROJECT 2
col1, col2 = st.columns([1, 2])

with col1:
    st.image("CORTEZ_BSCS-3C_ACTIVITY2/pages/Cortez_Picture1.jpg")

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🌍 Tourist Website")
    st.write("A website showcasing tourist spots in the Philippines.")

    if st.button("View Project 2", key="p2"):
        st.success("Opening Project 2 🚀")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# PROJECT 3
col1, col2 = st.columns([1, 2])

with col1:
    st.image("CORTEZ_BSCS-3C_ACTIVITY2/pages/Cortez_Picture2.jpg")

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🎬 Movie Platform")
    st.write("A movie platform with playback and download simulation.")

    if st.button("View Project 3", key="p3"):
        st.success("Opening Project 3 🚀")

    st.markdown("</div>", unsafe_allow_html=True)
