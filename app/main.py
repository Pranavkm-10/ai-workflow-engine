from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from uuid import uuid4

from app.workflows.code_review import create_code_review_graph
from app.engine.graph import WorkflowGraph
from app.engine.tools import register_default_tools

app = FastAPI(title="Minimal AI Workflow Engine")

# In-memory stores
GRAPHS: Dict[str, WorkflowGraph] = {}
RUNS: Dict[str, Dict[str, Any]] = {}

# Register default tools at startup
register_default_tools()

class CreateGraphRequest(BaseModel):
    workflow_type: str = "code_review"
    threshold: int = 80

class CreateGraphResponse(BaseModel):
    graph_id: str

class RunGraphRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any] = {}

class RunGraphResponse(BaseModel):
    run_id: str
    final_state: Dict[str, Any]
    log: list

@app.post("/graph/create", response_model=CreateGraphResponse)
def create_graph(req: CreateGraphRequest):
    if req.workflow_type == "code_review":
        graph = create_code_review_graph(threshold=req.threshold)
    else:
        # default to code_review if unknown - easy to extend
        graph = create_code_review_graph(threshold=req.threshold)

    graph_id = f"graph_{uuid4().hex[:8]}"
    GRAPHS[graph_id] = graph
    return {"graph_id": graph_id}

@app.post("/graph/run", response_model=RunGraphResponse)
def run_graph(req: RunGraphRequest):
    graph = GRAPHS.get(req.graph_id)
    if graph is None:
        raise HTTPException(status_code=404, detail="graph_id not found")

    final_state, log = graph.run(req.initial_state)
    run_id = f"run_{uuid4().hex[:8]}"
    RUNS[run_id] = {"state": final_state, "log": log}
    return {"run_id": run_id, "final_state": final_state, "log": log}

@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    data = RUNS.get(run_id)
    if data is None:
        raise HTTPException(status_code=404, detail="run_id not found")
    return data

if __name__ == "__main__":
    import uvicorn
    # Run via VS Code "Run Python File" — this will open the server in the integrated output window.
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
    
