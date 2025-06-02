import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Set up model (use full model name)
model = genai.GenerativeModel(model_name="models/gemini-pro")

# Streamlit setup
st.set_page_config(page_title="NexusAI Chatbot", page_icon="🤖")
st.title("🤖 NexusAI - Chat with AI")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# Get user input
prompt = st.chat_input("Say something to NexusAI...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append(("user", prompt))

    try:
        response = model.generate_content(prompt)
        reply = response.text
        st.chat_message("assistant").markdown(reply)
        st.session_state.chat_history.append(("assistant", reply))
    except Exception as e:
        st.error(f"Gemini API error: {e}")
