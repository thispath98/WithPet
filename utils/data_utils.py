import sqlite3
import pandas as pd
import os

csv_files = {
    "data/내국인 관심 관광지_수정.csv": "local_tourist_spots",
    "data/외국인 관심 관광지_수정.csv": "foreign_tourist_spots",
    "data/busan_restrau_20to24_witch_eng_data.csv": "restaurants",
}

def load_csv_to_sqlite(csv_files, db_path=":memory:"):
    conn = sqlite3.connect(db_path)

    print(os.getcwd())

    for file_path, table_name in csv_files.items():
        try:
            df = pd.read_csv(file_path) 
            df.to_sql(table_name, conn, index=False, if_exists="replace") 
            print(f"Loaded {file_path} into table '{table_name}'.")
        except Exception as e:
            print(f"Error loading {file_path} into table '{table_name}': {e}")
    
    return conn

def filter_csv_with_sql(query: str):
    try:
        # Execute the SQL query
        result = pd.read_sql_query(query, load_csv_to_sqlite(csv_files))
        return result
    except Exception as e:
        return f"Error executing query: {e}"