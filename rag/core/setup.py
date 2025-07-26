from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env'))


def pinecone_setup():
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    # Require index name from environment variable
    index_name = os.getenv("INDEX_NAME")
    if not index_name:
        raise ValueError("INDEX_NAME environment variable must be set in .env file.")

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=1024,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
        
    index = pc.Index(index_name)
    
    return index

print(pinecone_setup().describe_index_stats())