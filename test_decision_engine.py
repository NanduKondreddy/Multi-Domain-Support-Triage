import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "code"))

from agent import SupportAgent

# ? FIX: use Path instead of string
agent = SupportAgent(data_dir=Path("data"))

test_cases = [
    "How do I reset my password?",
    "I don't recognize this charge",
    "Something is wrong",
    "How to enable international transactions?",
    "My card was declined abroad",
    "What happens if a candidate disconnects during interview?"
]

print("\n=== PHASE 3 DECISION TEST ===\n")

for i, text in enumerate(test_cases, 1):
    result = agent.triage({
        "issue": text,
        "company": "",
        "subject": ""
    })

    print(f"{i}. Query: {text}")
    print(f"   Status: {result['status']}")
    print(f"   Justification: {result['justification']}")
    print("-" * 60)
