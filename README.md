🚀 ResearchAIHub – AI Research Assistant










ResearchAIHub is a full-stack AI-powered chatbot application that allows users to ask research questions and receive intelligent answers in real time.

The project integrates a modern React frontend with a high-performance FastAPI backend and connects to large language models using the Groq API.

This project demonstrates how to build a scalable AI-powered web application using modern technologies.

✨ Features

🤖 AI-powered chatbot

⚡ Fast API backend

🎨 Clean and interactive UI

🔗 Integration with large language models

📡 REST API communication

🧩 Modular project structure

🛠 Tech Stack
Frontend

React

TypeScript

Axios

Backend

FastAPI

Uvicorn

Python

Groq LLM API

📂 Project Structure
ResearchAIHub
│
├── backend
│   ├── app
│   │   ├── routers
│   │   │   └── chat_router.py
│   │   │
│   │   ├── services
│   │   │   └── groq_service.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   ├── public
│   │   └── index.html
│   │
│   ├── src
│   │   ├── components
│   │   │   └── Chatbot.tsx
│   │   │
│   │   ├── api
│   │   │   └── chat.ts
│   │   │
│   │   ├── App.tsx
│   │   └── index.tsx
│   │
│   └── package.json
│
└── README.md
🧠 System Architecture
User
  │
  ▼
React Frontend
  │
  ▼
Axios API Request
  │
  ▼
FastAPI Backend
  │
  ▼
Groq LLM API
  │
  ▼
AI Response
  │
  ▼
Displayed in Chatbot UI
⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/yourusername/ResearchAIHub.git
cd ResearchAIHub
🔧 Backend Setup

Navigate to backend folder:

cd backend

Create virtual environment:

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Example requirements.txt

fastapi
uvicorn
groq
python-dotenv
pydantic
🔑 Environment Variables

Create a .env file inside backend folder

backend/.env

Add your Groq API key.

GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key

Get your key here:

https://console.groq.com/keys

▶️ Run Backend Server
uvicorn app.main:app --reload

Backend will run at

http://127.0.0.1:8000

API documentation

http://127.0.0.1:8000/docs
🎨 Frontend Setup

Open another terminal.

Navigate to frontend folder:

cd frontend

Install dependencies:

npm install
▶️ Run Frontend
npm start

Frontend will run at

http://localhost:3000
🔄 How the Application Works

User enters a question in the chatbot UI

React frontend sends request using Axios

Request reaches FastAPI backend

Backend sends prompt to Groq LLM

AI generates response

Response is displayed in chatbot interface

📸 Frontend Screenshot

<img width="1304" height="872" alt="Screenshot 2026-03-08 141634" src="https://github.com/user-attachments/assets/b3a95cc4-cf24-47be-a9fd-eedfa1e5b7ff" />

📸 Backend Screenshot

<img width="1856" height="918" alt="Screenshot 2026-03-08 141621" src="https://github.com/user-attachments/assets/ae96ffeb-6016-4b2d-9f82-fc8abbaca84c" />


[ Insert Demo GIF ]
🚀 Deployment (Optional)
Deploy Backend

You can deploy the FastAPI backend using:

Render

Railway

Docker

Deploy Frontend

React app can be deployed using:

Vercel

Netlify
