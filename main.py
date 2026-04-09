from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage

from graph import buid_graph
from sandbox.sandbox import app

graph = buid_graph()
config = {"configurable": {"thread_id": "1"}}

def run_task(task: str):
    result = graph.invoke({
        "messages": [HumanMessage(content=task)],
        "task": task,
        "result": ""  
    }, config)
    
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
