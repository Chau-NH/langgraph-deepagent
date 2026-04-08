from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, AIMessage

from graph import buid_graph
from sandbox.sandbox import app

graph = buid_graph()

class Memory:
    def __init__(self):
        self.history = []

    def add(self, user_input: str, result: str):
        self.history.append(HumanMessage(content=user_input))
        self.history.append(AIMessage(content=result))

    def get(self):
        return self.history
    
    def last(self, k=4):
        return self.history[-k:]
    
    def print(self):
        print("\n--- Conversation History ---")
        for msg in self.history:
            print(msg)
        print("----------------------------\n")

memory = Memory()

def run_task(task: str):
    result = graph.invoke({
        "messages": memory.get(),
        "task": task,
        "result": ""  
    })
    
    memory.add(task, result.get("result", ""))
    return result.get("result", "")

@app.local_entrypoint()
def main():
    print("=== Multi-Agent System Demo ===\n")

    tasks = [
        "What is this PDF about?",
        "Explain more",
        "Give details",
        "run: echo Hello from the command agent!"
    ]

    for task in tasks:
        print(f"\n🧑 User: {task}")
        result = run_task(task)
        print("\n🤖 Assistant:")
        print(result)

    # while True:
    #     task = input("\n🧑 User: ")
    #     if task.lower() in ["exit", "quit"]:
    #         print("Exiting...")
    #         break

    #     result = run_task(task)
    #     print(f"🤖 Assistant: {result}")
