class DefaultWebParams:
    def __init__(self):
        self.temperature = 0.0
        self.template = """
You are a search assistant. Given the query "{query}", provide the best search results and a summary.
"""
        self.serpapi_params = {
            "engine": "google",
        }
