# Sourdough Chatbot

A simple and minimalistic **AI chatbot** for sourdough baking. It is built with **Streamlit** that helps you bake better sourdough using the power of HF open-source **LLMs**.

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
- 🤖 Context-aware responses.
- 🌿 Custom prompt trained to behave like a sourdough expert.
- 🛠️ Fully open-source and easily extendable.

---

## 📁 Project Structure

#### sourdough_chat

├── app/

──├── app.py        # Streamlit UI

──├── chat.py       # Hugging Face API logic

──├── prompts.py    # Sourdough expert prompts

├── .env          

├── .gitignore 

├── README.md 

└── requirements.txt 

---

## 🔐 Environment Variables

Create a .env file with your Hugging Face API token. You can generate one at: https://huggingface.co/settings/tokens

HF_API_TOKEN = your_token

