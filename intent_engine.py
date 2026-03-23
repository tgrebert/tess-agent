import re
from typing import Dict, Any

class IntentEngine:
    def __init__(self):
        # Basic keyword heuristics for our initial prototype
        self.coding_keywords = r'\b(write|refactor|debug|code|function|class|script|bug|compile|build)\b'
        self.system_keywords = r'\b(check|run|status|start|stop|ip|memory|disk|install|update|system|process)\b'

    def parse_intent(self, user_input: str) -> Dict[str, Any]:
        """
        Analyzes natural language input to determine if it's a System Query or a Coding Task.
        """
        input_lower = user_input.lower()
        
        is_coding = bool(re.search(self.coding_keywords, input_lower))
        is_system = bool(re.search(self.system_keywords, input_lower))
        
        # Simple routing logic
        if is_coding and not is_system:
            intent = "Coding Task"
            confidence = 0.8
        elif is_system and not is_coding:
            intent = "System Query"
            confidence = 0.8
        elif is_coding and is_system:
            intent = "Hybrid (System & Coding)"
            confidence = 0.5
        else:
            intent = "General Conversation / Unknown"
            confidence = 0.2

        return {
            "intent": intent,
            "confidence": confidence,
            "original_input": user_input
        }

if __name__ == "__main__":
    # Quick tests
    engine = IntentEngine()
    print(engine.parse_intent("Can you refactor this python script to run faster?"))
    print(engine.parse_intent("Check the disk space on the main server and restart Docker."))
    print(engine.parse_intent("Hello Tess, how are you today?"))
