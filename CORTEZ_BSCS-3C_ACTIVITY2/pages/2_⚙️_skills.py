import streamlit as st

# Page setup
st.set_page_config(page_title="My Portfolio", page_icon="🦋", layout="wide")

# 🎨 CSS Design
st.markdown("""
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(to right, #a1c4fd, #c2e9fb);
    }

    /* Title */
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
    }

    /* Card Style */
    .card {
        background-color: blue;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🦋 My Skills</p>', unsafe_allow_html=True)

st.markdown("---")

# Layout
col1, col2 = st.columns(2)

# 💻 Technical Skills
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💻 Technical Skills")

    st.write("HTML")
    st.progress(80)

    st.write("CSS")
    st.progress(75)

    st.write("JavaScript")
    st.progress(60)

    st.write("Python")
    st.progress(70)

    st.markdown("</div>", unsafe_allow_html=True)

# 🎨 Other Skills
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🎨 Other Skills")

    st.write("Creativity")
    st.progress(85)

    st.write("Communication")
    st.progress(80)

    st.write("Problem Solving")
    st.progress(75)

    st.write("Teamwork")
    st.progress(90)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Footer
st.success("✨ Always learning new skills and improving every day!")