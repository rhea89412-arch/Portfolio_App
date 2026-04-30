import streamlit as st

# Page setup
st.set_page_config(page_title="My Portfolio", page_icon="🦋", layout="wide")

# 🎨 CSS Design
st.markdown("""
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
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
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">📩 Contact Me</p>', unsafe_allow_html=True)

st.markdown("---")

# Form Card
st.markdown('<div class="card">', unsafe_allow_html=True)

name = st.text_input("👤 Name")
email = st.text_input("📧 Email")
message = st.text_area("💬 Message")

if st.button("Send 🚀"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Message:**", message)
    else:
        st.error("Please fill all fields ❌")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Social Links
st.subheader("🌐 Social Links")
st.write("🔗 GitHub: https://github.com/")
st.write("🔗 Facebook: https://facebook.com/")

st.success("✨ Thank you for visiting my portfolio!")