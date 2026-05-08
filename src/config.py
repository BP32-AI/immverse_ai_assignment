import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DATA PATHS
IMAGE_DIR = os.path.join(BASE_DIR, "data/images")
OCR_OUTPUT_DIR = os.path.join(BASE_DIR, "output/ocr")
CHUNK_OUTPUT_DIR = os.path.join(BASE_DIR, "output/chunks")
VECTOR_STORE_DIR = os.path.join(BASE_DIR, "output/vector_store")

# MODEL CONFIG
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# LOCAL OLLAMA URL
OLLAMA_URL = "http://localhost:11434/api/generate"

OLLAMA_MODEL = "qwen2.5"

# CHUNK SETTINGS
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100