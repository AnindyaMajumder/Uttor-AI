from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env'))

qdrant_url = os.getenv('QDRANT_URL')
qdrant_api_key = os.getenv('QDRANT_API_KEY')

qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key,
)

print(qdrant_client.get_collections())