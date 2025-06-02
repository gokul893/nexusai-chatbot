import streamlit as st
import google.generativeai as genai

# ✅ Load Gemini API Key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ Set up Streamlit app
st.set_page_config(page_title="NexusAI Chatbot", page_icon="🤖")
st.title("🤖 NexusAI - Gemini Chatbot")

# ✅ Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Display chat history
for role, content in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(content)

# ✅ Input box
user_input = st.chat_input("Say something to NexusAI...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    try:
        # ✅ Correct model call using GenerativeModel
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        bot_reply = response.text
        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.chat_history.append(("assistant", bot_reply))

    except Exception as e:
        st.error(f"❌ Gemini API error: {e}")
