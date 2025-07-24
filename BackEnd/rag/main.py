import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pre-processing'))

from splitter import semantic_splitter
from loader import load_pdf
from clean_text import clean_text

sys.path.append(os.path.join(os.path.dirname(__file__), 'pre-processing'))
from embedding import embeddings

from langchain_core.documents import Document

# == Load and clean PDF text ==
text = load_pdf(r"C:\Users\MSI\Desktop\Uttor-AI\BackEnd\rag\data\HSC26-Bangla1st-Paper.pdf")
print("Extracted text length:", len(text))
# print(text[19]["text"])

# Clean text
for i in range(len(text)):
    text[i]["text"] = clean_text(text[i]["text"])

# Convert to Document objects for semantic splitting
documents = [Document(page_content=entry["text"], metadata=entry["metadata"]) for entry in text]

# Semantic splitting
semantic_chunks = semantic_splitter(documents)
print(f"Number of semantic chunks created: {len(semantic_chunks)} and type: {type(semantic_chunks)}\n")

# Embedding
embedding_model = embeddings(semantic_chunks)