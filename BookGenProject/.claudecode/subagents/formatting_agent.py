class FormattingAgent:
    """
    Agent: Formatting Sub-Agent
    Role: Ensures the final output is clean and structured (Markdown/HTML).
    Dependencies: None (Pure Logic)
    """
    
    def format_book(self, chapters: dict) -> str:
        print("[Formatting Agent] Compiling final manuscript...")
        full_text = "# Book Title\n\n"
        
        for title, content in chapters.items():
            full_text += f"## {title}\n\n{content}\n\n---\n\n"
            
        return full_text
