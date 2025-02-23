from ..modules.context import Context
from ..modules.graph_state import GraphState


class BaseNode:
    def __init__(
        self,
        context: Context,
    ) -> None:
        self.context = context  # Shared context for LLM, DB connection, etc.

    def execute(
        self,
        state: GraphState,
    ) -> GraphState:
        raise NotImplementedError("Subclasses must implement the 'execute' method.")
