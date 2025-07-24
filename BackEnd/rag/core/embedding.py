import os
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore  
from pinecone import Pinecone

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# EMBEDDING_DIMENSION = 1536

def embeddings(texts):
    """
    Accepts a list of texts, creates embeddings, and upserts to Pinecone.
    Returns the PineconeVectorStore for retrieval.
    """
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=OPENAI_API_KEY,
    )

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index("bangla")

    # Upsert all texts to Pinecone
    vectorstore = PineconeVectorStore(index, embedding_model, texts)
    return vectorstore