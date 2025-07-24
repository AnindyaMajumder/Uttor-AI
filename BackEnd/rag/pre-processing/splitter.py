import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings 
from langchain_experimental.text_splitter import SemanticChunker 
from langchain_core.documents import Document

api_key = os.getenv('OPENAI_API_KEY')
def semantic_splitter(data):
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))
    embeddings = OpenAIEmbeddings(api_key=api_key, model='text-embedding-3-large') 

    semantic_splitter = SemanticChunker( 
        embeddings=embeddings,  
        breakpoint_threshold_type="gradient", 
        breakpoint_threshold_amount=0.8  
    ) 
    chunks = semantic_splitter.split_documents(data) 
    return chunks