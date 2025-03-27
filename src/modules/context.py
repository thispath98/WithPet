from typing import Union

from sqlite3 import Connection

from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_pinecone import PineconeVectorStore


class Context:
    def __init__(
        self,
        llm: ChatOpenAI,
        llm_stream: ChatOpenAI,
        conn: Connection,
        vs_example: FAISS,
        vs_data: Union[FAISS, PineconeVectorStore],
    ) -> None:
        self.llm = llm
        self.llm_stream = llm_stream
        self.conn = conn
        self.vs_example = vs_example
        self.vs_data = vs_data
