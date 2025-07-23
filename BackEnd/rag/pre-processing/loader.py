#from langchain_community.document_loaders import PyMuPDFLoader
import pymupdf

def load_pdf(file_path: str = r"C:\Users\Anindya Majumder\Documents\Uttor-AI\BackEnd\rag\data\HSC26-Bangla1st-Paper.pdf"):
    doc = pymupdf.open(file_path) # open a document

    text = []
    for page in doc: # iterate the document pages
        text.append(page.get_text())
        
    return text

# def load_pdf_with_metadata(file_path: str = r"C:\Users\Anindya Majumder\Documents\Uttor-AI\BackEnd\rag\data\HSC26-Bangla1st-Paper.pdf"):
#     """Returns both text and metadata for more advanced processing"""
#     loader = PyMuPDFLoader(file_path)
#     documents = loader.load()
    
#     processed_docs = []
#     for doc in documents:
#         processed_docs.append({
#             'text': doc.page_content,
#             'metadata': doc.metadata  # Contains page number, source file, etc.
#         })
    
#     return processed_docs