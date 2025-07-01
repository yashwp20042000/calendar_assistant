# Streamlit UI Application
import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/chat"  # Replace after deployment

st.title("Google Calendar AI Assistant 🤖")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")

    res = requests.post(BACKEND_URL, json={"message": user_input})
    reply = res.json().get("reply", "No reply")

    st.session_state.chat_history.append(f"AI: {reply}")

for msg in st.session_state.chat_history:
    st.write(msg)
