"""
Application settings and configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """
    Centralized configuration class.
    """

    # ==============================
    # LLM SETTINGS
    # ==============================

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))

    # ==============================
    # VECTOR DATABASE SETTINGS
    # ==============================

    VECTOR_DB_PATH = os.getenv(
        "VECTOR_DB_PATH",
        "vectorstore/faiss_index"
    )

    # ==============================
    # DATA DIRECTORIES
    # ==============================

    UPLOAD_DIR = os.getenv(
        "UPLOAD_DIR",
        "data/uploaded_pdfs"
    )

    OUTPUT_DIR = os.getenv(
        "OUTPUT_DIR",
        "data/generated_papers"
    )

    # ==============================
    # EMBEDDING MODEL
    # ==============================

    EMBEDDING_MODEL = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # ==============================
    # TEXT SPLITTING SETTINGS
    # ==============================

    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    # ==============================
    # PDF SETTINGS
    # ==============================

    MAX_FILE_SIZE_MB = 25

    # ==============================
    # UI SETTINGS
    # ==============================

    APP_TITLE = "AI Question Paper Generator"

    APP_DESCRIPTION = (
        "Generate question papers and answer keys "
        "using local AI models."
    )