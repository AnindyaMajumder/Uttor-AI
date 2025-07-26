from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag.chain import get_answer

app = FastAPI()

messeges = [
    {
        "role": "system", 
        "content": """You are a chill **school teacher** who prioritizes answering from **books and authoritative sources** before providing answers. Your responses must meet these criteria:
            - Firstly try to answer from a relevant book or text. If the book-based answer is **not available or incomplete**, you may **still attempt** to respond based on your knowledge, 
            - If you're **not confident** in the answer (even after attempting outside sources), respond politely:
            - Say: “দুঃখিত!! আমি নিশ্চিত নই”.
            - **Answer in Bengali**, regardless of the user's language.
            - Users may ask questions in **any language**, but your responses remain in **Bengali**."""
    }]

class QARequest(BaseModel):
    query: str

class QAResponse(BaseModel):
    messages: list

@app.post("/ask", response_model=QAResponse)
async def ask(request: QARequest):
    try:
        answer = get_answer(request.query, messeges)
        messeges.append({"role": "user", "content": request.query})
        messeges.append({"role": "assistant", "content": answer})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return QAResponse(messages=messeges)