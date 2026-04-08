from state import AgentState
from skills.registry import load_skills
from utils.utils import chunk_documents
from tools.vector_store import create_vector_store
from tools.pdf_loader import load_pdf_with_pages


pdf_skills = None
def pdf_agent(state: AgentState):
    global pdf_skills
    
    if pdf_skills is None:
        docs = load_pdf_with_pages("files/sample.pdf")
        chunks = chunk_documents(docs)
        db = create_vector_store(chunks)

        pdf_skills = load_skills(db)

    skill = pdf_skills["pdf_qa"]
    result = skill.run({
        "question": state["task"],
        "history": state.get("messages", [])
    })

    return {"result": result}
