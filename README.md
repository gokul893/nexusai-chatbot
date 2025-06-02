
# NexusAI Chatbot (Streamlit + OpenAI)

This is a simple AI chatbot built with Streamlit and OpenAI's GPT-3.5 model.

## 💻 How to Run Locally

1. Clone or download this repo.
2. Add a `.env` file in the root with:

```
OPENAI_API_KEY=your_openai_key_here
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

## 🚀 Deploy Online (Streamlit Cloud)

1. Push this project to a GitHub repo.
2. Go to https://streamlit.io/cloud and click "New App".
3. Select your repo and set `app.py` as the main file.
4. Set your `OPENAI_API_KEY` in the "Secrets" section.

Done! Your chatbot is live! 🎉
