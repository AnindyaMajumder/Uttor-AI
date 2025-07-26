from .core.retriever import retriever
from .core.model import model

from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser 

def get_answer(query: str, history: list = None):
    # Get retriever results using the query
    retriever_results = retriever(query)
    
    # Extract page_content from matches to create context
    context_pieces = []
    for match in retriever_results.get('matches', []):
        page_content = match.get('metadata', {}).get('page_content', '')
        if page_content:
            context_pieces.append(page_content)
    
    # Join all context pieces into a single context string
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