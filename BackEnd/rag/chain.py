from core.retriever import retriever
from core.model import model

from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser 

def get_answer(query: str):
    retriever_init = retriever()
    ans = retriever_init.invoke(query)
    
    prompt, llm = model()
    chain = (
        RunnablePassthrough()
        | prompt
        | llm
        | StrOutputParser()
    )
    inputs = {"context": ans, "question": query}
    result = chain.invoke(inputs)
    return result

print(get_answer("কষ্টি পাথর নিয়ে কে বসে ছিল?")) # শ্যাকরা