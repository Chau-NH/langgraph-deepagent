class Skill:
    name: str
    description: str

    def run(self, input: dict):
        raise NotImplementedError("Each skill must implement the run method.")
