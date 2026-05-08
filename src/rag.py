# src/rag.py

from vector_store import VectorStore
from llm import generate_response

class RAGPipeline:

    def __init__(self):
        self.vector_store = VectorStore()

    def ask(self, query):
        retrieved_chunks = self.vector_store.search(query)
        context = "\n\n".join([
            chunk["text"]
            for chunk in retrieved_chunks
        ])
        sources = list(set([
            chunk["metadata"]["page_number"]
            for chunk in retrieved_chunks
        ]))
        prompt = f"""
                    You are a manuscript assistant.
                    Answer ONLY from provided context.
                    Context:
                    {context}
                    Question:
                    {query}
                    Answer:
                """
        answer = generate_response(prompt)
        return {
            "answer": answer,
            "sources": sources
        }