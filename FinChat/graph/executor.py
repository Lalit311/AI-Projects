from graph.state import GraphState
from tools.registry import TOOL_REGISTRY

def executor_node(state: GraphState):
    outputs = {}

    for step in state.execution_plan:
        tool = TOOL_REGISTRY[step.tool]
        outputs[step.tool] = tool.run(**step.input)

    return {
        "tool_outputs": outputs
    }