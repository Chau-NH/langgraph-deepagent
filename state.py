from typing import TypedDict, Annotated

from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    task: str
    command: str
    skill: str
    agent: str
    result: str
