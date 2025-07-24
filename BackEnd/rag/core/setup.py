from dotenv import load_dotenv
import os
from pinecone import Pinecone

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env'))

def pinecone_setup():
    
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    index_name = "bangla"
    index = pc.Index(index_name)

    if not pc.has_index(index_name):
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "chunk_text"}
            }
        )
    
    return index

print(pinecone_setup().describe_index_stats())