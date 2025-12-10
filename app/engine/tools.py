from typing import Callable, Dict, Any

Tool = Callable[..., Dict[str, Any]]
TOOLS: Dict[str, Tool] = {}

def register_tool(name: str, func: Tool):
    TOOLS[name] = func

def get_tool(name: str) -> Tool:
    if name not in TOOLS:
        raise KeyError(f"tool '{name}' not registered")
    return TOOLS[name]

# -------------------------
# Simple / fake tool implementations
# -------------------------

def extract_functions(code: str) -> Dict[str, Any]:
    """
    Very simple heuristic: return list of 'functions' as lines starting with 'def '.
    This is a placeholder for real parsing.
    """
    lines = (code or "").splitlines()
    funcs = []
    for ln in lines:
        stripped = ln.strip()
        if stripped.startswith("def "):
            # take the function name until '('
            name = stripped[4:].split("(")[0].strip()
            funcs.append(name)
    return {"functions": funcs, "count": len(funcs)}

def check_complexity(functions: list) -> Dict[str, Any]:
    """
    Fake complexity score: complexity = min(1.0, 0.1 * number_of_functions + random small bias)
    """
    num = len(functions or [])
    score = min(1.0, 0.1 * num)
    return {"complexity_score": score}

def detect_smells(code: str) -> Dict[str, Any]:
    """
    Fake smell detector: count occurrences of 'TODO' + very long lines
    """
    lines = (code or "").splitlines()
    todos = sum(1 for ln in lines if "TODO" in ln)
    long_lines = sum(1 for ln in lines if len(ln) > 120)
    issues = todos + long_lines
    return {"issues": issues, "todos": todos, "long_lines": long_lines}

def register_default_tools():
    register_tool("extract_functions", extract_functions)
    register_tool("check_complexity", check_complexity)
    register_tool("detect_smells", detect_smells)
