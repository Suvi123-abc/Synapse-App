import streamlit as st
import os
from groq import Groq


# =========================
# GROQ AI FUNCTION
# =========================
def ask_groq(prompt):
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "Groq API key not set."

        client = Groq(api_key=api_key)
        message = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
        )
        return message.choices[0].message.content

    except Exception as e:
        return f"AI service is currently unavailable: {str(e)}"


# =========================
# AI CHAT SECTION
# =========================
st.title("💬 Educational Assistant")
st.write("Ask any study-related questions and get AI-powered help!")

# Initialize chat history if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_question = st.chat_input("Ask a study question...")
if user_question:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_question}
    )

    ai_reply = ask_groq(user_question)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": ai_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(ai_reply)

# Clear chat button
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()


# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.markdown("## 📚 SYNAPSE")
st.sidebar.markdown("Smart Student Dashboard")

