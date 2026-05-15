"""
Main Streamlit application file.
"""

import streamlit as st

from config.settings import Settings


def initialize_app():
    """
    Configure Streamlit page settings.
    """

    st.set_page_config(
        page_title=Settings.APP_TITLE,
        page_icon="📘",
        layout="wide"
    )


def main():
    """
    Main application function.
    """

    initialize_app()

    # ==============================
    # APP HEADER
    # ==============================

    st.title(Settings.APP_TITLE)

    st.markdown(Settings.APP_DESCRIPTION)

    st.divider()

    # ==============================
    # SIDEBAR
    # ==============================

    with st.sidebar:
        st.header("⚙️ Configuration")

        st.info(
            f"""
            Model: {Settings.OLLAMA_MODEL}

            Embeddings:
            {Settings.EMBEDDING_MODEL}
            """
        )

    # ==============================
    # MAIN CONTENT
    # ==============================

    st.subheader("📂 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Upload study materials",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(
            f"{len(uploaded_files)} file(s) uploaded successfully."
        )

    st.divider()

    st.subheader("📝 Question Paper Generator")

    st.info(
        "Generation pipeline will be implemented "
        "in the next steps."
    )


if __name__ == "__main__":
    main()