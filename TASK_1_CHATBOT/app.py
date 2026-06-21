import streamlit as st
import time
from chatbot import get_response

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Sidebar

with st.sidebar:
    st.title("🤖 AI Assistant")
    st.write("Rule-Based Chatbot")
    st.write("Built using Python + Streamlit")
    st.write("CodSoft Internship Project")

st.title("🤖 AI Career Assistant")
st.write("Ask me about AI, Machine Learning, Python, Programming and Careers.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages

for msg in st.session_state.messages:

    avatar = "🤖" if msg["role"] == "assistant" else "🧑"

    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# Chat Input

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )

    with st.spinner("Thinking..."):
        time.sleep(1)

    response = get_response(user_input)

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )

    st.rerun()