from langgraph.graph import StateGraph
from langgraph.graph import START, END

from graph.state import GraphState

from graph.planner import planner_node
from graph.executor import executor_node
from graph.response import response_node


builder = StateGraph(GraphState)

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "executor",
    executor_node
)

builder.add_node(
    "response",
    response_node
)

builder.add_edge(
    START,
    "planner"
)

builder.add_edge(
    "planner",
    "executor"
)

builder.add_edge(
    "executor",
    "response"
)

builder.add_edge(
    "response",
    END
)

graph = builder.compile()