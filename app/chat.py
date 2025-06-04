import os
import httpx
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT


load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def build_prompt(messages: list) -> str:
    prompt = SYSTEM_PROMPT + "\n\n"
    for message in messages:
        role = "User" if message["role"] == "user" else "Assistant"
        prompt += f"{role}: {message['content']}\n"
    prompt += "Assistant:"
    return prompt


def query_llm(messages: list) -> str:
    prompt = build_prompt(messages)
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
            "top_p": 0.9,
            "return_full_text": False
        }
    }
    try:
        response = httpx.post(MODEL_URL, headers=HEADERS, json=payload, timeout=40.0)
        response.raise_for_status()
        generated_text = response.json()[0]["generated_text"]
        return generated_text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"
