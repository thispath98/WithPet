from langgraph.graph import END, StateGraph
from models.graph_state import GraphState
from nodes.select_data_source import select_data_source
from nodes.generate_sql import generate_sql
from nodes.retrieve_from_web import retrieve_from_web
from nodes.verify_sql import verify_sql
from nodes.generate_final_answer import generate_final_answer, handle_no_data
from nodes.routing import get_data_source, get_sql_status

sql_workflow = StateGraph(GraphState)

sql_workflow.add_node("select_vec", select_data_source)
sql_workflow.add_node("generate_sql", generate_sql)
sql_workflow.add_node("retrieve_from_web", retrieve_from_web)
sql_workflow.add_node("verify_sql", verify_sql)  
sql_workflow.add_node("generate_final_answer", generate_final_answer)
sql_workflow.add_node("handle_no_data", handle_no_data) 

sql_workflow.add_edge("generate_sql", "verify_sql")
sql_workflow.add_edge("retrieve_from_web", "generate_final_answer")
sql_workflow.add_edge("generate_final_answer", END)
sql_workflow.add_edge("handle_no_data", END)

sql_workflow.add_conditional_edges(
    "select_vec",
    get_data_source,
    {
        'local_tourist_spots': "generate_sql", 
        'foreign_tourist_spots': "generate_sql",
        'restaurants': "generate_sql",
        'web': "retrieve_from_web",
    },
)

sql_workflow.add_conditional_edges(
    "verify_sql",
    get_sql_status,
    {
        'retry': "generate_sql", 
        'data exists': "generate_final_answer",
        'no data': "handle_no_data",
    },
)

sql_workflow.set_entry_point("select_vec")