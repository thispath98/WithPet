from langchain_core.prompts import ChatPromptTemplate

from .base_node import BaseNode

from ..modules.context import Context
from ..modules.graph_state import GraphState
from ..modules.response_schema import QueryRouter


class SelectDataNode(BaseNode):
    def __init__(
        self,
        context: Context,
        source_routing_prompt: str,
    ) -> None:
        super().__init__(context=context)
        self.source_routing_prompt = source_routing_prompt

    def execute(
        self,
        state: GraphState,
    ) -> GraphState:
        llm = self.context.llm
        question = state["question"]

        structured_llm = llm.with_structured_output(QueryRouter)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.source_routing_prompt),
                ("human", "{question}"),
            ]
        )

        # Define router
        router = prompt | structured_llm

        response = router.invoke(question)
        print(response.datasource)
        return GraphState(data_source=response.datasource)
