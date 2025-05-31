
import streamlit as st

st.set_page_config(page_title="Qorvex AI", layout="wide")

st.title("🚀 Qorvex AI Risk Monitor")
st.markdown("Monitor prompt injection, plugin abuse, and risky inputs.")

# Test input field
user_prompt = st.text_input("🔍 Enter a user prompt to analyze:")

# Simple pattern-based detector
blacklist = ["ignore", "you are now", "act as", "jailbreak", "simulate", "###", "system prompt"]
if user_prompt:
    if any(term in user_prompt.lower() for term in blacklist):
        st.error("⚠️ Prompt Injection Detected!")
    else:
        st.success("✅ Prompt is clean.")
