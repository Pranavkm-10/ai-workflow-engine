# AI Workflow Engine – Coding Assignment

## 📌 Project Overview

This project implements a **minimal AI-style workflow engine** using **Python and FastAPI**.  
The engine executes **agent-like workflows** defined as a graph of nodes, where each node performs a task and updates a shared state.

The objective of this assignment is to demonstrate:
- Workflow orchestration
- Agent-based execution
- Shared state management
- Modular and extensible backend design

A **Code Review Workflow** is implemented as a sample agent to showcase the engine’s capabilities.

---

## 🧠 Key Concepts

- **Workflow Graph**: A directed graph representing steps in a workflow
- **Node**: A Python function that processes and updates workflow state
- **State**: A shared dictionary passed between workflow steps
- **Tools**: Reusable helper functions accessed by workflow nodes
- **Agent-style Execution**: Step-by-step reasoning with decision-based stopping

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


---

## 🗂 Project Structure



ai-workflow-engine/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── app/
├── main.py
├── init.py
│
├── engine/
│ ├── graph.py # Workflow execution engine
│ ├── tools.py # Tool registry and utilities
│ └── init.py
│
└── workflows/
├── code_review.py # Code Review workflow implementation
└── init.py


---

## ✅ Implemented Features

### ✔ Workflow Engine
- Executes workflow nodes step-by-step
- Maintains shared state across nodes
- Supports sequential execution and decision-based stopping
- Generates execution logs for debugging

### ✔ Tool Registry
- Centralized registration of tools
- Nodes dynamically invoke tools
- Easily extendable to real AI/ML or LLM tools

### ✔ Sample Workflow – Code Review Agent
The sample workflow performs:
1. Function extraction from code
2. Complexity estimation
3. Basic issue detection (TODOs, long lines)
4. Suggestion generation
5. Quality score calculation
6. Threshold-based completion

### ✔ FastAPI Backend
- REST API interface for workflow creation and execution
- Swagger UI support for easy testing

### ✔ In-Memory Execution Storage
- Stores workflow graphs and execution results during runtime
- Maintains full execution logs

---

## 🔌 API Endpoints

### 1️⃣ Create Workflow Graph
**POST /graph/create**

**Request**
```json
{
  "workflow_type": "code_review",
  "threshold": 80
}


Response

{
  "graph_id": "graph_xxxxx"
}

2️⃣ Run Workflow

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
    "suggestions": [
      "Address TODOs"
    ]
  },
  "log": []
}

3️⃣ Get Workflow State

GET /graph/state/{run_id}

Returns the stored execution state and log for a workflow run.

▶️ How to Run the Project
Requirements

Python 3.10 or higher

FastAPI

Uvicorn

Steps

Open the project root folder

Install dependencies:

pip install -r requirements.txt


Run the application:

python -m app.main


Open browser:

http://127.0.0.1:8000/docs

🧪 Testing

All APIs can be tested using Swagger UI at:

http://127.0.0.1:8000/docs

🔮 Future Improvements

Persistent database storage

Asynchronous workflow execution

Integration with real static analysis tools

LLM-powered agent workflows

Authentication and authorization

Workflow visualization UI

🎯 Why This Project Matters

This project demonstrates:

Backend system design

AI-agent workflow orchestration

Clean modular architecture

API-driven execution pipelines

The same architecture can be extended to:

AI agents

LLM pipelines

Automation systems

Data processing workflows

🧑‍💻 Author

Pranav Km
B.Tech Computer Science Engineering
Graduation Year: 2026

✅ Assignment Completed Successfully


---

If you want next, I can:
- Rewrite this into **resume bullet points**
- Shorten it for **GitHub profile pin**
- Prepare **interview explanation answers**
- Help you add **one advanced feature** to stand out

Just tell me 👍
