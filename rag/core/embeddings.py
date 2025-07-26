from transformers import AutoTokenizer, AutoModel
import torch
from pinecone import Pinecone
from pinecone import ServerlessSpec
from tqdm import tqdm
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "bangla"

# Load the BAAI/bge-m3 model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
model = AutoModel.from_pretrained("BAAI/bge-m3")

index = pc.Index(index_name)

def embeddings(documents):
    upsert_data = []

    for doc in tqdm(documents):
        text = doc.page_content
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

        # Get embeddings (mean of the last hidden state)
        with torch.no_grad():
            outputs = model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

        # Upsert the data to Pinecone (embedding + metadata)
        upsert_data.append((f"doc_{hash(text)}", embeddings.tolist(), {"page_content": text}))

    # Upsert all the documents into Pinecone
    index.upsert(vectors=upsert_data)
    
    return index.describe_index_stats()