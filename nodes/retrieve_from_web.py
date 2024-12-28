import dotenv

dotenv.load_dotenv(
    override=True,
)

from models.graph_state import GraphState
from configs.default_translate_params import DefaultTranslateParams
from utils.translate import ko_to_eng
from configs.default_web_params import DefaultWebParams
from utils.web_search import web_search


def retrieve_from_web(state: GraphState) -> GraphState:
    query = state["question"]

    default_translate_params = DefaultTranslateParams()
    translated = ko_to_eng(
        temperature=default_translate_params.temperature,
        template=default_translate_params.template,
        query=query,
    )

    default_web_params = DefaultWebParams()
    output = web_search(
        temperature=default_web_params.temperature,
        template=default_web_params.template,
        serpapi_params=default_web_params.serpapi_params,
        query=translated,
    )
    return GraphState(answer=output)


if __name__ == "__main__":
    state = GraphState(
        question="부산 수영구의 돼지국밥 맛집 추천해줘.",
    )
    output = retrieve_from_web(state)
    print(output)
