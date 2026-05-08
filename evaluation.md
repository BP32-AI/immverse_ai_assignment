# Evaluation Documentation

# OCR Evaluation

OCR quality can be evaluated using:

- Character Error Rate (CER)

Reference text can be compared against OCR output.

Suggested Tool:
- jiwer

---

# RAG Evaluation

Evaluation performed on:

- Retrieval relevance
- Answer correctness
- Groundedness
- Hallucination reduction

---

# Sample Queries

1. What is the manuscript about?
2. Explain verse 2.
3. Summarize the manuscript.

---

# Evaluation Methodology

## Retrieval Evaluation

Check:
- Whether relevant chunks are retrieved

## Answer Evaluation

Check:
- Whether answer is grounded in context
- Whether hallucinations are reduced

---

# Observations

- Vector retrieval improves contextual accuracy
- Chunk overlap improves semantic continuity
- OCR quality highly impacts downstream retrieval

---

# Future Evaluation Improvements

- Human evaluation
- Retrieval precision metrics
- Answer faithfulness scoring
- Semantic similarity evaluation