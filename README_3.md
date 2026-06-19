# 🔍 DocuQuery — RAG Pipeline Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.2-green?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red?style=flat-square&logo=streamlit)
![FAISS](https://img.shields.io/badge/FAISS-Meta-blue?style=flat-square)
![LLaMA3](https://img.shields.io/badge/LLaMA3-Groq-orange?style=flat-square)

> Upload any PDF or text document and ask questions about it in plain English.  
> Powered by Retrieval-Augmented Generation (RAG) — LangChain + FAISS + HuggingFace + Groq LLaMA3.

🚀 **[Live Demo →](https://your-app-name.streamlit.app)** *(add your Streamlit link here after deployment)*

---

## 🧠 What is RAG?

Standard LLMs only know what they were trained on. RAG gives them access to **your documents** at query time.

```
📄 Your Document
      ↓
   CHUNK IT          → Split into ~500 char paragraphs
      ↓
   EMBED IT          → Convert each chunk to a vector (384 numbers)
      ↓
   STORE IN FAISS    → Meta's lightning-fast vector search database
      ↓
❓ User asks question
      ↓
   RETRIEVE          → Find 4 most semantically similar chunks
      ↓
   ASK LLM           → Send question + those chunks to LLaMA3
      ↓
🤖 Accurate, grounded answer
```

---

## 🛠️ Tech Stack

| Component | Tool | Why |
|-----------|------|-----|
| **Framework** | LangChain | Connects all RAG components cleanly |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` | Free, fast, local — no API key needed |
| **Vector Store** | FAISS (Facebook AI) | Millisecond similarity search |
| **LLM** | LLaMA3-8B via Groq | Free API, extremely fast inference |
| **UI** | Streamlit | Python → web app with zero HTML/CSS |

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/madhura-23/rag-pipeline
cd rag-pipeline

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Get free Groq API key at https://console.groq.com

# 5. Run the app
streamlit run app.py
```

---

## 📁 Project Structure

```
rag-pipeline/
│
├── app.py           # Streamlit UI — handles uploads, questions, display
├── rag_engine.py    # RAG logic — load, chunk, embed, retrieve, answer
├── requirements.txt # All Python dependencies
├── .gitignore       # Files to exclude from git
└── README.md        # You are here
```

---

## 💡 Key Concepts (Interview-Ready)

**Chunking** — Documents are split into ~500 character pieces with 50-char overlap so no meaning is lost at boundaries.

**Embeddings** — `all-MiniLM-L6-v2` converts text into 384-dimensional vectors. Semantically similar sentences produce nearby vectors.

**FAISS** — Stores all vectors and performs approximate nearest-neighbour search in O(log n) time.

**Retrieval** — User question is embedded, top-k=4 most similar chunks are retrieved via cosine similarity.

**Augmented Generation** — Retrieved chunks are injected into the LLM prompt as context, grounding the answer in your document.

---

## 👩‍💻 About

**Madhura Bhat** — B.Tech AI & Data Science | ML · NLP · GenAI · Full-Stack

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/madhura-bhatt23)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/madhura-23)

---

<p align="center">⭐ Star this repo if you found it useful!</p>
