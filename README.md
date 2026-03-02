🚀 ResearchHub AI
Intelligent Research Paper Management and Analysis System using Agentic AI
📌 Overview

ResearchHub AI is an intelligent, agentic AI-powered research paper management platform designed to help researchers efficiently discover, organize, and analyze academic literature.

With the exponential growth of scientific publications, researchers struggle to manually search, manage, and analyze large volumes of research papers. ResearchHub AI solves this problem by combining:

Secure user authentication

Workspace-based paper organization

AI-powered contextual analysis

Vector embeddings for document retrieval

Large Language Model integration

The system is built using:

Frontend: React + TypeScript + Tailwind CSS

Backend: FastAPI (Python 3.12)

LLM Integration: Groq

Model Used: Llama 3.3 70B

Authentication: JWT (python-jose)

Password Hashing: Passlib (bcrypt)

Embeddings: sentence-transformers

🎯 Problem Statement

Researchers often:

Search multiple academic databases manually

Download and organize PDFs separately

Read large volumes of papers

Struggle to compare findings across papers

Lack AI-assisted contextual research tools

ResearchHub AI provides an intelligent assistant that:

Searches and imports research papers

Stores them in organized workspaces

Answers contextual research questions

Generates summaries and comparisons

Maintains secure user-specific data

🧠 Core Features
1️⃣ Secure Authentication

User Registration

User Login

JWT-based access control

Password hashing using bcrypt

Protected API routes

2️⃣ Research Paper Discovery

Query academic APIs

Retrieve metadata:

Title

Authors

Publication Date

Abstract

One-click import to workspace

3️⃣ Workspace Management

Multiple workspaces per user

Example:

"Deep Learning Research"

"Medical Imaging Analysis"

User-specific paper storage

Context-aware AI conversations

4️⃣ AI-Powered Chatbot

The chatbot:

Retrieves workspace papers

Converts abstracts into vector embeddings

Fetches relevant context

Sends context to Groq LLM

Generates research-specific answers

Example Questions:

"What are differences between Transformers and CNN?"

"Summarize findings across imported papers."

"Compare methodologies used in these studies."

🏗 Technical Architecture
Frontend (React + TS)
        ↓
FastAPI Backend
        ↓
Authentication (JWT)
        ↓
Database (Users, Papers, Workspaces)
        ↓
Vector Embeddings
        ↓
Groq LLM (Llama 3.3 70B)
📂 Project Structure (Backend)
app/
│
├── main.py
├── database.py
├── models/
│     ├── user.py
│     ├── paper.py
│     ├── workspace.py
│
├── schemas/
│     ├── user_schema.py
│     ├── paper_schema.py
│
├── routers/
│     ├── auth.py
│     ├── papers.py
│     ├── workspace.py
│     ├── chat.py
│
├── services/
│     ├── groq_client.py
│     ├── vector_store.py
│
├── utils/
│     ├── security.py
│
└── .env
🔐 Authentication Flow

User registers

Password hashed using bcrypt

User logs in

JWT access token generated

Token required for protected routes

🔎 Vector-Based Retrieval System

Abstracts converted into embeddings

Stored in vector index

Relevant papers retrieved based on query similarity

Context sent to LLM for accurate response

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/researchhub-ai.git
cd researchhub-ai
2️⃣ Create Virtual Environment
python -m venv .venv

Activate:

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup Environment Variables

Create .env file:

GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

Generate Groq API Key from:
Groq Console

5️⃣ Run Backend
uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000
6️⃣ Run Frontend
npm install
npm start

Frontend runs on:

http://localhost:3000
🌐 CORS Configuration

Ensure FastAPI allows frontend:

origins = ["http://localhost:3000"]
🧪 Testing Flow

Register user

Login → receive JWT

Create workspace

Search papers

Import paper

Ask chatbot questions

Receive AI-generated contextual responses

🛡 Security Features

Password hashing (bcrypt)

JWT-based authentication

User-isolated workspaces

Protected endpoints

Environment-based secrets

👨‍💻 Team Members

Kishan Kumar

Manas Jain

Ruchi Yadav

Deepansh Asati (Team Lead)

📊 Project Stats

Total Epics: 9

Total Tasks: 16

🔮 Future Enhancements

PDF content extraction

Research paper citation graph

Multi-user collaboration

Export summaries as PDF

Real-time AI streaming responses

📌 Conclusion

ResearchHub AI transforms traditional research workflows by integrating secure authentication, intelligent paper management, and advanced LLM-powered analysis into one unified system.

It reduces manual effort, enhances productivity, and enables researchers to gain insights faster using Agentic AI architecture.
