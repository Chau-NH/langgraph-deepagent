from deepagents import create_deep_agent
from langchain.tools import tool
from skills.base import Skill
from tools.command import execute_command
from core.llm import get_llm    


llm = get_llm(temperature=0)

@tool(description="Executes a shell command and returns the output.")
def run_command(command: str):
    return execute_command(command)

class CommandSkill(Skill):
    name = "Command Execution"
    description = "Executes a shell command and returns the output."

    def __init__(self):
        self.agent = create_deep_agent(
            tools=[run_command],
            model=llm,
            system_prompt="Always use the tool to execute commands. Do not explain."
        )

    def run(self, input: dict):
        command = input.get("command")
        if not command:
            return "No command provided."
        
        result = self.agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"Execute this command: {command}"
                }
            ]
        })

        return result["messages"][-1].content.strip()
