import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def load_pdf(pdf_path = "/content/HSC26-Bangla1st-Paper.pdf"):
    images = convert_from_path(pdf_path, dpi=300)

    ignore_pages = [1, 19] + list(range(22, 41))
    result = []

    for i, img in enumerate(images):
        if i in ignore_pages:
            print(f"Skipping page {i}")
            continue

        text = pytesseract.image_to_string(img, lang='ben')
        doc = {
            'text': text,
            'metadata': {
                'page': i
            }
        }
        result.append(doc)
        print(f"Processed page {i}/{len(images)-1}")
    return result

# texts = load_pdf()
# with open("output.txt", "w", encoding="utf-8") as f:
#     for item in texts:
#         f.write(item['text'] + "\n")