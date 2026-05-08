# Architecture Documentation

# System Architecture

```text
Input Images
      ↓
OCR Pipeline
      ↓
Extracted Text
      ↓
Chunking + Metadata
      ↓
Embeddings Generation
      ↓
FAISS Vector Store
      ↓
Retriever
      ↓
LLM
      ↓
Conversational Response
```

---

# OCR Module

Tool Used:
- Tesseract OCR

Reason:
- Open-source
- Lightweight
- Supports Indic languages
- Easy reproducibility

---

# Text Processing

Chunking Strategy:
- Chunk Size: 500
- Chunk Overlap: 100

Reason:
- Preserves semantic continuity
- Better retrieval quality

---

# Embedding Model

Model:
- sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

Reason:
- Multilingual
- Lightweight
- Good semantic retrieval performance

---

# Vector Store

Tool:
- FAISS

Reason:
- Fast similarity search
- Lightweight local storage
- Efficient retrieval

---

# LLM Selection

Model Used:
- qwen2.5

Reason for Selection:

The assignment involves:
- multilingual understanding
- conversational interaction
- Indic-language manuscript reasoning
- grounded question answering

Qwen2.5 was selected because:

- Strong multilingual capabilities
- Better handling of Hindi and Indic languages
- Good instruction-following performance
- Lightweight deployment through Ollama
- Efficient local inference
- Good contextual reasoning for RAG systems

The model integrates easily with local/self-hosted Ollama APIs and provides reliable conversational responses for retrieval-augmented generation pipelines.

---

# Retrieval Pipeline

Steps:
1. Convert query into embeddings
2. Search relevant chunks
3. Build context
4. Generate grounded answer

---

# Scaling Strategy

For scaling to millions of pages:

- Distributed vector database
- Parallel OCR processing
- Batch embedding generation
- Metadata indexing
- GPU inference
- Caching frequently accessed queries

---

# Latency Optimization

- Smaller embedding models
- FAISS indexing
- Chunk caching
- Parallel OCR execution
- Query optimization