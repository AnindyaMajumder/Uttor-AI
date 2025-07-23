from loader import load_pdf
from clean_text import clean_text

# == Load and clean PDF text ==
text = load_pdf()
print("Extracted text length:", len(text))
# print(text)
print(text[19])  

for i in range(len(text)):
    text[i] = clean_text(text[i])
    print(f"Cleaned text for page {i+1}: {text[i]}:")