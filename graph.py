from langgraph.graph import StateGraph
from agents.pdf_agent import pdf_agent
from agents.command_agent import command_agent
from state import AgentState
from core.llm import get_llm

db = None
llm = get_llm(temperature=0.7)

def router(state: AgentState):
    task = state.get("task")
    messages = state.get("messages", [])

    history_text = "\n".join(
        [msg.content for msg in messages[-4:]]
    )

    prompt = f"""
    Conversation History:
    {history_text}

    Task:
    {task}

    Decide which agent should handle the task.

    Agents:
    1. pdf_agent: Answers questions based on the content of a PDF document.
    2. command_agent: Executes a shell command in a safe sandbox environment.
    3. unknown_agent: Handles requests that don't fit the other agents.

    Return ONLY one:
    pdf_agent or command_agent or unknown_agent
    """

    response = llm.invoke(prompt)
    decision = response.content.strip().lower()

    if "pdf" in decision:
        agent = "pdf_agent"
    elif "command" in decision:
        agent = "command_agent"
    else:
        agent = "unknown_agent"

    return {"agent": agent}

def route_decision(state: AgentState):
    agent = state.get("agent")
    return agent

def buid_graph():
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("router", router)

    graph_builder.add_node("pdf_agent", pdf_agent)
    graph_builder.add_node("command_agent", command_agent)
    graph_builder.add_node("unknown_agent", lambda state: {"result": "❌ Sorry, I don’t understand this request. Please try again with a clearer instruction."})

    graph_builder.set_entry_point("router")
    graph_builder.add_conditional_edges(
        "router",
        route_decision,
        {
            "pdf_agent": "pdf_agent",
            "command_agent": "command_agent",
            "unknown_agent": "unknown_agent"
        }
    )

    return graph_builder.compile()
