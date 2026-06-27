from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

search = DuckDuckGoSearchAPIWrapper(region="wt-wt", max_results=5)

def web_search(query: str):
    responses = search.results(query, max_results=5)
    return responses

