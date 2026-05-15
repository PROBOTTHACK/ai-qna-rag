"""
Caching utilities.
"""

import streamlit as st

from modules.embeddings import (
    EmbeddingModel
)

from modules.ollama_client import (
    OllamaClient
)


@st.cache_resource
def load_embedding_model():
    """
    Load embedding model once.
    """

    embedding_service = (
        EmbeddingModel()
    )

    return (
        embedding_service.get_embeddings()
    )


@st.cache_resource
def load_ollama_client():
    """
    Load Ollama client once.
    """

    return OllamaClient()