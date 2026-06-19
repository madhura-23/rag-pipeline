import os
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_and_chunk(file_path):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    return chunks

def build_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

def retrieve_context(vector_store, question, k=4):
    relevant_docs = vector_store.similarity_search(question, k=k)
    context = "\n\n---\n\n".join([doc.page_content for doc in relevant_docs])
    return context

def ask_llm(question, context, api_key):
    client = Groq(api_key=api_key)
    prompt = f"""You are a helpful assistant that answers questions 
based ONLY on the provided document context below.
If the answer is not in the context, say: 
"I could not find this information in the uploaded document."

CONTEXT FROM DOCUMENT:
{context}

USER QUESTION:
{question}

ANSWER:"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a precise document assistant. Answer only from the given context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1024
    )
    return response.choices[0].message.content

def run_rag_pipeline(file_path, question, api_key):
    chunks = load_and_chunk(file_path)
    vector_store = build_vector_store(chunks)
    context = retrieve_context(vector_store, question)
    answer = ask_llm(question, context, api_key)
    return {"answer": answer, "context": context, "num_chunks": len(chunks)}
