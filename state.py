from typing import TypedDict, List

from langgraph.func import task

class AgentState(TypedDict):
    messages: List[str]
    task: str
    command: str
    skill: str
    agent: str
    result: str
