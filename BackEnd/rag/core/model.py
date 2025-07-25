from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

api_key = os.getenv("OPENAI_API_KEY")

def model(): 
    prompt = ChatPromptTemplate.from_template("""
        ধরুন আপনি একজন স্কুলের অধ্যাপক, যিনি সবসময় বই থেকে উত্তর দিতে পছন্দ করেন। আপনার উত্তরগুলো অবশ্যই নির্ভুল ও সঠিক হতে হবে এবং শুধুমাত্র প্রদত্ত প্রসঙ্গের উপর ভিত্তি করে দিতে হবে। উত্তরটি বাংলায় দিন।
        যদি প্রসঙ্গ থেকে উত্তর জানা না যায়, তাহলে বলুন আপনি জানেন না। \n
        context: {context}\n
        question: {question}
    """)
    

    llm = ChatOpenAI(
        model="gpt-4-turbo", 
        api_key=api_key, 
        temperature=0)
    
    return prompt, llm
