# Mini Manuscript Conversational Pipeline

## Overview

This project implements a mini conversational AI pipeline for Indic manuscript understanding using:

- OCR extraction
- Text chunking
- Vector embeddings
- FAISS vector database
- Retrieval-Augmented Generation (RAG)
- Conversational CLI interface

The system extracts text from manuscript images and enables grounded question-answering over the extracted content.

---

# Features

## Mandatory Features

- OCR pipeline for manuscript images
- Text chunking with metadata
- Embedding generation
- Vector search using FAISS
- Conversational RAG pipeline
- CLI-based chat interface

## Optional Capability

- Multilingual support (Hindi/English)
- Local/self-hosted LLM support

---

# Tech Stack

| Component | Technology |
|---|---|
| OCR | Tesseract OCR |
| Image Processing | OpenCV |
| Embeddings | Sentence Transformers |
| Vector Store | FAISS |
| LLM | Self-hosted Ollama API |
| Language | Python |

---

# Folder Structure

```text
immverse_ai_assignment/
│
├── README.md
├── architecture.md
├── evaluation.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── images/
│   │   ├── page_1.png
│   │   ├── page_2.png
│   │   └── ...
│   │
│   ├── reference_text/
│   │   ├── page_1.txt
│   │   └── ...
│   │
│   └── sample_queries.txt
│
├── output/
│   ├── ocr/
│   │   ├── page_1.txt
│   │   └── ...
│   │
│   ├── chunks/
│   │   └── chunks.json
│   │
│   ├── vector_store/
│   │   ├── faiss.index
│   │   └── chunks.pkl
│   │
│   └── audio/
│
├── sample_outputs/
│   ├── image1.png
│   └── image2.png
│
└── src/
    ├── config.py
    ├── preprocess.py
    ├── ocr.py
    ├── chunking.py
    ├── embeddings.py
    ├── vector_store.py
    ├── llm.py
    ├── rag.py
    ├── chat.py
```

---

# Installation

## Step 1 — Clone Repository

```bash
git clone <your_repo_url>
cd repo
```

---

## Step 2 — Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 3 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Tesseract OCR Setup

Tesseract is required for OCR extraction.

---

## Mac Installation

```bash
brew install tesseract
brew install tesseract-lang
```

---

## Ubuntu/Linux Installation

```bash
sudo apt update

sudo apt install tesseract-ocr

sudo apt install tesseract-ocr-eng

sudo apt install tesseract-ocr-hin
```

---

## Windows Installation

Download installer:

https://github.com/UB-Mannheim/tesseract/wiki

After installation add Tesseract path:

Example:

```text
C:\Program Files\Tesseract-OCR
```

to system environment variables.

---

# Verify Tesseract Installation

Run:

```bash
tesseract --version
```

Check installed languages:

```bash
tesseract --list-langs
```

Expected:

```text
eng
hin
```

---

# Multilingual OCR Setup

This project supports:

- English
- Hindi

You can also add:
- Sanskrit
- Marathi

if language packages are installed.

---

## OCR Language Configuration

File:

```text
src/ocr.py
```

Current:

```python
lang="eng"
```

For Hindi:

```python
lang="hin"
```

For Hindi + English:

```python
lang="hin+eng"
```

For Marathi:

```python
lang="mar"
```

For Sanskrit:

```python
lang="san"
```

---

# Supported Models

The system supports self-hosted Ollama-compatible models.

Current API:

```text
http://localhost:11434/api/generate
```

Example request:

```json
{
  "model": "qwen2.5",
  "prompt": "What is AI?"
}
```

---

# Model Comparison

| Model | Advantages | Limitations |
|---|---|---|
| TinyLlama | Lightweight | Weak multilingual capability |
| Mistral | Strong reasoning | Less Indic-language optimization |
| Llama3 | Good conversation | Higher resource usage |
| Qwen2.5 | Strong multilingual + instruction following | Slightly larger model |

Final Choice:
- Qwen2.5

---

## Selected Model

This project uses:

```text
qwen2.5
```

Reason:
- Better multilingual support
- Good Indic-language understanding
- Strong instruction-following capability
- Efficient for local RAG pipelines

# Add Input Images

Place manuscript images inside:

```text
data/images/
```

Example:

```text
data/images/page_1.png
data/images/page_2.png
```

---

# Run Complete Pipeline

---

## Step 1 — OCR Extraction

Run:

```bash
python src/ocr.py
```

Expected Output:

```text
OCR completed: page_1.txt
OCR completed: page_2.txt
```

Generated files:

```text
output/ocr/
```

---

## Step 2 — Text Chunking

Run:

```bash
python src/chunking.py
```

Generated:

```text
output/chunks/chunks.json
```

---

## Step 3 — Generate Embeddings

Run:

```bash
python src/embeddings.py
```

Generated:

```text
output/vector_store/faiss.index
output/vector_store/chunks.pkl
```

---

## Step 4 — Start Conversational Chat

Run:

```bash
python src/chat.py
```

Example:

```text
Ask:
What is this manuscript about?
```

Output:

```text
Answer:
The manuscript discusses ...

Sources:
page_1
page_2
```

---

# Sample Questions

You can ask:

```text
What is the main topic of this manuscript?
Explain the first section.
Summarize the manuscript.
```

---

# Output Directories

| Folder | Description |
|---|---|
| output/ocr | OCR extracted text |
| output/chunks | Chunked text |
| output/vector_store | FAISS vector index |
| sample_outputs | Sample results |

---

# Multilingual Response Support

You can modify prompts for:

- Hindi responses
- English responses
- Marathi responses

Example prompt:

```python
Answer the question in Hindi.
```

inside:

```text
src/rag.py
```

---

# Architecture Summary

Pipeline:

```text
Images
→ OCR
→ Chunking
→ Embeddings
→ FAISS
→ Retriever
→ LLM
→ Conversational Response
```

---

# Limitations

- OCR accuracy depends on image quality
- Manuscript-style handwritten text may require advanced OCR
- Basic chunking strategy used
- No reranking implemented
- No hybrid search implemented

---

# Future Improvements

- Hybrid Search (BM25 + Vector)
- Streamlit UI
- Text-to-Speech
- Better OCR preprocessing
- Indic-specific OCR models
- Metadata filtering

---

# Author

Brajendra Pateriya