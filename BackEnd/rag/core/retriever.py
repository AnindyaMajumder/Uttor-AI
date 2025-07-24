
def retriever(query: str, k: int = 3, vectorstore=None):
    return vectorstore.similarity_search(  
        query,  # search query  
        k=3  # 3 most relevant docs  
    )  

# Response:
# [Document(page_content='Benito Amilcare Andrea Mussolini KSMOM GCTE (29 July 1883 – 28 April 1945) was an Italian politician and journalist...', metadata={'chunk': 0.0, 'source': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini', 'title': 'Benito Mussolini', 'wiki-id': '6754'}),  
# Document(page_content='Fascism as practiced by Mussolini\nMussolini\'s form of Fascism, "Italian Fascism"- unlike Nazism, the racist ideology...', metadata={'chunk': 1.0, 'source': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini', 'title': 'Benito Mussolini', 'wiki-id': '6754'}),  
# Document(page_content='Veneto was made part of Italy in 1866 after a war with Austria. Italian soldiers won Latium in 1870. That was when...', metadata={'chunk': 5.0, 'source': 'https://simple.wikipedia.org/wiki/Italy', 'title': 'Italy', 'wiki-id': '363'})]