# AI Question Paper Generator

An AI-powered Question Paper and Answer Key Generator built using:

- Streamlit
- LangChain
- Ollama
- Mistral
- FAISS
- HuggingFace Embeddings
- ReportLab

The application runs completely locally using Ollama.

---

# Features

- Upload one or multiple PDFs
- Extract text from PDFs
- Chunk large documents
- Generate embeddings
- Store vectors using FAISS
- Retrieve relevant context using RAG
- Generate:
  - Question Papers
  - Answer Keys
- Preview generated content
- Export as PDF
- Fully offline AI pipeline

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Streamlit | Frontend UI |
| LangChain | AI orchestration |
| Ollama | Local LLM runtime |
| Mistral | Language model |
| FAISS | Vector database |
| HuggingFace Embeddings | Text embeddings |
| ReportLab | PDF generation |
| PyPDF | PDF text extraction |

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd ai-question-paper-generator
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

## Install Ollama

Download from:

https://ollama.com

---

## Pull Mistral Model

```bash
ollama pull mistral
```

---

## Run Ollama

```bash
ollama serve
```

---

# Running the Application

```bash
streamlit run app.py
```

---

# Project Structure

```txt
ai-question-paper-generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── config/
├── modules/
├── ui/
├── data/
├── vectorstore/
├── templates/
└── utils/
```

---

# Future Improvements

- Multiple question difficulty levels
- Bloom's Taxonomy support
- Subject-specific templates
- MCQ generation
- Auto-marking scheme
- Multi-model support
- API deployment
- Docker support

---

# License

MIT License