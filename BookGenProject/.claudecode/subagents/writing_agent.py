from skills.outline_generator import OutlineGeneratorSkill
from skills.character_helper import CharacterHelperSkill
from config import client

class WritingAgent:
    """
    Agent: Writing Sub-Agent
    Role: Drafts the content of the book chapters.
    Dependencies: OutlineGeneratorSkill, CharacterHelperSkill, (Internal Writing Logic)
    """
    def __init__(self):
        self.outline_skill = OutlineGeneratorSkill()
        self.character_skill = CharacterHelperSkill()

    def generate_outline(self, topic: str, genre: str, audience: str):
        return self.outline_skill.run(topic, genre, audience)

    def draft_chapter(self, chapter_title: str, research_context: str) -> str:
        print(f"[Writing Agent] Drafting chapter: {chapter_title}...")
        
        system_prompt = "You are a skilled author. Write a compelling chapter draft."
        user_prompt = f"""
        Title: {chapter_title}
        Context/Research: {research_context}
        
        Write the chapter content (approx 500 words).
        """
        return client.generate_text(system_prompt, user_prompt)
