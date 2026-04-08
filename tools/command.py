from sandbox.sandbox import run_command

def execute_command(command: str):
    result = run_command.remote(command)
    return result["stdout"] or result["stderr"]
