from .core.retriever import retriever
from .core.model import model

from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser 
import re

def get_answer(query: str, history: list = None):
    Wh_words = ["কি", "কী", "কিসে", "কিসের", "কেন", "ক্যানো", "কে", "কারা", "কার", "কাকে", "কাদের", "কাদেরকে", "কোন", "কোনটা", "কোনটি", "কোনগুলো", "কোনগুলা", "কোনদিক", "কিভাবে", "কেমন করে", "কীভাবে", "কেমন", "কী উপায়ে", "কখন", "কখনো", "কখন থেকে", "কখন পর্যন্ত", "কবে", "কোথায়", "কোথা থেকে", "কোথা দিয়ে", "কোথাকার", "কত", "কতো", "কতগুলো", "কটি", "ক’টি", "কজন", "ক’জন", "কতবার", "কতদিন", "কদিন", "কতখানি", "কতদূর", "কতটা", "কতক্ষণ", "কার", "কারটা", "কারোর", "কাহার", "কাদের", "কাকে", "কাহাকে", "কাদেরকে", "কী দিয়ে", "কিসে", "কী মাধ্যমে", "কোনভাবে", "কাহাকে", "কাহার", "কাহারা", "কাহাদিগকে", "কাহাদের", "কাহারও", "কারও", "কাহাকে", "কি করে", "?"]
    # Split query into words and remove WH words
    words = query.split()
    cleaned_query = [w for w in words if w not in Wh_words]
    cleaned_query = ' '.join(cleaned_query).strip()
    
    # Get retriever results using the query
    retriever_results = retriever(cleaned_query)
    
    # Extract page_content from matches to create context
    context_pieces = []
    for match in retriever_results.get('matches', []):
        page_content = match.get('metadata', {}).get('page_content', '')
        if page_content:
            context_pieces.append(page_content)
    
    context = '\n'.join(context_pieces)
    
    prompt, llm = model()
    chain = (
        RunnablePassthrough()
        | prompt
        | llm
        | StrOutputParser()
    )
    inputs = {"context": context, "question": query, "history": history or []}
    result = chain.invoke(inputs)
    return result

# print(get_answer("কষ্টি পাথর নিয়ে কে বসে ছিল?")) # শ্যাকরা