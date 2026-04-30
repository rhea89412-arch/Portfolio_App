import streamlit as st

# Page setup
st.set_page_config(page_title="My Portfolio", page_icon="🦋", layout="wide")

# 🎨 Custom CSS Design
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(to right, #c2e9fb, #a1c4fd);
    }

    /* Title */
    .main-title {
        font-size: 50px;
        font-weight: bold;
        color: #2c3e50;
    }

    /* Subtitle */
    .subtitle {
        font-size: 20px;
        color: #34495e;
    }

    /* Cards *
    .card {
        padding: 20px;
        border-radius: 20px;
        background-color: blue;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        transition: 0.3s;
    }

    .card:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 🏠 Header Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<p class="main-title">Hi, I am a Future Developer 👩‍💻</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Welcome to my portfolio 💻🌈</p>', unsafe_allow_html=True)
    st.write("I love designing and building simple, beautiful applications.")

with col2:
    st.image("CORTEZ_BSCS-3C_ACTIVITY2/pages/Cortez_Picture1.jpg", caption="My Profile")

st.markdown("---")

# 🎯 Cards Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">💡<h3>Skills</h3><p>My abilities and tools.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">📂<h3>Projects</h3><p>Things I created.</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">📞<h3>Contact</h3><p>Reach me بسهولة.</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("### ✨ Thank you for visiting!")
