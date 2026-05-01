import sys
import csv
from pathlib import Path

sys.path.append('code')
from agent import SupportAgent

agent = SupportAgent(Path('data'))

with open('support_tickets/interview_tests.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        res = agent.triage(row)
        print(f"Test {i+1} [{res['status']}]: {row['subject']} -> {res['request_type']} | {res['response'][:60]}...")
