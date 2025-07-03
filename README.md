# Sourdough Chatbot

A simple and minimalistic **AI chatbot** specialized in the field of sourdough bakes. It is built with **Streamlit** that helps you bake better sourdough using the power of Hugging face open-source **LLMs**.

> Ask questions like:
> - “I have 150g of discard. Give me a sweet recipe.”
> - “Why does my starter smell acidic?”
> - “What’s the best hydration level for ciabatta?”

## Demo:
<img src="https://github.com/user-attachments/assets/b6a0c8b0-e8f2-447a-8f14-dcca037cf285" alt="demo" width="500" height="600">

---

## 🚀 Features

- 🔥 Powered by [Hugging Face](https://huggingface.co/) models (Zephyr 7B)
- 💬 Real-time chat interface via [Streamlit](https://streamlit.io/).
- 🤖 Context-aware responses with memory (FAISS + embeddings)
- 🌿 Custom Jinja2 prompt templates for maintainable prompt logic

---

## 📁 Project Structure

#### sourdough_chat


├── prompts/

│   └── template.jinja       # Jinja2 template for system prompt

├── app/

│   ├── prompts.py           # Load and render Jinja2 templates

│   ├── chat.py              # Memory + LLM query logic

│   └── app.py               # Streamlit UI (chat interface)

├── .env                     # Environment variables (API tokens)

├── .gitignore

├── README.md

└── requirements.txt         # Dependencies
                    

---

## 🔐 Environment Variables

Create a .env file with your Hugging Face API token. You can generate one at: https://huggingface.co/settings/tokens

HF_API_TOKEN = your_token

