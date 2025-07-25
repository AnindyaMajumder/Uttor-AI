from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document

# def load_pdf(file_path: str = r"C:\Users\Anindya Majumder\Documents\Uttor-AI\BackEnd\rag\data\HSC26-Bangla1st-Paper.pdf", as_documents: bool = True):
#     doc = pymupdf.open(file_path)
#     pages = []
#     for i, page in enumerate(doc):
#         # Pages to remove: 1, 19, 22-40 (MCQ questions considered as noise)
#         if i in [1, 19] or 22 <= i <= 40:
#             continue
#         text = page.get_text()
#         if as_documents:
#             pages.append(Document(page_content=text, metadata={"page": i}))
#         else:
#             pages.append(text)
#     doc.close()
#     return pages

def load_pdf(file_path: str = r"C:\Users\Anindya Majumder\Documents\Uttor-AI\BackEnd\rag\data\HSC26-Bangla1st-Paper.pdf"):
    """Returns both text and metadata for more advanced processing, skipping pages 1, 19, 22-40 (0-based)"""
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()

    # Remove pages 1, 19, 22-40 (0-based)
    filtered_docs = []
    for doc in documents:
        page_num = doc.metadata.get('page', None)
        if page_num is not None and (page_num in [1, 19] or 22 <= page_num <= 40):
            continue
        filtered_docs.append({
            'text': doc.page_content,
            'metadata': doc.metadata
        })
    return filtered_docs

texts = load_pdf()
with open("output.txt", "w", encoding="utf-8") as f:
    for item in texts:
        f.write(item['text'] + "\n")