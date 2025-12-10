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



