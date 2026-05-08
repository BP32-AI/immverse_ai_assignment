# src/vector_store.py

import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import (
    VECTOR_STORE_DIR,
    EMBEDDING_MODEL
)
class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.index = faiss.read_index(
            os.path.join(VECTOR_STORE_DIR, "faiss.index")
        )
        with open(
            os.path.join(VECTOR_STORE_DIR, "chunks.pkl"),
            "rb"
        ) as file:

            self.chunks = pickle.load(file)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )
        results = []
        for idx in indices[0]:
            results.append(self.chunks[idx])
        return results