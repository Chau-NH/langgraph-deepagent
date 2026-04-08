from skills.base import Skill
from tools.pdf_qa import ask_pdf

class PDFQASkill(Skill):
    name = "PDF Question Answering"
    description = "Answers questions based on the content of a PDF document."

    def __init__(self, db):
        self.db = db

    def run(self, input: dict):
        question = input.get("question")
        history = input.get("history", [])

        if not self.db or not question:
            return "Database and question are required."

        answer = ask_pdf(self.db, question, history)
        return answer
