from skills.style_enhancer import StyleEnhancerSkill
from skills.plot_checker import PlotConsistencySkill

class EditingAgent:
    """
    Agent: Editing Sub-Agent
    Role: Refines the draft for style, grammar, and consistency.
    Dependencies: StyleEnhancerSkill, PlotConsistencySkill
    """
    def __init__(self):
        self.style_skill = StyleEnhancerSkill()
        self.plot_skill = PlotConsistencySkill()

    def review(self, draft_text: str, prev_context: str = "") -> str:
        print("[Editing Agent] Reviewing draft...")
        
        # 1. Check Consistency
        consistency_notes = self.plot_skill.run(draft_text, prev_context)
        
        # 2. Enhance Style
        refined_text = self.style_skill.run(draft_text, tone="Engaging")
        
        return f"{refined_text}\n\n[Editor Notes]: {consistency_notes}"
