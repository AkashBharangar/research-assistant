from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import read_page, web_search

load_dotenv()

llm = ChatGroq(
    model ="llama-3.3-70b-versatile",
    temperature=0
)

tools = [web_search, read_page]

llm_with_tools = llm.bind_tools(tools)