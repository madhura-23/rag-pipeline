# ============================================================
# app.py — The FACE of the RAG pipeline (Streamlit UI)
# ============================================================
# Streamlit turns Python code into a web app automatically.
# No HTML, no CSS, no JavaScript needed.
# Every time the user does something (uploads file, clicks button),
# Streamlit reruns this file from top to bottom. Simple!
# ============================================================

import streamlit as st
import tempfile
import os
from rag_engine import run_rag_pipeline

# ────────────────────────────────────────────────────────────
# PAGE CONFIG — must be the very first Streamlit command
# ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DocuQuery — RAG Pipeline",
    page_icon="🔍",
    layout="centered"
)

# ────────────────────────────────────────────────────────────
# CUSTOM STYLING
# ────────────────────────────────────────────────────────────
st.markdown("""
    <style>
    .main { background-color: #0f0f0f; }
    .stTextInput > div > div > input { border-color: #C0392B; }
    .stButton > button {
        background-color: #C0392B;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton > button:hover { background-color: #a93226; }
    .answer-box {
        background-color: #1a1a1a;
        border-left: 4px solid #C0392B;
        padding: 1rem 1.2rem;
        border-radius: 4px;
        margin-top: 1rem;
    }
    .context-box {
        background-color: #111;
        border: 1px solid #333;
        padding: 0.8rem;
        border-radius: 4px;
        font-size: 0.8rem;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────
# HEADER
# ────────────────────────────────────────────────────────────
st.title("🔍 DocuQuery")
st.markdown("**RAG-powered document Q&A** — Upload any PDF or text file and ask questions about it.")
st.markdown("---")

# ────────────────────────────────────────────────────────────
# SIDEBAR — API Key input
# ────────────────────────────────────────────────────────────
# We put the API key in the sidebar so it's separate from main UI
# In production you'd use environment variables (st.secrets)
with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("Get your **free** Groq API key at [console.groq.com](https://console.groq.com)")

    groq_api_key = st.text_input(
        "Groq API Key",
        type="password",       # Hides the key like a password field
        placeholder="gsk_..."
    )

    st.markdown("---")
    st.markdown("**How it works:**")
    st.markdown("""
    1. 📄 Upload your document
    2. ✂️ It gets split into chunks
    3. 🔢 Chunks → vectors (embeddings)
    4. 💾 Stored in FAISS database
    5. ❓ You ask a question
    6. 🔍 Most relevant chunks retrieved
    7. 🤖 LLaMA3 answers using those chunks
    """)

    st.markdown("---")
    st.markdown("Built by **Madhura Bhat**")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-madhura--23-black?logo=github)](https://github.com/madhura-23)")

# ────────────────────────────────────────────────────────────
# MAIN AREA — File Upload
# ────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "📁 Upload a document",
    type=["pdf", "txt"],
    help="Supports PDF and plain text files"
)

# Show file info when uploaded
if uploaded_file:
    col1, col2 = st.columns(2)
    col1.metric("File Name", uploaded_file.name)
    col2.metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")
    st.success("✅ File uploaded successfully!")

st.markdown("---")

# ────────────────────────────────────────────────────────────
# QUESTION INPUT
# ────────────────────────────────────────────────────────────
question = st.text_input(
    "💬 Ask a question about your document",
    placeholder="e.g. What is the main topic of this document?",
)

# Show context toggle — great for understanding RAG in interviews!
show_context = st.checkbox(
    "🔍 Show retrieved context (see which chunks were used)",
    value=False,
    help="Shows the raw text chunks retrieved from your document before sending to LLM"
)

# ────────────────────────────────────────────────────────────
# RUN BUTTON
# ────────────────────────────────────────────────────────────
run_button = st.button("🚀 Get Answer", use_container_width=True)

if run_button:
    # Input validation — check everything is ready
    if not groq_api_key:
        st.error("⚠️ Please enter your Groq API key in the sidebar.")
    elif not uploaded_file:
        st.error("⚠️ Please upload a document first.")
    elif not question.strip():
        st.error("⚠️ Please enter a question.")
    else:
        # ── Save uploaded file to a temp location ──────────────
        # Streamlit gives us a file-like object, but LangChain needs
        # an actual file path on disk. So we save it temporarily.
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f".{uploaded_file.name.split('.')[-1]}"
        ) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        # ── Run the RAG pipeline ────────────────────────────────
        try:
            with st.spinner("⏳ Processing document and generating answer..."):
                result = run_rag_pipeline(
                    file_path=tmp_path,
                    question=question,
                    api_key=groq_api_key
                )

            # ── Display Answer ──────────────────────────────────
            st.markdown("### 🤖 Answer")
            st.markdown(
                f'<div class="answer-box">{result["answer"]}</div>',
                unsafe_allow_html=True
            )

            # Show chunk count as a fun metric
            st.caption(f"📊 Document split into {result['num_chunks']} chunks | "
                      f"Top 4 most relevant chunks used for this answer")

            # ── Show Context (optional) ─────────────────────────
            # This is the KEY teaching feature — shows exactly what
            # the LLM received as context before answering.
            # Great to mention in interviews!
            if show_context:
                st.markdown("### 🔍 Retrieved Context")
                st.info("These are the exact chunks from your document that were sent to the LLM:")
                st.markdown(
                    f'<div class="context-box">{result["context"]}</div>',
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.markdown("**Common fixes:**")
            st.markdown("- Check your Groq API key is correct")
            st.markdown("- Make sure your document isn't password-protected")
            st.markdown("- Try a smaller file if the document is very large")

        finally:
            # Always clean up the temp file
            os.unlink(tmp_path)

# ────────────────────────────────────────────────────────────
# FOOTER
# ────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center><small>Built with LangChain · FAISS · HuggingFace · Groq LLaMA3 · Streamlit</small></center>",
    unsafe_allow_html=True
)