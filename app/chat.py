import os
import httpx
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss
from prompts import render_prompt

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_URL = os.getenv(
    "MODEL_URL",
    "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
)
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# Initialize memory encoder and FAISS index
encoder = SentenceTransformer('all-MiniLM-L6-v2')
dim = encoder.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(dim)
memory_texts = []


def add_to_memory(text: str):
    emb = encoder.encode(text)
    index.add(np.array([emb]).astype('float32'))
    memory_texts.append(text)


def get_relevant_history(num_results: int = 5) -> str:
    if index.ntotal == 0:
        return ''
    # Use the last added embedding as query
    query_emb = index.reconstruct(index.ntotal - 1)
    _, ids = index.search(np.array([query_emb]).astype('float32'), num_results)
    return ''.join(memory_texts[i] for i in ids[0] if i < len(memory_texts))


def build_and_query(messages: list, model_name: str = None) -> str:
    """
    Add user message to memory, retrieve relevant history,
    render prompt via Jinja2, and query the LLM API.
    """
    # Add last user message to memory
    last_msg = messages[-1]['content']
    add_to_memory(last_msg)

    # Retrieve relevant history
    history = get_relevant_history()

    # Render prompt with template
    prompt = render_prompt(history, last_msg, model_name)

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 700,
            "temperature": float(os.getenv("TEMPERATURE", 0.7)),
            "top_p": float(os.getenv("TOP_P", 0.9)),
            "return_full_text": False
        }
    }

    try:
        response = httpx.post(
            MODEL_URL,
            headers=HEADERS,
            json=payload,
            timeout=40.0
        )
        response.raise_for_status()
        generated = response.json()[0].get("generated_text", '').strip()
        # Save assistant response to memory
        add_to_memory(generated)
        return generated
    except Exception as e:
        return f"⚠️ Error: {e}"