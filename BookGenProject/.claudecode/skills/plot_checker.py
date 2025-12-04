from config import client

class PlotConsistencySkill:
    """
    Skill: Plot Consistency Checker
    Purpose: Analyzes narrative flow to ensure no contradictions exist.
    """

    def run(self, current_chapter_summary: str, previous_context: str) -> str:
        """
        Checks for inconsistencies.
        """
        system_prompt = "You are a continuity editor. Flag any plot holes or character inconsistencies."
        user_prompt = f"""
        Previous Context: {previous_context}
        Current Chapter: {current_chapter_summary}
        
        Are there any contradictions?
        """
        
        response = client.generate_text(system_prompt, user_prompt)
        return response
