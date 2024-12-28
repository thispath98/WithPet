from langchain_core.prompts import PromptTemplate
from models.llm import CHATLLM



def ko_to_eng(
    template: str,
    query: str,
) -> str:

    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
    )

    llm_chain = prompt | CHATLLM

    output = llm_chain.run(query=query)
    return output


if __name__ == "__main__":
    TEMPERATURE = 0.0
    TEMPLATE = """
You are a professional translator. Given the query "{query}", provide the best result of Korean to English.
"""

    QUERY = "부산 수영구의 돼지국밥 맛집 추천해줘."
    result = ko_to_eng(
        template=TEMPLATE,
        query=QUERY,
    )
    print(result)
