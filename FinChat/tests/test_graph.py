from graph.graph import graph
from graph.state import GraphState


result = graph.invoke(
    GraphState(
        question="How much did I spend on Swiggy?"
    )
)

print(result["final_answer"])