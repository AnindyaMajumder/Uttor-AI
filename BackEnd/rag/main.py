import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pre-processing'))

from splitter import semantic_splitter
from loader import load_pdf
from clean_text import clean_text

sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
from embedding import embeddings
from retriever import retriever

from langchain_core.documents import Document

# == Load and clean PDF text ==
text = load_pdf(r"C:\Users\MSI\Desktop\Uttor-AI\BackEnd\rag\data\HSC26-Bangla1st-Paper.pdf")
print("Extracted text length:", len(text))

# Clean text
for i in range(len(text)):
    text[i]["text"] = clean_text(text[i]["text"])

# Convert to Document objects for semantic splitting
documents = [Document(page_content=entry["text"], metadata=entry["metadata"]) for entry in text]

# Semantic splitting
semantic_chunks = semantic_splitter(documents)
print(f"Number of semantic chunks created: {len(semantic_chunks)} and type: {type(semantic_chunks)}\n")

# Convert semantic chunks to strings
chunk_texts = [chunk.page_content for chunk in semantic_chunks]

# Embedding and upsert to Pinecone using core/embedding.py
vectorstore = embeddings(chunk_texts)

# Query
Query = "কষ্টি পাথর নিয়ে কে বসে ছিল?" # শ্যাকরা
semantic_results = retriever(query=Query, vectorstore=vectorstore)
print(f"Results found: {semantic_results}\n")