import os

from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent
from langchain.tools import tool
from skills.base import Skill
from tools.command import execute_command


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

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
