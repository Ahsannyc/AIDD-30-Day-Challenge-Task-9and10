from config import client

class StyleEnhancerSkill:
    """
    Skill: Writing Style & Grammar Enhancer
    Purpose: Refines text to match a specific tone and fixes grammatical errors.
    """

    def run(self, text: str, tone: str = "Professional") -> str:
        """
        Enhances the provided text.
        """
        system_prompt = f"You are a world-class editor. Improve clarity, grammar, and apply a {tone} tone."
        user_prompt = f"""
        Rewrite the following text:
        "{text}"
        """
        
        response = client.generate_text(system_prompt, user_prompt)
        return response
