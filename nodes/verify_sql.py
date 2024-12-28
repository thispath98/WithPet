from models.graph_state import GraphState
from utils.data_utils import filter_csv_with_sql
import pandas as pd
import re

def verify_sql(state: GraphState) -> GraphState:
    response = state["sql_response"]    
    trial_num=state["trial_num"]
    print(f'<<Trial {trial_num}>>')

    match = re.search(r'<SQL>(.*?)</SQL>', response, re.DOTALL)
    if match:
        sql_query = match.group(1).strip()
    else:
        return GraphState(sql_status = 'retry', trial_num=state["trial_num"]+1)

    filtered_data = filter_csv_with_sql(sql_query)
    print(filtered_data)

    if isinstance(filtered_data, pd.DataFrame) and not filtered_data.empty:
        return GraphState(sql_status = 'data exists', data=filtered_data)
    elif trial_num < 3:
        return GraphState(sql_status = 'retry', trial_num=state["trial_num"]+1)
    else:
        return GraphState(sql_status = 'no data')