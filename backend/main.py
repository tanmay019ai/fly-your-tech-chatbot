from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.graph import chat_graph

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
    result = chat_graph.invoke(
        {"message": req.message}
    )

    print("🧾 FINAL GRAPH STATE:", result)

    return {
        "reply": result["response"]
    }
