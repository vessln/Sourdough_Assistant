import streamlit as st
from chat import build_and_query

# Streamlit configuration
st.set_page_config(page_title="Sourdough Chatbot", layout="centered")
st.title("🥖 Sourdough Chatbot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if user_input := st.chat_input("Ask me anything about sourdough..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Query LLM using new logic with memory and Jinja templates
    with st.chat_message("assistant"):
        response = build_and_query(st.session_state.messages)
        st.markdown(response)

    # Append assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
