# AI Workflow Engine (Minimal)

Minimal workflow/agent engine (sample: Code Review workflow) implemented with:
- Python + FastAPI
- Simple graph engine (nodes, edges, branching, loop)
- Tool registry (in-memory)
- In-memory run storage
- Swagger UI at `/docs`

## How to run (without using command prompt; use VS Code run)
1. Open folder in VS Code.
2. Create a Python environment (Ctrl+Shift+P → "Python: Create Environment") and select it.
3. Open `requirements.txt` and install missing packages using VS Code suggestions or the IDE UI.
4. Open `app/main.py` and click "Run Python File" (or Run → Start Debugging).
5. Open browser: `http://127.0.0.1:8000/docs` to test endpoints.

## Endpoints
- `POST /graph/create` → create a graph instance
- `POST /graph/run` → run a graph with initial state
- `GET  /graph/state/{run_id}` → fetch run state & log

## What to improve (future)
- Persist graphs & runs to a database
- Make nodes asynchronous for external calls
- Authentication and input validation
- Better tool implementations (real code analysis tools)
