
# AI Workflow Engine – Coding Assignment

## 📌 Project Overview
This project implements a **minimal AI-style workflow engine** using **Python and FastAPI**.  
The engine executes **agent-like workflows** defined as a directed graph of nodes. Each node performs a task and updates a shared state.

This assignment demonstrates:
- Workflow orchestration  
- Agent-based execution  
- Shared state management  
- Modular and extensible backend design  

A **Code Review Workflow** is implemented as a sample agent to showcase the engine.

---

## 🧠 Key Concepts
- **Workflow Graph**: Directed graph representing workflow steps  
- **Node**: Python function that processes and updates workflow state  
- **State**: Shared dictionary passed between workflow nodes  
- **Tools**: Reusable helper functions accessed by workflow nodes  
- **Agent-style Execution**: Step-by-step execution with decision-based stopping  

---

## ⚙️ Architecture Overview

Client (Swagger UI / API Client)
        |
        v
   FastAPI Application
        |
        v
   Workflow Engine
   ├── Nodes (Functions)
   ├── Shared State
   ├── Decision Logic
   └── Execution Logs
        |
        v
   In-Memory Storage

🗂 Project Structure
ai-workflow-engine/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── app/
    ├── main.py
    ├── __init__.py
    │
    ├── engine/
    │   ├── graph.py        # Workflow execution engine
    │   ├── tools.py        # Tool registry and utilities
    │   └── __init__.py
    │
    └── workflows/
        ├── code_review.py  # Code Review workflow implementation
        └── __init__.py
        

✅ Implemented Features
Workflow Engine

Executes workflow nodes step-by-step

Maintains shared state across nodes

Supports sequential execution and decision-based stopping

Generates execution logs

Tool Registry

Centralized registration of tools

Nodes dynamically invoke tools

Easily extendable to real AI/ML or LLM-based tools

Sample Workflow – Code Review Agent

---

Workflow Steps:

Extracts functions from input code

Estimates code complexity

Detects issues (TODO comments, long lines)

Generates improvement suggestions

Computes a quality score

Stops execution once quality threshold is reached

FastAPI Backend

REST API interface

Swagger UI for interactive testing

In-Memory Storage

Stores workflow graphs

Stores execution logs and final states

---

🔌 API Endpoints
1️⃣ Create Workflow Graph

Endpoint

POST /graph/create


Request

{
  "workflow_type": "code_review",
  "threshold": 80
}


Response

{
  "graph_id": "graph_xxxxx"
}

---

2️⃣ Run Workflow

Endpoint

POST /graph/run


Request

{
  "graph_id": "graph_xxxxx",
  "initial_state": {
    "code": "def hello():\n    # TODO\n    print('Hello')"
  }
}


Response

{
  "run_id": "run_xxxxx",
  "final_state": {
    "quality_score": 90,
    "suggestions": ["Address TODOs"]
  },
  "log": []
}

---

3️⃣ Get Workflow State

Endpoint

GET /graph/state/{run_id}


Description
Returns the stored state and execution log.

---

▶️ How to Run the Project
Requirements

Python 3.10 or higher

FastAPI

Uvicorn

Installation
pip install -r requirements.txt

Run the Server
python -m app.main

Open Swagger UI
http://127.0.0.1:8000/docs

---

🧪 Testing

All APIs can be tested directly using Swagger UI.

---

🔮 Future Improvements

Persistent database storage

Asynchronous workflow execution

Integration with real static analysis tools

LLM-powered agent nodes

Authentication and authorization

Visual workflow builder

---

🎯 Why This Project Matters

Demonstrates backend architecture design

Shows AI-agent workflow orchestration

Uses clean, modular, extensible code

Provides a strong foundation for automation and AI pipelines
