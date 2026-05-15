from modules.pdf_loader import PDFLoader
from modules.text_splitter import TextSplitter
from modules.embeddings import EmbeddingModel
from modules.vector_store import (
    VectorStoreManager
)
from modules.retriever import Retriever
from modules.ollama_client import (
    OllamaClient
)
from modules.question_generator import (
    QuestionPaperGenerator
)

# ==============================
# LOAD PDF
# ==============================

loader = PDFLoader()

documents = loader.load_single_pdf(
    "data/uploaded_pdfs/sample.pdf"
)

# ==============================
# SPLIT DOCUMENTS
# ==============================

splitter = TextSplitter()

chunks = splitter.split_documents(
    documents
)

# ==============================
# LOAD EMBEDDINGS
# ==============================

embedding_service = EmbeddingModel()

embedding_model = (
    embedding_service.get_embeddings()
)

# ==============================
# CREATE VECTOR STORE
# ==============================

vector_store = VectorStoreManager(
    embedding_model
)

vector_store.create_vector_store(
    chunks
)

# ==============================
# CREATE RETRIEVER
# ==============================

retriever = Retriever(
    vector_store
)

# ==============================
# LOAD OLLAMA
# ==============================

ollama_client = OllamaClient()

# ==============================
# CREATE GENERATOR
# ==============================

generator = QuestionPaperGenerator(
    retriever=retriever,
    ollama_client=ollama_client
)

# ==============================
# GENERATE QUESTIONS
# ==============================

questions = (
    generator.generate_question_paper(
        topic="RMI and Hibernate",
        num_questions=5
    )
)

print("\n")
print("=" * 60)

print("GENERATED QUESTION PAPER")

print("=" * 60)

print("\n")

print(questions)

# ==============================
# GENERATE ANSWERS
# ==============================

answers = (
    generator.generate_answer_key(
        questions
    )
)

print("\n")
print("=" * 60)

print("GENERATED ANSWER KEY")

print("=" * 60)

print("\n")

print(answers)