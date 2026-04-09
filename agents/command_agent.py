from langchain_core.messages import AIMessage
from state import AgentState
from skills.registry import load_skills
from utils.utils import is_command_safe, extract_command

command_skills = None

def command_agent(state: AgentState):
    global command_skills
    
    if command_skills is None:
        command_skills = load_skills(db=None)

    skill = command_skills["command"]
    cmd = extract_command(state["task"])

    if not is_command_safe(cmd):
        msg = "❌ Sorry, this command is not allowed for safety reasons."
        return {"result": msg, "messages": [AIMessage(content=msg)]}

    result = skill.run({"command": cmd})

    return {"result": result, "messages": [AIMessage(content=result)]}
