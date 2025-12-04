from config import client

class CharacterHelperSkill:
    """
    Skill: Character Development Helper
    Purpose: Generates or fleshes out character details.
    """

    def run(self, name: str, role: str) -> Dict[str, str]:
        """
        Creates a character profile.
        """
        system_prompt = "You are a creative writer. Build a deep, believable character profile."
        user_prompt = f"""
        Create a profile for:
        Name: {name}
        Role: {role}
        
        Include: Motivation, Flaws, and Backstory.
        """
        
        response = client.generate_text(system_prompt, user_prompt)
        
        # In a real app, we might parse JSON here.
        return {"raw_profile": response}
