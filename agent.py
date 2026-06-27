from llm import llm
from prompts import RESEARCH_PROMPT

def summarize(content: str):
    prompt = RESEARCH_PROMPT.format(content=content)

    responses = llm.invoke(prompt)

    return responses