from typing import Dict, Literal

from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

from .base_node import BaseNode
from ..modules.context import Context
from ..modules.graph_state import GraphState


class QueryRouter(BaseModel):
    datasource: Literal["PET_PLACES", "NOT_RELEVANT"] = Field(
        description="Given a user question choose which datasource would be most relevant for answering their question",
    )


class SelectDataNode(BaseNode):
    def __init__(
        self,
        context: Context,
        schemas: Dict[str, str],
        source_routing_template: PromptTemplate,
    ) -> None:
        super().__init__(context=context)
        self.schemas = schemas
        self.source_routing_template = source_routing_template

    def execute(
        self,
        state: GraphState,
    ) -> GraphState:
        llm = self.context.llm
        question = state["question"]

        structured_llm = llm.with_structured_output(QueryRouter)
        router = self.source_routing_template | structured_llm
        response = router.invoke(
            {
                "question": question,
            }
        )
        schema = self.schemas.get(
            response.datasource,
            {},
        )
        return GraphState(
            schema=schema,
            data_source=response.datasource,
        )
