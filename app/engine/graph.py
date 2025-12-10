from typing import Callable, Dict, Any, Optional

State = Dict[str, Any]
NodeFunc = Callable[[State], State]
BranchFunc = Callable[[State], Optional[str]]

class WorkflowGraph:
    """
    Minimal workflow graph:
    - nodes: dict[node_name, node_function]
    - edges: dict[node_name, either next_node_name (str) OR callable(state)->next_node_name]
    - start_node: str
    """

    def __init__(self, nodes: Dict[str, NodeFunc], edges: Dict[str, object], start_node: str):
        self.nodes = nodes
        self.edges = edges
        self.start_node = start_node

    def run(self, initial_state: Optional[State] = None, max_steps: int = 200) -> (State, list):
        state: State = dict(initial_state or {})
        log: list = []
        current = self.start_node
        steps = 0

        while current is not None and steps < max_steps:
            if current not in self.nodes:
                # unknown node -> stop
                break

            node_fn = self.nodes[current]
            try:
                # run node function (mutates and/or returns state)
                new_state = node_fn(state)
                # ensure state remains a dict
                if not isinstance(new_state, dict):
                    # if user returned None or something, keep existing state
                    new_state = state
            except Exception as e:
                # record the error in log and stop
                log.append({"node": current, "error": str(e)})
                break

            state = dict(new_state)  # shallow copy to freeze snapshot
            log.append({"step": steps + 1, "node": current, "state": dict(state)})

            # decide next node
            next_spec = self.edges.get(current)
            next_node = None
            if isinstance(next_spec, str):
                next_node = next_spec
            elif callable(next_spec):
                try:
                    next_node = next_spec(state)
                except Exception as e:
                    log.append({"node": current, "branch_error": str(e)})
                    next_node = None
            else:
                # absent/None or unknown spec -> stop
                next_node = None

            current = next_node
            steps += 1

        if steps >= max_steps:
            log.append({"warning": "max_steps_reached", "max_steps": max_steps})

        return state, log
