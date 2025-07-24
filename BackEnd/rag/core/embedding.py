import os
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore  

from typing import List

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# EMBEDDING_DIMENSION = 1536

def embeddings(text: List[str]):
    embeddings = OpenAIEmbeddings(  
        model="text-embedding-3-large",  
        openai_api_key=OPENAI_API_KEY,
    )
    
    vectorstore = PineconeVectorStore("bangla", embeddings, text)
    return vectorstore 