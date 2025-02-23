import os

import sqlite3
from sqlite3 import Connection
import pandas as pd


def load_csv_to_sqlite(
    csv_files: str,
    db_path: str = ":memory:",
) -> Connection:
    conn = sqlite3.connect(db_path)

    print(os.getcwd())

    for file_path, table_name in csv_files.items():
        try:
            df = pd.read_csv(file_path)
            df.to_sql(
                name=table_name,
                con=conn,
                index=False,
                if_exists="replace",
            )
            print(f"Loaded {file_path} into table '{table_name}'.")
        except Exception as e:
            print(f"Error loading {file_path} into table '{table_name}': {e}")

    return conn


def filter_csv_with_sql(
    query: str,
    conn: Connection,
) -> pd.DataFrame:
    try:
        # Execute the SQL query
        result = pd.read_sql_query(
            sql=query,
            con=conn,
        )
        return result
    except Exception as e:
        return f"Error executing query: {e}"


def format_docs_with_metadata(docs: pd.DataFrame) -> str:
    formatted_docs = []
    for i, doc in enumerate(docs):
        metadata_str = "\n".join(
            [
                f"{key}: {value}"
                for key, value in doc.metadata.items()
                if pd.notnull(value)
            ]
        )
        formatted_docs.append(f"<Data {i+1}>\n{metadata_str}\n{doc.page_content}")
    return "\n\n".join(formatted_docs)


def format_dataframe(
    df: pd.DataFrame,
    data_source: str,
) -> str:
    columns = (
        [
            "RESTAURANT_NAME_KOREAN",
            "FOOD_TYPE",
            "ADDRESS_KOREAN",
            "MENU_NAME",
            "NATIONAL_PHONE_NUMBER",
            "BREAKFAST_YN",
            "LUNCH_YN",
            "DINNER_YN",
            "BEER_YN",
            "OUTDOOR_SEAT_YN",
            "MENU_FOR_CHILDREN_YN",
            "RESTROOM_YN",
            "PARKING_LOT_YN",
            "DISTRICT",
            "RESTAURANT_NAME_ENGLISH",
            "ADDRESS_ENGLISH",
            "REVIEW",
        ]
        if data_source == "restaurants"
        else [
            "PLACE_NM",
            "ADDRESS",
            "TEL_NO",
            "SEASON_NM",
            "CATEGORY",
            "AREA",
            "DESCRIPTION",
        ]
    )
    return df[columns].to_markdown(index=False)
