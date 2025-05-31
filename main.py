
import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Qorvex AI – Web Preview", layout="wide")

# Title or description
st.title("🌐 Qorvex AI Web App Preview")
st.markdown("This is a live preview of your HTML landing page rendered inside Streamlit.")

# Load HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display HTML using iframe-style embedding
components.html(html_code, height=800, scrolling=True)
