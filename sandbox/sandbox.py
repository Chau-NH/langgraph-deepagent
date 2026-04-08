import modal
import subprocess

app = modal.App("sandbox-app")

image = modal.Image.debian_slim().pip_install("pandas", "openpyxl")

@app.function(image=image, timeout=10)
def run_command(command: str):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "error": str(e)
        }
