from workflows.sql_workflow import sql_workflow
from models.graph_state import GraphState

def main():
    initial_state = GraphState(
        question="광안리 근처 사진찍기 좋은 곳 추천해주세요",
        trial_num=0,
        sql_status="",
    )

    app = sql_workflow.compile()

    result = app.invoke(initial_state)
    print("Final Answer:", result['answer'])

if __name__ == "__main__":
    main()