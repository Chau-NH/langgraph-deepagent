def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def chunk_documents(documents, chunk_size=500):
    chunks = []
    for doc in documents:
        text = doc["text"]
        page = doc["page"]

        text_chunks = chunk_text(text, chunk_size)
        for chunk in text_chunks:
            chunks.append({"page": page, "text": chunk})
    return chunks



FORBIDDEN = ["rm", "shutdown", "reboot", "mkfs", "dd"]
def is_command_safe(command):
    return not any(forbidden in command for forbidden in FORBIDDEN)

def extract_command(task):
    task = task.strip()

    if task.startswith("run:"):
        return task.replace("run:", "", 1).strip()

    if task.startswith("execute:"):
        return task.replace("execute:", "", 1).strip()

    return task
