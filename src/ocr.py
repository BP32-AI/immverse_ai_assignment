# src/ocr.py

import os
import pytesseract
from PIL import Image
from preprocess import preprocess_image
from config import IMAGE_DIR, OCR_OUTPUT_DIR
os.makedirs(OCR_OUTPUT_DIR, exist_ok=True)
SUPPORTED_EXTENSIONS = [".png", ".jpg", ".jpeg"]

def run_ocr():

    image_files = [
        file for file in os.listdir(IMAGE_DIR)
        if os.path.splitext(file)[1].lower() in SUPPORTED_EXTENSIONS
    ]
    for image_name in image_files:
        image_path = os.path.join(IMAGE_DIR, image_name)
        processed_image = preprocess_image(image_path)
        text = pytesseract.image_to_string(
            processed_image,
            lang="hin"
            # lang="eng"
        )
        output_filename = os.path.splitext(image_name)[0] + ".txt"
        output_path = os.path.join(
            OCR_OUTPUT_DIR,
            output_filename
        )
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"OCR completed: {output_filename}")


if __name__ == "__main__":
    run_ocr()