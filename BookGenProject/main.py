import sys
import os

# Add .claudecode to the python path to allow imports from it
sys.path.append(os.path.join(os.path.dirname(__file__), '.claudecode'))

from orchestration.main_orchestrator import Orchestrator

def main():
    print("Welcome to the Claude Code Book Generator")
    
    # Inputs (Could be dynamic input() calls)
    topic = "The Future of Artificial Intelligence"
    genre = "Non-Fiction/Tech"
    audience = "Tech Enthusiasts and General Public"
    
    app = Orchestrator()
    final_book = app.create_book(topic, genre, audience)
    
    # Save Output
    with open("generated_book.md", "w") as f:
        f.write(final_book)
        
    print("\n=== Success! Book saved to 'generated_book.md' ===")

if __name__ == "__main__":
    main()

