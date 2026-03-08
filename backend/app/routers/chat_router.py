from fastapi import APIRouter
from pydantic import BaseModel
from app.services.groq_service import ask_llm

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    question: str

@router.post("/")
def chat(data: ChatRequest):
    answer = ask_llm(data.question, "AI research assistant")
    return {"response": answer}