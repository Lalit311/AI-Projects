from typing import Any
from pydantic import BaseModel, Field
from graph.models import ExecutionStep

class GraphState(BaseModel):

    # User Input
    question: str

    # Planner Output
    intent: str | None = None
    execution_plan: list[ExecutionStep] = Field(default_factory=list)
    
    # Executor Output
    tool_outputs: dict[str, Any] = Field(default_factory=dict)

    # Final Response
    final_answer: str | None = None