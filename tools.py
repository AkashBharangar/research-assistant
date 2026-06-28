from langchain.tools import tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from utils.scraper import read_webpage

search = DuckDuckGoSearchAPIWrapper(region="wt-wt", max_results=5)

@tool
def web_search(query: str):
    """Search the web."""
    return search.results(query, max_results=5)

@tool
def read_page(url: str):
    """Read a web page"""

    return read_webpage(url)[:6000]
