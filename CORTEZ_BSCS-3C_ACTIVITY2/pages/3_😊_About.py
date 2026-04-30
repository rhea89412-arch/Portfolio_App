import streamlit as st

# Page setup
st.set_page_config(page_title="My Portfolio", page_icon="🦋", layout="wide")

# 🎨 Custom CSS Design
st.markdown("""
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
    }

    /* Main Title */
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }

    /* Card Style */
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🦋 About Me</p>', unsafe_allow_html=True)

st.markdown("---")

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.image("CORTEZ_BSCS-3C_ACTIVITY2/pages/Cortez_Picture2.jpg", caption="My Profile")

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👩‍💻 Hello!")
    st.write("Hi! I'm a student who wants to learn coding and build simple systems using Python and web development.")

    st.write("💡 My Interests:")
    st.write("- 💻 Web Development")
    st.write("- 🎨 UI/UX Design")
    st.write("- 🐍 Python Programming")

    st.info("🌱 I am continuously learning and improving my skills!")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Goal Section
st.subheader("🎯 My Goal")
st.success("To become a skilled developer and create amazing applications 🚀")

# Contact Section
st.markdown("---")
st.subheader("📞 Contact Me")
st.write("📧 Email: your@email.com")
st.write("📱 Facebook: your profile link")
