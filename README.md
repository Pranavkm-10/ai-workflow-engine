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


---

## Project Structure


---

## Implemented Features

### Workflow Engine
- Executes workflow nodes step-by-step
- Maintains shared state across nodes
- Supports sequential execution and decision-based stopping
- Generates execution logs

### Tool Registry
- Centralized registration of tools
- Nodes dynamically invoke tools
- Extendable to real AI/ML or LLM-based tools

### Sample Workflow – Code Review Agent
1. Extracts functions
2. Estimates complexity
3. Detects issues (TODOs, long lines)
4. Generates suggestions
5. Computes quality score
6. Stops when threshold is reached

### FastAPI Backend
- REST API interface
- Swagger UI for interactive testing

### In-Memory Execution Storage
- Stores workflow graphs
- Stores execution logs and final state

---

## API Endpoints

### Create Workflow Graph
POST /graph/create

Request:
```json
{
  "workflow_type": "code_review",
  "threshold": 80
}
{
  "graph_id": "graph_xxxxx"
}
{
  "graph_id": "graph_xxxxx",
  "initial_state": {
    "code": "def hello():\n    # TODO\n    print('Hello')"
  }
}
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



