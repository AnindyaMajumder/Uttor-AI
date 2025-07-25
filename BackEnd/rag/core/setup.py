from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env'))

def pinecone_setup():
    
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    index_name = "bangla"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=3072,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
        
    index = pc.Index(index_name)
    
    return index

print(pinecone_setup().describe_index_stats())