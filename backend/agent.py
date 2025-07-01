# LangChain Conversational Agent Logic
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from backend.calendar_utils import check_availability, book_appointment

load_dotenv()

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_agent(message):
    # Simple version: Process message, check intent manually (expand with LangGraph later)
    if "available" in message.lower():
        events = check_availability()
        if not events:
            return "Your calendar is free. Would you like to book a slot?"
        return f"You have {len(events)} upcoming events."

    if "book" in message.lower():
        # Dummy booking - Replace with parsed time from message
        start = "2024-07-01T15:00:00Z"
        end = "2024-07-01T15:30:00Z"
        book_appointment(start, end, "AI Scheduled Meeting")
        return "Meeting successfully booked!"

    return llm.invoke(message)
