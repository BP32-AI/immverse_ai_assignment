# src/embeddings.py

import os
import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import (
    CHUNK_OUTPUT_DIR,
    VECTOR_STORE_DIR,
    EMBEDDING_MODEL
)
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)


def generate_embeddings():
    model = SentenceTransformer(EMBEDDING_MODEL)
    chunk_file = os.path.join(
        CHUNK_OUTPUT_DIR,
        "chunks.json"
    )
    with open(chunk_file, "r", encoding="utf-8") as file:
        chunks = json.load(file)
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    faiss.write_index(
        index,
        os.path.join(VECTOR_STORE_DIR, "faiss.index")
    )
    with open(
        os.path.join(VECTOR_STORE_DIR, "chunks.pkl"),
        "wb"
    ) as file:
        pickle.dump(chunks, file)
    print("Embeddings stored successfully")


if __name__ == "__main__":
    generate_embeddings()