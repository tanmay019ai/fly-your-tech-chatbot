import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def call_llm(message: str) -> str:
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": message}],
    }

    res = requests.post(API_URL, headers=HEADERS, json=payload)
    data = res.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]

    if "error" in data:
        return data["error"]["message"]

    return "LLM error"
