from subagents.research_agent import ResearchAgent
from subagents.writing_agent import WritingAgent
from subagents.editing_agent import EditingAgent
from subagents.formatting_agent import FormattingAgent

class Orchestrator:
    """
    Main Orchestrator Agent
    Role: Manages the workflow from topic to final book.
    """
    def __init__(self):
        self.researcher = ResearchAgent()
        self.writer = WritingAgent()
        self.editor = EditingAgent()
        self.formatter = FormattingAgent()

    def create_book(self, topic: str, genre: str, audience: str):
        print(f"\n=== Starting Book Generation: {topic} ===")
        
        # Step 1: Outline
        print("\n--- Step 1: Generating Outline ---")
        chapters = self.writer.generate_outline(topic, genre, audience)
        print(f"Generated {len(chapters)} chapters.")
        
        final_chapters = {}
        previous_context = "Start of book."
        
        # Step 2: Loop through chapters
        for i, chapter_title in enumerate(chapters):
            print(f"\n--- Processing Chapter {i+1}: {chapter_title} ---")
            
            # Research
            research_data = self.researcher.process(f"{topic} - {chapter_title}")
            
            # Write
            draft = self.writer.draft_chapter(chapter_title, research_data)
            
            # Edit
            final_text = self.editor.review(draft, previous_context)
            
            final_chapters[chapter_title] = final_text
            previous_context += f"\nSummary of {chapter_title}: {draft[:100]}..."
            
        # Step 3: Format
        print("\n--- Step 3: Formatting Final Manuscript ---")
        book_content = self.formatter.format_book(final_chapters)
        
        return book_content
