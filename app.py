import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("ERROR: GEMINI_API_KEY not found. Please add it to your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI setup
st.set_page_config(page_title="NexusAI Chatbot", page_icon="🤖")
st.title("🤖 NexusAI - Chat with AI")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# Input prompt
prompt = st.chat_input("Say something to NexusAI...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append(("user", prompt))

    try:
        response = model.generate_content(
            st.session_state.chat_history
        )
        reply = response.text

        # Show assistant reply
        st.chat_message("assistant").markdown(reply)
        st.session_state.chat_history.append(("assistant", reply))

    except Exception as e:
        st.error(f"Gemini API error: {e}")
