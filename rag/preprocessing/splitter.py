from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def semantic_splitter(data):
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY"),
        model='text-embedding-3-large')

    semantic_splitter = SemanticChunker(
        embeddings=embeddings,
        breakpoint_threshold_type="gradient",
        breakpoint_threshold_amount=0.8
    )
    chunks = semantic_splitter.split_documents(data)
    return chunks