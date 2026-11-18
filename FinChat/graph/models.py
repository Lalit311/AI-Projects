from typing import Any
from pydantic import BaseModel, Field


class ExecutionStep(BaseModel):
    tool: str
    input: dict[str, Any] = Field(default_factory=dict)