import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    st.error("Set GROQ_API_KEY in a .env file or as an env var.")
    st.stop()

client = Groq(api_key=API_KEY)

st.set_page_config(page_title="Tiny AI Q&A", page_icon="✨", layout="centered")
st.title("✨ Tiny AI Q&A")

with st.sidebar:
    st.subheader("Settings")
    model = st.selectbox(
        "Model",
        options=[
            "llama-3.1-8b-instant",        # fast/cheap
            "llama-3.3-70b-versatile",     # big/detailed (newer 70B)
            "llama-3.2-11b-preview",       # optional preview
            "llama-3.2-90b-preview",       # optional preview
        ],
        index=0
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1)
    concise = st.toggle("Concise mode (<=120 words)", value=True)

# session chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

SYSTEM_PROMPT = "Be helpful and concise." if concise else "Be helpful and thorough."

# chat UI
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

user_q = st.chat_input("Ask anything...")
if user_q:
    st.session_state.messages.append({"role": "user", "content": user_q})
    with st.chat_message("user"):
        st.markdown(user_q)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *st.session_state.messages  # send the running chat
                    ],
                    temperature=temperature,
                )
                answer = resp.choices[0].message.content.strip()
            except Exception as e:
                answer = f"❌ API error: {e}"
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

col1, col2 = st.columns(2)
with col1:
    if st.button("🧹 Clear chat"):
        st.session_state.messages = []
        st.rerun()
with col2:
    st.caption(f"Model: `{model}` • Temp: {temperature}")

