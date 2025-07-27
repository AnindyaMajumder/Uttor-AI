# 🤖 Uttor-AI

> An intelligent Bengali Q&A system powered by Retrieval-Augmented Generation (RAG), specifically designed for Higher Secondary Bangla.

## � Table of Contents

- [✨ Key Features](#-key-features)
- [🚀 Quick Start](#-quick-start)
- [🧾 Sample Queries and Outputs](#-sample-queries-and-outputs)
- [💬 Question & Answer regarding the project](#-a-few-qa-regarding-the-project)
- [📚 API Documentation](#-api-documentation)
- [🧪 Testing with Postman](#-testing-with-postman)
- [🏗️ Project Structure](#️-project-structure)

## ✨ Key Features

- 🎯 **Subject-Specific Expertise**: Focused on HSC Bangla 1st Paper content
  - 🧠 **Smart Processing**: Bengali text processing with **bnlp_toolkit** and semantic chunking using text-embedding-3-large
- 🔍 **Intelligent Retrieval**: Advanced RAG system with **Pinecone** vector database and **BAAI/bge-m3** embeddings for accurate context matching
- 🌐 **Multilingual Input**: Accepts questions in any language 
- 📚 **Book-First Approach**: Prioritizes answers from provided pdf
- 🎭 **Teacher Persona**: Responds like a knowledgeable school teacher powered by **OpenAI GPT-4.1**
- ⚡ **RESTful API**: RESTful API built with **FastAPI** for easy integration

## 🚀 Quick Start

### Prerequisites

- Python 3.10.11 (recommended)
- OpenAI API key
- Pinecone API key
- Tesseract OCR (for PDF text extraction)
- Postman (for API testing)

### Installation

1. **Install Tesseract OCR**
   
   **On Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev
   ```
   
   **On Windows:**
   - Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install and add Tesseract to your PATH environment variable

2. **Clone the repository**
   ```bash
   git clone https://github.com/AnindyaMajumder/Uttor-AI.git
   cd Uttor-AI
   ```

3. **Create a virtual environment**
   
   **Using venv (recommended):**
   ```bash
   python -m venv .venv
   ```
   or
   ```bash
   py -3.10 -m venv .venv
   ```
   
   **Activate virtual environment:**
   ```bash
   # On Linux/Mac:
   source .venv/bin/activate
   
   # On Windows (Command Prompt):
   .venv\Scripts\activate
   
   # On Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   ```

4. **Install dependencies**
   1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=<your_openai_api_key>
   PINECONE_API_KEY=<your_pinecone_api_key>
   INDEX_NAME=<your_index_name>
   ```

6. **Vectordb (Pinecone) Setup**
  The script `rag/vectorstore.py` is responsible for generating embeddings from your documents and storing them in the Pinecone vector database. Make sure your database and index is set up before running the main application.
  After setting up the database and running the embedding process, you can execute `app.py` to start the API server.

1. **Run the application**
   ```bash
   uvicorn app:app --host 127.0.0.1 --port 8000
   ```

   The API will be available at `http://127.0.0.1:8000`

2. **Test on Postman**
   
   Enter with `POST` request at -> `http://127.0.0.1:8000` and
   send `JSON` request as `raw body` like 
   ```
   {
     "query": "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"
   }
   ```
   Another `JSON` file with short-term memory will return as resonse.

## 🧾 Sample Queries and Outputs

**Query (English):**
```
Hi
```

**Response:**
```
হ্যালো! আপনি কী জানতে চান? আপনার প্রশ্নটি করুন, আমি বই থেকে উত্তর দেওয়ার চেষ্টা করব।
```

**Query (Bengali):**
```
কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?
```

**Response:**
```
বই অনুযায়ী, 'অপরিচিতা' গল্পে অনুপম তার মামাকে "ভাগ্য দেবতা" বলে উল্লেখ করেছে।
```

**Query (Bangla):**
```
বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?
```

**Response:**
```
বই অনুযায়ী, বিয়ের সময় কল্যাণীর প্রকৃত বয়স ছিল ১৫ বছর।
```

**Query (English):**
```
Who is the author of the story?
```
**Response:**
```
বই অনুযায়ী, 'অপরিচিতা' গল্পের রচয়িতা রবীন্দ্রনাথ ঠাকুর।
```

## 🤔 A few Q&A regarding the project

#### 1. What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?
I used `pdf2image` to convert each PDF page into an image, followed by `pytesseract` with Bengali-trained data to perform optical character recognition. This approach was necessary because, despite the fonts being selectable, they were not mapped to Unicode code points. Preprocessing steps, such as binarisation and noise reduction—were applied to improve the clarity of the scanned text and thereby enhance recognition accuracy

#### 2. What chunking strategy did you choose (e.g. paragraph-based, sentence-based, character limit)? Why do you think it works well for semantic retrieval?
I opted for a sentence‑based segmentation method. Firstly, the raw text was cleaned using the `BNLP toolkit` to remove artefacts and standardise punctuation. Subsequently, I split on sentence boundaries detected by the semantic splitter using OPENAI's ```text-embedding-3-large``` with a breakpoint threshold of `0.8`, rather than imposing arbitrary character limits. This yields self‑contained, semantically coherent fragments that are well suited to vector‑based similarity search. For every page, it will generate numerous embeddings based on the context. I excluded pages composed primarily of MCQs, since these often lack explanatory context and could degrade retrieval precision (work as noise for this case).

#### 3. What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?
For vectorisation, I selected the ```BGE‑m3``` embedding model, owing to its robust support for Bangla script and its capacity to process extended passages (up to 8000 tokens). The model generates dense numerical representations that capture the semantic relationships between words and phrases, facilitating the retrieval of passages that best match a given query.

#### 4. How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?
Queries and document fragments are both encoded with the ```BGE‑m3``` model, after which cosine similarity is computed between the query vector and each fragment vector. All vectors are stored in a Pinecone index (in cloud) for efficient approximate nearest‑neighbour search using cosine similarity. Cosine similarity measures the angle between two normalised vectors, making it insensitive to text length and well-suited to comparing semantic content.

#### 5. How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?
By using the same embedding model for queries and document fragments, the system ensures that both are represented in a common semantic space. A similarity threshold is applied if the highest cosine score falls below a predetermined cutoff; the system informs the user that it cannot locate a relevant passage and suggests rephrasing or providing additional detail.

#### 6. Do the results seem relevant? If not, what might improve them (e.g. better chunking, better embedding model, larger document)?
Overall, the retrieved passages align pretty well with user queries. Mapping the font with unicode would be great for robust text extraction. Introducing post‑OCR cleaning, such as common misrecognition corrections for specific Bangla characters to reduce OCR errors. Also, labelling a small subset of query–passage pairs manually and fine-tuning a cross‑encoder reranker, thereby improving precision on top results.

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### POST `/ask`

**Request Body:**
```json
{
  "query": "string"
}
```

**Response:**
```json
{
  "messages": [
    {
      "role": "system",
      "content": "System prompt..."
    },
    {
      "role": "user", 
      "content": "User question ..."
    },
    {
      "role": "assistant",
      "content": "AI response in Bengali ..."
    }
  ]
}
```

**Example Response**
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a chill **school teacher** who prioritizes answering from **books and authoritative sources** before providing answers. Your responses must meet these criteria:\n- Firstly try to answer from a relevant book or text. If the book-based answer is **not available or incomplete**, you may **still attempt** to respond based on your knowledge.\n- If you're **not confident** in the answer (even after attempting outside sources), respond politely:\n  - Say: “দুঃখিত!! আমি নিশ্চিত নই”.\n- **Answer in Bengali**, regardless of the user's language.\n- Users may ask questions in **any language**, but your responses remain in **Bengali**."
    },
    {
      "role": "user",
      "content": "Hi!"
    },
    {
      "role": "assistant",
      "content": "হ্যালো! আপনি কী জানতে চান? আপনার প্রশ্নটি করুন, আমি বই থেকে উত্তর দেওয়ার চেষ্টা করব।"
    },
    {
      "role": "user",
      "content": "কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?"
    },
    {
      "role": "assistant",
      "content": "বই অনুযায়ী, 'অপরিচিতা' গল্পে অনুপম তার মামাকে \"ভাগ্য দেবতা\" বলে উল্লেখ করেছে।"
    },
    {
      "role": "user",
      "content": "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"
    },
    {
      "role": "assistant",
      "content": "বই অনুযায়ী, বিয়ের সময় কল্যাণীর প্রকৃত বয়স ছিল ১৫ বছর।"
    },
    {
      "role": "user",
      "content": "Who is the author of the story?"
    },
    {
      "role": "assistant",
      "content": "বই অনুযায়ী, 'অপরিচিতা' গল্পের রচয়িতা রবীন্দ্রনাথ ঠাকুর।"
    },
    {
      "role": "user",
      "content": "Summarise our conversation"
    },
    {
      "role": "assistant",
      "content": "আপনার ও আমার কথোপকথনের সংক্ষিপ্তসার নিচে দেওয়া হলো—\n\n১. আপনি প্রথমে জানতে চেয়েছিলেন, “কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?”\nউত্তরে আমি বই থেকে জানাই, ‘অপরিচিতা’ গল্পে অনুপম তার মামাকে “ভাগ্য দেবতা” বলে উল্লেখ করেছে।\n\n২. এরপর আপনি জানতে চেয়েছিলেন, “বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?”\nআমি বই থেকে উত্তর দিই, বিয়ের সময় কল্যাণীর প্রকৃত বয়স ছিল ১৫ বছর।\n\n৩. এরপর আপনি ইংরেজিতে জানতে চেয়েছিলেন, “Who is the author of the story?”\nআমি বই থেকে উত্তর দিই, ‘অপরিচিতা’ গল্পের রচয়িতা রবীন্দ্রনাথ ঠাকুর।\n\nএই ছিল আমাদের সংক্ষিপ্ত কথোপকথন। আমি সব প্রশ্নের উত্তর বই থেকে দেওয়ার চেষ্টা করেছি।"
    }
  ]
}
```

## 🧪 Testing with Postman

### Quick Setup
1. Import the `UttorAI_API_testing.postman_collection` file into Postman
2. Start the server: `uvicorn app:app --host 127.0.0.1 --port 8000`
3. Send requests to test the API

### Manual Setup
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/ask`
- **Headers**: `Content-Type: application/json`
- **Body**:
```json
{
  "query": "কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?"
}
```

### Test Cases
- Bengali queries: `"বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"`
- English queries: `"Who is the author of the story?"`
- Greetings: `"Hi"`


## 🏗️ Project Structure

```
Uttor-AI/
├── app.py                 # FastAPI application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── UttorAI_API_testing.postman_collection # Postman API testing
├── LICENSE               # Project license
└── rag/                  # RAG implementation
    ├── chain.py          # Main RAG chain logic
    ├── vectorstore.py    # Vector store operations
    ├── core/             # Core RAG components
    │   ├── embeddings.py # Embedding models
    │   ├── model.py      # Language model setup
    │   ├── retriever.py  # Document retrieval logic
    │   └── setup.py      # Database Index status check
    ├── data/             # Dataset corpus for context 
    │   └── HSC26-Bangla1st-Paper.pdf
    └── preprocessing/    # Data processing
        ├── clean_text.py # Text cleaning utilities
        ├── loader.py     # Document loaders
        └── splitter.py   # Text chunking with semantic splitter
```
