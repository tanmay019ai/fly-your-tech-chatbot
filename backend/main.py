from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": req.message}
        ]
    }

    res = requests.post(API_URL, headers=HEADERS, json=payload)
    data = res.json()

    if "choices" in data:
        return {"reply": data["choices"][0]["message"]["content"]}

    if "error" in data:
        return {"reply": data["error"]["message"]}

    return {"reply": "Unexpected response"}
