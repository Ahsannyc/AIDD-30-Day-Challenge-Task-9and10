from config import client

class OutlineGeneratorSkill:
    """
    Skill: Chapter Outline Generator
    Purpose: Creates a structured chapter list based on a book topic.
    """

    def run(self, topic: str, genre: str, target_audience: str) -> List[str]:
        """
        Generates a list of chapter titles.
        """
        system_prompt = "You are an expert book outliner. Generate a concise table of contents."
        user_prompt = f"""
        Create a 5-chapter outline for a book.
        Topic: {topic}
        Genre: {genre}
        Audience: {target_audience}
        
        Output format: A simple numbered list of chapter titles.
        """
        
        response = client.generate_text(system_prompt, user_prompt)
        
        # Parse response into a list (simple splitting for demo)
        lines = [line.strip() for line in response.split('\n') if line.strip()]
        return lines
