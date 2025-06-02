
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the Streamlit app
st.set_page_config(page_title="NexusAI Chatbot", page_icon="🤖")
st.title("🤖 NexusAI - Chat with AI")

# Initialize chat history with a system prompt for persistent memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are NexusAI, a helpful and friendly AI assistant. Remember the context of the conversation and respond accordingly."}
    ]

# Display previous chat messages (skip the system message)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input from user
prompt = st.chat_input("Say something to NexusAI...")

if prompt:
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message["content"]

    # Display assistant response
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
