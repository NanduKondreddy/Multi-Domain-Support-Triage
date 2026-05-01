# code/ - Core Implementation

This directory contains the primary logic for the Multi-Domain Support Triage Agent.

## 🚀 Execution
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
# Copy .env.example to .env and add your ANTHROPIC_API_KEY

# 3. Run the agent
python main.py --input ../support_issues/support_issues.csv --output ../support_issues/output.csv
```

## 📂 Module Map
- **`main.py`**: Entry point. Orchestrates the loading of data and the triage loop.
- **`agent.py`**: The "Intelligence Controller." Handles intent detection, confidence fusion, and response generation.
- **`retriever.py`**: Implements the Hybrid Retrieval logic (BM25 + Vector Search).
- **`semantic_safety.py`**: Embedded safety layer for detecting high-risk semantic categories.
- **`sanitizer.py`**: Security layer for prompt injection and PII removal.
- **`decision_engine.py`**: Deterministic decision logic for safe escalation.

## ⚙️ Configuration
The agent's sensitivity can be tuned in `agent.py`:
- `CONF_HIGH` (0.65): Confidence required for a direct grounded answer.
- `CONF_LOW` (0.40): Confidence below which we force human escalation.
- `USE_EMBEDDINGS`: Toggle semantic search in the retriever.
