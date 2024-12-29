class DefaultTranslateParams:
    def __init__(self):
        self.temperature = 0.0
        self.template = """
You are a professional translator. Given the query "{query}", provide the best result of Korean to English.
"""
