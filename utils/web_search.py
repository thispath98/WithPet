
from typing import Dict
import os

from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import SerpAPIWrapper
from models.llm import chatllm


def web_search(
    temperature: float,
    template: str,
    serpapi_params: Dict[str, str],
    query: str,
) -> str:


    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
    )

    llm_chain = prompt | chatllm

    search = SerpAPIWrapper(
        serpapi_api_key=os.getenv("SERPAPI_API_KEY"),
        params=serpapi_params,
    )

    search_results = search.run(query)
    output = llm_chain.run(query=search_results)
    return output


if __name__ == "__main__":
    TEMPERATURE = 0.0
    TEMPLATE = """
You are a search assistant. Given the query "{query}", provide the best search results and a summary.
"""
    SERPAPI_PARAMS = {
        "engine": "google",
    }
    QUERY = "2024 paris olympic soccer winner team"
    result = web_search(
        temperature=TEMPERATURE,
        template=TEMPLATE,
        serpapi_params=SERPAPI_PARAMS,
        query=QUERY,
    )
    print(result)
