import os
import openai
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore  
from pinecone import Pinecone

from transformers import AutoTokenizer, AutoModel
import torch
from pinecone import ServerlessSpec
from tqdm import tqdm
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


pc = Pinecone(api_key=PINECONE_API_KEY)
# Require index name from environment variable
INDEX_NAME = os.getenv("INDEX_NAME")
if not INDEX_NAME:
    raise ValueError("INDEX_NAME environment variable must be set in .env file.")
index = pc.Index(INDEX_NAME)

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
model = AutoModel.from_pretrained("BAAI/bge-m3")

def retriever(query_text: str = "রসনচৌকি' শব্দের অর্থ কী?"):
    # Tokenize and generate the embedding for the query text
    query_inputs = tokenizer(query_text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        query_outputs = model(**query_inputs)

    # Extract the embeddings (mean of the last hidden state)
    query_embeddings = query_outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

    # Perform similarity search on Pinecone index
    results = index.query(vector=query_embeddings.tolist(), top_k=10, include_metadata=True)

    return results