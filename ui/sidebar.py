"""
Sidebar UI module.

Responsible for:
- Sidebar controls
- Configuration display
- User settings
"""

import streamlit as st

from config.settings import Settings


def render_sidebar():
    """
    Render application sidebar.

    Returns:
        dict:
            User-selected settings.
    """

    st.sidebar.title(
        "⚙️ Settings"
    )

    st.sidebar.markdown("---")

    # ==============================
    # MODEL INFO
    # ==============================

    st.sidebar.subheader(
        "🤖 Model Configuration"
    )

    st.sidebar.info(
        f"""
        Model:
        {Settings.OLLAMA_MODEL}

        Embeddings:
        {Settings.EMBEDDING_MODEL}
        """
    )

    # ==============================
    # GENERATION SETTINGS
    # ==============================

    st.sidebar.subheader(
        "📝 Generation Settings"
    )

    num_questions = (
        st.sidebar.slider(
            "Number of Questions",
            min_value=1,
            max_value=20,
            value=5
        )
    )

    retrieval_chunks = (
        st.sidebar.slider(
            "Retrieved Chunks",
            min_value=1,
            max_value=10,
            value=4
        )
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        "Local AI System Ready"
    )

    return {
        "num_questions": num_questions,
        "retrieval_chunks": retrieval_chunks
    }