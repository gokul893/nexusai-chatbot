import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Create OpenAI client (it automatically uses OPENAI_API_KEY env var)
client = OpenAI()

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

# Take user input
prompt = st.chat_input("Say something to NexusAI...")

if prompt:
    # Show user message in chat
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI chat completion API with full conversation history
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    # Get assistant reply
    reply = response.choices[0].message.content

    # Show assistant reply in chat
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
