# FastAPI Application Entry Point
from fastapi import FastAPI, HTTPException
from backend.calendar_utils import check_availability, book_appointment
from backend.agent import chat_with_agent
from backend.models import ChatRequest, ChatResponse

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        reply = chat_with_agent(request.message)
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

