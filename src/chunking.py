# src/chunking.py

import os
import json
from config import (
    OCR_OUTPUT_DIR,
    CHUNK_OUTPUT_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)
os.makedirs(CHUNK_OUTPUT_DIR, exist_ok=True)


def create_chunks(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def process_chunks():
    all_chunks = []
    txt_files = [
        file for file in os.listdir(OCR_OUTPUT_DIR)
        if file.endswith(".txt")
    ]
    for txt_file in txt_files:
        page_number = txt_file.split(".")[0]
        file_path = os.path.join(OCR_OUTPUT_DIR, txt_file)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        chunks = create_chunks(
            text,
            CHUNK_SIZE,
            CHUNK_OVERLAP
        )
        for index, chunk in enumerate(chunks):
            chunk_data = {
                "chunk_id": f"{page_number}_{index}",
                "text": chunk,
                "metadata": {
                    "page_number": page_number,
                    "source": "manuscript",
                    "chunk_index": index
                }
            }
            all_chunks.append(chunk_data)
    output_file = os.path.join(
        CHUNK_OUTPUT_DIR,
        "chunks.json"
    )
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(all_chunks, file, ensure_ascii=False, indent=4)
    print("Chunking completed")


if __name__ == "__main__":
    process_chunks()