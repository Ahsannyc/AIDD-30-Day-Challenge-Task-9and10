from config import client

class ResearchSkill:
    """
    Skill: Research & Fact-Checking
    Purpose: Retrieves key facts or context about a specific sub-topic.
    """

    def run(self, query: str) -> str:
        """
        Performs research on a query.
        """
        system_prompt = "You are a meticulous research assistant. Provide key facts and verify accuracy."
        user_prompt = f"""
        Research the following topic and provide 3 key bullet points with mock citations.
        Topic: {query}
        """
        
        response = client.generate_text(system_prompt, user_prompt)
        return response
