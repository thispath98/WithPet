from models.graph_state import GraphState
from nodes.base_node import BaseNode

class GenerateAnswerNode(BaseNode):
    def execute(self, state):
        chatllm = self.context.llm
        question = state["question"]
        data = state["web_response"] if state["data_source"] == "web" else state["data"]
        final_query = f"""
            Based on the user's question: {question}
            and the following retrieved information:
            {data}
            Please provide a detailed and concise answer in Korean.
            """
        final_answer = chatllm.invoke(final_query)

        return GraphState(answer=final_answer.content)

def handle_no_data(state: GraphState) -> GraphState:
    return GraphState(answer='해당하는 데이터를 찾을 수 없습니다. 다른 질문을 해주세요.')