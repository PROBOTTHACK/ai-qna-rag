# 🧠 AI Question Paper Generator
 
> **Production-grade RAG pipeline** that transforms academic PDFs into fully formatted examination papers and answer keys — running entirely offline, zero cloud dependency.
 
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=flat-square)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-009688?style=flat-square)](https://faiss.ai)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=flat-square)](https://ollama.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
 
---
 
## 🎯 What This Does
 
Upload any academic PDF → get a professionally structured, export-ready question paper with a matching answer key in seconds.
 
Built to demonstrate **end-to-end AI engineering**: from raw document ingestion through semantic retrieval to structured output generation — all running locally with Mistral via Ollama.
 
---
 
## ✨ Key Features
 
### 📄 Intelligent PDF Ingestion
- Multi-PDF upload with automatic text extraction
- Production-style chunking pipeline optimized for academic content
- Persistent FAISS vector store — embeddings computed once, reused across sessions
### 🔍 RAG Pipeline (Retrieval-Augmented Generation)
- Semantic similarity search over document chunks using HuggingFace embeddings
- Context-aware prompting ensures questions are grounded in source material
- Eliminates hallucination by anchoring generation to retrieved context
### 🤖 Fully Local Inference
- Runs 100% offline using Ollama + Mistral
- No OpenAI API key, no data leaving your machine
- Privacy-first architecture — suitable for sensitive institutional content
### 📝 Configurable Exam Generation
- **Question types**: MCQ, Short Answer, Long Answer
- **Controls**: marks per section, difficulty level, question count, exam duration
- **Auto-computed**: total marks, section distribution, instructions block
### 📑 PDF Export
- Professional exam layout: Section A / B / C structure
- Separate answer key PDF with structured, context-aware answers
- Clean typography with markdown-aware formatting via ReportLab
---
 
## 🏗️ System Architecture
 
```
PDF Upload
    │
    ▼
Text Extraction & Chunking
    │
    ▼
HuggingFace Embeddings
    │
    ▼
FAISS Vector Store  ◄──── Persistent (reused across sessions)
    │
    ▼
Semantic Retrieval (Top-K chunks)
    │
    ▼
Mistral via Ollama  ◄──── Fully local inference
    │
    ▼
Question Generation + Answer Key
    │
    ▼
Exam Template Builder
    │
    ▼
PDF Export (Question Paper + Answer Key)
```
 
---
 
## 🛠️ Tech Stack
 
| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Streamlit | Interactive UI with session state |
| **Orchestration** | LangChain | RAG pipeline, prompt chaining |
| **Vector DB** | FAISS | Semantic similarity search |
| **LLM Runtime** | Ollama | Local model serving |
| **LLM** | Mistral 7B | Question & answer generation |
| **Embeddings** | HuggingFace (`all-MiniLM`) | Semantic text encoding |
| **PDF Export** | ReportLab | Professional document generation |
| **Backend** | Python 3.10+ | Core logic & pipeline |
 
---
 
## 📂 Project Structure
 
```
ai-question-paper-generator/
│
├── app.py                  # Streamlit entry point
├── config/                 # Config-driven design (models, paths, params)
├── modules/                # Core pipeline: ingestion, retrieval, generation
├── ui/                     # Streamlit page components
├── utils/                  # Logging, validation, formatting helpers
├── templates/              # Exam layout templates
├── vectorstore/            # Persistent FAISS index
├── data/                   # Uploaded PDFs
├── logs/                   # Structured application logs
└── requirements.txt
```
 
---
 
## ⚙️ Getting Started
 
### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed
### 1. Clone & Install
 
```bash
git clone https://github.com/PROBOTTHACK/ai-qna-rag.git
 
python -m venv env
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate
 
pip install -r requirements.txt
```
 
### 2. Set Up Ollama
 
```bash
ollama pull mistral
ollama run mistral
```
 
### 3. Launch
 
```bash
streamlit run app.py
```
 
Open `http://localhost:8501` — upload a PDF and generate your first exam paper.
 
---
 
## 🧩 Engineering Highlights
 
This project was built to reflect production-grade practices, not just a working prototype:
 
- **RAG over fine-tuning** — retrieval grounds generation without expensive retraining; scales to any domain by swapping the PDF
- **Persistent vector store** — FAISS index survives app restarts; embeddings are computed once and reused, cutting latency significantly on repeat runs
- **Config-driven design** — models, chunk sizes, retrieval parameters, and export settings are externalized; no magic numbers in business logic
- **Modular architecture** — ingestion, retrieval, generation, and export are decoupled; each module is independently testable
- **Structured logging** — request tracing and error context for debugging generation failures
- **Streamlit session state** — UI state is preserved across interactions without redundant recomputation
---
 
## 🗺️ Roadmap
 
- [ ] DOCX export alongside PDF
- [ ] Citation-aware RAG (question references source section)
- [ ] Multi-model support (swap Mistral for Llama 3, Phi-3, etc.)
- [ ] Async generation for large PDFs
- [ ] Docker deployment
- [ ] Advanced answer evaluation (rubric scoring)
- [ ] Cloud deployment with auth
---
 
## 🤝 Contributing
 
PRs welcome. For major changes, open an issue first to discuss scope.
 
---
 
## 📄 License
 
MIT License
