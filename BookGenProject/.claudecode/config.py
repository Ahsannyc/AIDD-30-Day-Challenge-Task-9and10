import os
import time
from typing import List, Dict, Any

# Mock Mode for demonstration purposes (set to False to use real API)
MOCK_MODE = True

class ClaudeClient:
    """
    A wrapper for the Anthropic Client to handle calls or mock them.
    """
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key and not MOCK_MODE:
            print("Warning: ANTHROPIC_API_KEY not found. Defaulting to Mock Mode.")
    
    def generate_text(self, system_prompt: str, user_prompt: str, max_tokens: int = 1000) -> str:
        """
        Simulates or performs a text generation call.
        """
        if MOCK_MODE:
            time.sleep(0.5) # Simulate latency
            return self._get_mock_response(system_prompt, user_prompt)
        
        # Real implementation would look like:
        # client = anthropic.Anthropic(api_key=self.api_key)
        # message = client.messages.create(...)
        # return message.content[0].text
        return "Real API call placeholder."

    def _get_mock_response(self, system: str, user: str) -> str:
        """
        Returns plausible mock data based on keywords in the prompt.
        """
        user_lower = user.lower()
        
        if "outline" in user_lower:
            return """
            1. Introduction to AI
            2. The History of Neural Networks
            3. Modern LLMs
            4. Future Implications
            5. Conclusion
            """
        elif "research" in user_lower:
            return """Key Fact: The first neural network was proposed in 1944.
Source: Wikipedia."""
        elif "style" in user_lower or "grammar" in user_lower:
            return "Improved Text: The quick brown fox jumps over the lazy dog. (Corrected for flow)."
        elif "plot" in user_lower:
            return "Consistency Check: No contradictions found in the timeline."
        elif "character" in user_lower:
            return """Name: John Doe
Role: Protagonist
Motivation: To learn Python."""
        elif "write" in user_lower or "draft" in user_lower:
            return "This is a drafted paragraph for the requested chapter. It flows well and covers the topic."
        else:
            return "Processed request successfully."

# Singleton instance
client = ClaudeClient()
