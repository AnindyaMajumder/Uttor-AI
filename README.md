# 🤖 Uttor-AI

> An intelligent Bengali Q&A system powered by Retrieval-Augmented Generation (RAG), specifically designed for Higher Secondary Bangla.

## � Table of Contents

- [✨ Key Features](#-key-features)
- [🚀 Quick Start](#-quick-start)
- [💬 Quesion & Answer regarding the project](#-A-few-Q&-A-regarding-the-project)
- [🤔 Design Choices & Rationale](#-design-choices--rationale)
- [📚 API Documentation](#-api-documentation)
- [🏗️ Project Structure](#️-project-structure)

## ✨ Key Features

- 🎯 **Subject-Specific Expertise**: Focused on HSC Bangla 1st Paper content using **pytesseract** and **pdf2image** for document processing
- 🧠 **Smart Processing**: Bengali text processing with **bnlp_toolkit** and **NLTK**
- 🔍 **Intelligent Retrieval**: Advanced RAG system with **Pinecone** vector database and **BAAI/bge-m3** embeddings for accurate context matching
- 🌐 **Multilingual Input**: Accepts questions in any language 
- 📚 **Book-First Approach**: Prioritizes answers from provided pdf
- 🎭 **Teacher Persona**: Responds like a knowledgeable school teacher powered by **OpenAI GPT-4.1**
- ⚡ **Fast API**: RESTful API built with **FastAPI** for easy integration

## 🚀 Quick Start

### Prerequisites

- Python 3.10.11 (recommended)
- OpenAI API key
- Pinecone API key
- Tesseract OCR (for PDF text extraction)

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
   OPENAI_API_KEY=your_openai_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   ```

6. **Run the application**
   ```bash
      uvicorn app:app --host 127.0.0.1 --port 8000
   ```

   The API will be available at `http://127.0.0.1:8000`

##  Sample Queries and Outputs

### Bengali Queries

**Query (Bengali):**
```
রবীন্দ্রনাথ ঠাকুরের 'সোনার তরী' কবিতার মূল বিষয়বস্তু কী?
```

**Response:**
```
রবীন্দ্রনাথ ঠাকুরের 'সোনার তরী' কবিতাটি মূলত কবির জীবনের ক্ষণস্থায়িত্ব ও শিল্পের স্থায়িত্বের দ্বন্দ্ব নিয়ে রচিত। কবিতায় দেখা যায় যে, কৃষক তার সোনালি ধানের ফসল নিয়ে মাঝির কাছে যায়, কিন্তু মাঝি শুধু ফসল নিয়ে যায়, কৃষককে নিয়ে যায় না। এখানে ফসল হলো কবির সৃষ্টিকর্ম আর কৃষক হলো কবি নিজে। কবিতার মূল বার্তা হলো শিল্প অমর, কিন্তু শিল্পী মরণশীল।
```

**Query (Bengali):**
```
'আমার পথ' প্রবন্ধে কাজী নজরুল ইসলাম কী বার্তা দিয়েছেন?
```

**Response:**
```
'আমার পথ' প্রবন্ধে কাজী নজরুল ইসলাম মানুষের ব্যক্তিত্ব ও স্বাধীনতার কথা বলেছেন। তিনি বলেছেন যে, প্রত্যেক মানুষের নিজস্ব পথ আছে এবং সে পথে চলতে গেলে কারও অনুসরণ করার প্রয়োজন নেই। তিনি ধর্মীয় গোঁড়ামি, সামাজিক কুসংস্কার ও প্রথাগত বিধি-নিষেধের বিরুদ্ধে প্রতিবাদ করেছেন। নজরুলের মতে, সত্যিকারের মানুষ হতে হলে নিজের বিবেক ও যুক্তি দিয়ে পথ বেছে নিতে হবে।
```

### English Queries (Bengali Responses)

**Query (English):**
```
What is the theme of Rabindranath Tagore's "Gitanjali"?
```

**Response:**
```
রবীন্দ্রনাথ ঠাকুরের 'গীতাঞ্জলি' কাব্যগ্রন্থের মূল বিষয়বস্তু হলো ভক্তি ও আধ্যাত্মিকতা। এই কাব্যগ্রন্থে কবি ঈশ্বরের প্রতি তাঁর গভীর ভালোবাসা ও নিবেদনের কথা ব্যক্ত করেছেন। গীতাঞ্জলির কবিতাগুলোতে মানুষ ও স্রষ্টার মধ্যকার সম্পর্ক, জীবনের অর্থ, মৃত্যুচেতনা এবং পরমপ্রেমের বিষয়গুলো স্থান পেয়েছে। এই কাব্যগ্রন্থের জন্য রবীন্দ্রনাথ ১৯১৩ সালে নোবেল পুরস্কার লাভ করেন।
```

## 🤔 A few Q&A regarding the project

#### 1. What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?
I employed pdf2image to convert each PDF page into a high‑resolution image, followed by pytesseract with the Bengali trained data to perform optical character recognition. This approach was necessary because, despite the fonts being selectable, they were not mapped to Unicode code points. Preprocessing steps—such as binarisation and noise reduction—were applied to improve the clarity of the scanned text and thereby enhance recognition accuracy

#### 2. What chunking strategy did you choose (e.g. paragraph-based, sentence-based, character limit)? Why do you think it works well for semantic retrieval?
I opted for a sentence‑based segmentation method. Firstly, the raw text was cleaned using the bnlp toolkit to remove artefacts and standardise punctuation. Subsequently, I split on sentence boundaries detected by the semantic splitter using OPENAI's ```text-embedding-3-large``` with breakpoint thresold amount as `0.8`, rather than imposing arbitrary character limits. This yields self‑contained, semantically coherent fragments that are well suited to vector‑based similarity search. For every page it will generate numerous embeddings based on the context. I excluded pages composed primarily of MCQs, since these often lack explanatory context and could degrade retrieval precision.

#### 3. What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?
For vectorisation I selected the ```BGE‑m3``` embedding model, owing to its robust support for Bangla script and its capacity to process extended passages (up to 8000 tokens). The model generates dense numerical representations that capture the semantic relationships between words and phrases, facilitating the retrieval of passages that best match a given query.

#### 4. How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?
Queries and document fragments are both encoded with the ```BGE‑m3``` model, after which cosine similarity is computed between the query vector and each fragment vector. All vectors are stored in a Pinecone index for efficient approximate nearest‑neighbour search using cosine similarity. 

#### 5. How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?
By using the same embedding model for queries and document fragments, the system ensures that both are represented in a common semantic space. A similarity threshold is applied: if the highest cosine score falls below a predetermined cutoff, the system informs the user that it cannot locate a relevant passage and suggests rephrasing or providing additional detail.

#### 6. Do the results seem relevant? If not, what might improve them (e.g. better chunking, better embedding model, larger document)?
Overall, the retrieved passages align pretty much well with user queries. Introducing post‑OCR cleaning such as common misrecognition corrections for specific Bangla characters to reduce OCR errors. Also, labeling a small subset of query–passage pairs manually and fine‑tune a cross‑encoder reranker, thereby improving precision on top results.

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

## 🏗️ Project Structure

```
Uttor-AI/
├── app.py                 # FastAPI application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # Project license
└── rag/                  # RAG implementation
    ├── chain.py          # Main RAG chain logic
    ├── vectorstore.py    # Vector store operations
    ├── core/             # Core RAG components
    │   ├── embeddings.py # Embedding models
    │   ├── model.py      # Language model setup
    │   ├── retriever.py  # Document retrieval logic
    │   └── setup.py      # Configuration setup
    ├── data/             # Educational content
    │   └── HSC26-Bangla1st-Paper.pdf
    └── preprocessing/    # Data processing
        ├── clean_text.py # Text cleaning utilities
        ├── loader.py     # Document loaders
        └── splitter.py   # Text chunking
```