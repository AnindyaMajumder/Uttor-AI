from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def model(): 
    prompt = ChatPromptTemplate.from_template("""
        ধরুন আপনি একজন স্কুলের শিক্ষক, যিনি সবসময় বই থেকে উত্তর দিতে পছন্দ করেন। আপনার উত্তরগুলো অবশ্যই নির্ভুল ও সঠিক হতে হবে। উত্তরটি বাংলায় দিন।
        যদি প্রসঙ্গ থেকে উত্তর জানা না যায়, তাহলে বলুন আপনি জানেন না। \n
        Chat History: {history}\n
        Book context: {context}\n
        Question: {question}
    """)
    

    llm = ChatOpenAI(
        model="gpt-4.1", 
        api_key=api_key, 
        temperature=0.1)
    
    return prompt, llm
