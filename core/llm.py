import os
from langchain_openai import ChatOpenAI

_llm_cache = {}

def get_llm(temperature=0.7):
    global _llm_cache
    key = f"temp_{temperature}"

    if key not in _llm_cache:
        _llm_cache[key] = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=temperature,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    return _llm_cache[key]
