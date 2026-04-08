from skills.command_skill import CommandSkill
from skills.pdf_qa_skill import PDFQASkill

def load_skills(db):
    return {
        "command": CommandSkill(),
        "pdf_qa": PDFQASkill(db)
    }
