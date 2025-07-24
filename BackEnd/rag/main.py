from splitter import semantic_splitter
from loader import load_pdf
from clean_text import clean_text
from langchain_core.documents import Document

# == Load and clean PDF text ==
text = load_pdf()
print("Extracted text length:", len(text))
# print(text[19]["text"])

# Clean text in each dict
for i in range(len(text)):
    text[i]["text"] = clean_text(text[i]["text"])

# Convert to Document objects for semantic splitting
documents = [Document(page_content=entry["text"], metadata=entry["metadata"]) for entry in text]

semantic_chunks = semantic_splitter(documents)
print(type(semantic_chunks))
print("Number of semantic chunks:", len(semantic_chunks))