# Book Generation System (Claude Code Project)

This project is a modular AI system designed to generate non-fiction or fiction books using a multi-agent architecture. It satisfies **Task 9 (Skills)** and **Task 10 (Sub-Agents)** of the AIDD 30-Day Challenge.

## Project Structure

- **`.claudecode/skills/`**: reusable functional units (Python modules) that perform specific tasks (e.g., Outline Generation, Fact Checking).
- **`.claudecode/subagents/`**: Specialized agents that utilize skills to perform complex roles (e.g., Researcher, Writer).
- **`.claudecode/orchestration/`**: The manager logic that coordinates the sub-agents.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your `ANTHROPIC_API_KEY` in your environment variables (optional for mock mode).

## Usage

Run the main entry point to generate a book:

```bash
python main.py
```

## Architecture

The system uses a **Waterfall-Agile Hybrid flow**:
1. **Research Agent** gathers context.
2. **Orchestrator** (with Outline Skill) generates the chapter plan.
3. **Writing Agent** drafts chapters iteratively.
4. **Editing Agent** refines the text.
5. **Formatting Agent** prepares the final output.
