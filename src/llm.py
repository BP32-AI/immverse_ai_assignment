# src/llm.py

import requests
from config import (
    OLLAMA_URL,
    OLLAMA_MODEL
)

def generate_response(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )
    data = response.json()
    return data.get("response", "")