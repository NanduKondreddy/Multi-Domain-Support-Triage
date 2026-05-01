# HackerRank Orchestrate: Support Triage Agent

A zero-dependency, deterministic support triage agent that classifies, routes, and resolves tickets across HackerRank, Claude, and Visa ecosystems. 

## Architecture

```text
Input Ticket 
   │
   ├─> 1. Sanitizer: Normalizes text, strips injection patterns
   ├─> 2. Classifier & Router: Identifies intent, request_type, and target domain
   ├─> 3. Retriever: BM25 + TF-IDF with Query Expansion & Re-ranking
   ├─> 4. Escalation Guard: Validates confidence and enforces hard safety rules
   │
   ▼
 Output (Status, Product Area, Response, Justification, Request Type)
```

## Core Design Decisions

1. **Why lexical retrieval (BM25 + TF-IDF) instead of vector embeddings?**
   - **Determinism & Stability:** Embeddings introduce non-determinism across environments and require heavy dependencies (PyTorch, sentence-transformers).
   - **Zero-Dependency:** This entire pipeline runs on the Python Standard Library. Zero installation friction.
   - **Performance:** Processes the entire batch of tickets in < 1 second.
   
2. **Why Query Expansion and Re-ranking?**
   - Lexical retrieval's main weakness is the "vocabulary mismatch" problem (e.g., "kicked out" vs "session timeout").
   - We use a mapped **Query Expansion** step to inject canonical corpus vocabulary before retrieval, significantly boosting recall.
   - To prevent precision loss (expansion noise), we use a **Post-Retrieval Re-ranker** that re-scores the top candidates against the *original, un-expanded query*.

3. **Why a Calibrated Escalation Threshold?**
   - Instead of an arbitrary confidence cutoff, the escalation threshold (`0.46`) was calibrated against the `sample_support_tickets.csv` golden dataset.
   - This ensures a data-backed balance between helpfulness (replies) and safety (escalations).

4. **Pattern-Generalized Routing over Hardcoded Rules**
   - Uses domain-specific pattern groups (e.g., `_BEDROCK_TERMS`, `_TRAVEL_CARD_TERMS`) instead of exact string matches, ensuring robust handling of unseen ticket phrasings without the fragility of massive IF/ELSE chains.

## Trade-offs Considered

| Approach | Why Rejected |
|---|---|
| Vector Embeddings (Dense Retrieval) | High complexity, large dependency footprint (GBs), unnecessary for a 100-document corpus. |
| LLM-in-the-loop Reasoning | Violates determinism requirements, high latency, requires API keys and network access. |
| Cosine Similarity only | TF-IDF alone struggles with term saturation; BM25 handles document length normalization better. We use a hybrid approach. |

## Known Failure Modes
- **Highly abstract phrasings:** If a user issue is described entirely in metaphor or highly abstract terms without overlapping synonyms in the expansion map, retrieval confidence drops and the system gracefully escalates.
- **Multiple competing issues:** While multi-intent detection exists, if a ticket contains three equally critical but unrelated domain issues, the system prioritizes safety and may escalate.

## Reproducing the Results

This project has **zero external dependencies** outside of the Python standard library.

```bash
# Run regression tests (17 golden cases covering edge scenarios)
python code/tests/test_regression.py

# Run pipeline on input data
python code/main.py --input support_tickets/support_tickets.csv --output support_tickets/output.csv

# View rich debug trace for routing and retrieval decisions
python code/main.py --debug
```
