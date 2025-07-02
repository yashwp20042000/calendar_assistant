# 🗓️ Google Calendar AI Assistant

An AI-powered conversational assistant that integrates with Google Calendar for appointment booking and availability checks, powered by FastAPI, LangChain, OpenAI, and Google APIs.

---

## 🚀 Features

✅ Conversational AI to interact with users  
✅ Book appointments directly into Google Calendar  
✅ Check availability of upcoming events  
✅ Built with FastAPI backend and LangChain for LLM integration  
✅ Secure credential handling via environment variables  
✅ Deployment-ready for platforms like Render or Railway  

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, Uvicorn  
- **AI/LLM**: LangChain, OpenAI, LangChain-Community  
- **Google Integration**: Google Calendar API, Google Service Account  
- **Environment Handling**: python-dotenv  
- **Deployment Tested On**: Render.com  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/calendar_assistant.git
cd calendar_assistant/backend
```
### 2️⃣ Setup Environment

- Obtain Google Service Account credentials with Calendar API access
- Prepare .env file in backend/ directory.

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 10000
```
---

###📚 Useful Links

- Render Lnk: "https://calendar-assistant-ptyw.onrender.com"
- Streamlit Link: "https://calendarassistantgit-vqshhdmapdtdsjbvmm2u4m.streamlit.app/"
- Github Link: "https://github.com/yashwp20042000/calendar_assistant.git"

---
