<div align="center">

<!-- ANIMATED HEADER BANNER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=C0392B&height=200&section=header&text=DocuQuery&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=RAG-Powered%20Document%20Intelligence&descAlignY=58&descSize=22&descColor=ffcccc"/>

<!-- BADGES ROW 1 -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-0.2-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/FAISS-Meta-0668E1?style=for-the-badge&logo=meta&logoColor=white"/>
</p>

<!-- BADGES ROW 2 -->
<p>
  <img src="https://img.shields.io/badge/LLaMA3-Groq-F55036?style=for-the-badge&logo=groq&logoColor=white"/>
  <img src="https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge"/>
</p>

<br/>

<!-- LIVE DEMO BUTTON -->
<a href="https://rag-pipeline-6zgewusfjx9multdcbcani.streamlit.app">
  <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Click%20Here-C0392B?style=for-the-badge"/>
</a>

<br/><br/>

> **Upload any PDF. Ask anything. Get precise answers — powered by RAG.**  
> No hallucinations. No guessing. Only answers grounded in your document.

---

</div>

## ⚡ What is DocuQuery?

Standard LLMs don't know your private documents. **DocuQuery solves this with RAG** — it reads your document, understands it, and answers questions about it with pinpoint accuracy.

Upload your resume, a research paper, a legal contract, or any PDF — and have a conversation with it.

---

## 🧠 How RAG Works (The Architecture)

```
╔══════════════════════════════════════════════════════════════════╗
║                     RAG PIPELINE FLOW                            ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   📄 PDF/TXT Upload                                              ║
║         │                                                        ║
║         ▼                                                        ║
║   ✂️  CHUNK  →  Split into 500-char pieces (50-char overlap)     ║
║         │                                                        ║
║         ▼                                                        ║
║   🔢  EMBED  →  HuggingFace MiniLM → 384-dim vectors            ║
║         │                                                        ║
║         ▼                                                        ║
║   💾  STORE  →  FAISS Vector Database (Meta)                     ║
║                                                                  ║
║   ❓ User Question                                               ║
║         │                                                        ║
║         ▼                                                        ║
║   🔍  RETRIEVE  →  Top-4 most similar chunks (cosine sim)        ║
║         │                                                        ║
║         ▼                                                        ║
║   🤖  GENERATE  →  LLaMA3 via Groq API + context = Answer       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🧩 **Framework** | LangChain 0.2 | Orchestrates the entire RAG pipeline |
| 🔢 **Embeddings** | HuggingFace `all-MiniLM-L6-v2` | Converts text → 384-dim vectors (free, local) |
| 💾 **Vector Store** | FAISS (Meta) | Lightning-fast similarity search |
| 🤖 **LLM** | LLaMA3 via Groq API | Free, fast inference for answer generation |
| 🖥️ **UI** | Streamlit | Python → interactive web app instantly |
| 📄 **Doc Loading** | PyPDF + TextLoader | Handles PDF and plain text files |
| ✂️ **Chunking** | RecursiveCharacterTextSplitter | Smart paragraph-aware splitting |

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/madhura-23/rag-pipeline
cd rag-pipeline

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Get your FREE Groq API key at https://console.groq.com

# Launch the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser 🎉

---

## 📁 Project Structure

```
rag-pipeline/
│
├── 📄 app.py            → Streamlit UI: file upload, question input, answer display
├── 🧠 rag_engine.py     → Core RAG logic: load → chunk → embed → retrieve → generate
├── 📋 requirements.txt  → All Python dependencies
├── 🙈 .gitignore        → Excludes venv, secrets, temp files
└── 📖 README.md         → You are here
```

---

## 💡 Key Concepts (Interview-Ready)

**🔹 Chunking** — Documents split into ~500 char pieces with 50-char overlap so meaning isn't lost at boundaries between chunks.

**🔹 Embeddings** — `all-MiniLM-L6-v2` converts text into 384-dimensional vectors. Semantically similar sentences produce nearby vectors in this space.

**🔹 FAISS** — Stores all chunk vectors and performs approximate nearest-neighbour search in milliseconds using cosine similarity.

**🔹 Retrieval** — User question is embedded, top-k=4 most similar chunks retrieved — not keyword matching, but *meaning* matching.

**🔹 Augmented Generation** — Retrieved chunks injected as context into LLaMA3 prompt. The LLM answers only from that context — grounded, not hallucinated.

---

## 🔮 Roadmap

- [x] PDF & TXT document support
- [x] FAISS vector store
- [x] LLaMA3 via Groq (free)
- [x] Streamlit UI with context viewer
- [ ] Multi-document support
- [ ] Chat history / conversation memory
- [ ] Support for DOCX and CSV files
- [ ] GPT-4 / Gemini model toggle

---

## 👩‍💻 Built By

<div align="center">

**Madhura Bhatt**  
B.Tech AI & Data Science | ML · NLP · GenAI · Full-Stack

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Madhura%20Bhat-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/madhura-bhatt23)
[![GitHub](https://img.shields.io/badge/GitHub-madhura--23-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/madhura-23)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=C0392B&height=100&section=footer"/>

</div>
