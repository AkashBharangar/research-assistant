from tools import web_search, read_page
from langchain_core.messages import HumanMessage, ToolMessage
from llm import llm, llm_with_tools
from prompts import RESEARCH_PROMPT

def summarize(content: str):
    prompt = RESEARCH_PROMPT.format(content=content)

    responses = llm.invoke(prompt)

    return responses

tool_map = {
    "web_search" : web_search,
    "read_page" : read_page
}

def run_agent(query: str):

    messages = [HumanMessage(content=query)]

    while True:

        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            return response.content

        for tool_call in response.tool_calls:

            tool = tool_map[tool_call["name"]]

            result = tool.invoke(tool_call["args"])

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )