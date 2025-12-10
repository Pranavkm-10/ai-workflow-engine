from typing import Dict, Any, Optional
from app.engine.graph import WorkflowGraph
from app.engine.tools import get_tool

State = Dict[str, Any]

# -------------------------
# Node implementations
# -------------------------

def extract_functions_node(state: State) -> State:
    code = state.get("code", "")
    tool = get_tool("extract_functions")
    out = tool(code)
    state = dict(state)
    state["functions"] = out.get("functions", [])
    state["functions_count"] = out.get("count", 0)
    return state

def check_complexity_node(state: State) -> State:
    funcs = state.get("functions", [])
    tool = get_tool("check_complexity")
    out = tool(funcs)
    state = dict(state)
    state["complexity_score"] = out.get("complexity_score", 0.0)
    return state

def detect_issues_node(state: State) -> State:
    code = state.get("code", "")
    tool = get_tool("detect_smells")
    out = tool(code)
    state = dict(state)
    state["issues"] = out.get("issues", 0)
    state["todos"] = out.get("todos", 0)
    state["long_lines"] = out.get("long_lines", 0)
    return state

def suggest_improvements_node(state: State) -> State:
    state = dict(state)
    # compute simple quality score out of 100
    issues = state.get("issues", 0)
    complexity = state.get("complexity_score", 0.0)
    # base 100, penalize issues and complexity
    score = 100 - issues * 10 - int(complexity * 50)
    if score < 0:
        score = 0
    state["quality_score"] = score

    suggestions = []
    if issues > 0:
        suggestions.append("Address TODOs and long lines.")
    if complexity > 0.6:
        suggestions.append("Refactor complex functions into smaller units.")
    if state.get("functions_count", 0) == 0:
        suggestions.append("Add functions / modularize code for readability.")

    if not suggestions:
        suggestions.append("Code looks good. Add tests and docstrings if missing.")

    state["suggestions"] = suggestions
    return state

# -------------------------
# Graph builder
# -------------------------

def create_code_review_graph(threshold: int = 80) -> WorkflowGraph:
    nodes = {
        "extract": extract_functions_node,
        "complexity": check_complexity_node,
        "issues": detect_issues_node,
        "improve": suggest_improvements_node,
    }

    def decide_next(state: State) -> Optional[str]:
        # stop if quality meets threshold, else loop to issues node once to recompute
        score = state.get("quality_score", 0)
        if score >= threshold:
            return None  # stop
        # simple: if still low, either stop (to avoid infinite loops) or re-run detect_issues
        # We'll re-run detect_issues once more (this is a simple loop example)
        # If you want multi-iteration, the graph engine supports it via this function.
        # For now return None to stop after one improve step to keep runs finite.
        return None

    edges = {
        "extract": "complexity",
        "complexity": "issues",
        "issues": "improve",
        "improve": decide_next,
    }

    return WorkflowGraph(nodes=nodes, edges=edges, start_node="extract")
