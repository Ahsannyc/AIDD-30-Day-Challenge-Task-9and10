from skills.researcher import ResearchSkill

class ResearchAgent:
    """
    Agent: Research Sub-Agent
    Role: Prepares background information for the writer.
    Dependencies: ResearchSkill
    """
    def __init__(self):
        self.skill = ResearchSkill()

    def process(self, topic: str) -> str:
        print(f"[Research Agent] Gathering info on: {topic}...")
        research_data = self.skill.run(topic)
        return research_data
