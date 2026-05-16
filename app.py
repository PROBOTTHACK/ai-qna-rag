"""
Main Streamlit application.
"""

import os

import streamlit as st

from config.settings import Settings

from ui.sidebar import render_sidebar
from ui.forms import render_generation_form
from ui.preview import (
    render_question_preview,
    render_answer_preview,
    render_generation_status
)

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
from modules.formatter import (
    Formatter
)
from modules.pdf_exporter import (
    PDFExporter
)

from utils.validators import (
    Validators
)
from utils.cache import (
    load_embedding_model,
    load_ollama_client
)

from modules.formatter import Formatter
from modules.pdf_exporter import PDFExporter

def initialize_app():
    """
    Configure Streamlit app.
    """

    st.set_page_config(
        page_title=Settings.APP_TITLE,
        page_icon="📘",
        layout="wide"
    )


def save_uploaded_files(
    uploaded_files
):
    """
    Save uploaded PDFs locally.

    Args:
        uploaded_files:
            Uploaded Streamlit files.

    Returns:
        list:
            Saved file paths.
    """

    saved_paths = []

    os.makedirs(
        Settings.UPLOAD_DIR,
        exist_ok=True
    )

    for file in uploaded_files:

        file_path = os.path.join(
            Settings.UPLOAD_DIR,
            file.name
        )

        with open(file_path, "wb") as f:

            f.write(file.getbuffer())

        saved_paths.append(file_path)

    return saved_paths


def main():
    """
    Main application function.
    """
    # ==============================
    # SESSION STATE
    # ==============================

    if "formatted_questions" not in st.session_state:
        st.session_state.formatted_questions = None

    if "formatted_answers" not in st.session_state:
        st.session_state.formatted_answers = None

    if "question_pdf_path" not in st.session_state:
        st.session_state.question_pdf_path = None

    if "answer_pdf_path" not in st.session_state:
        st.session_state.answer_pdf_path = None

    initialize_app()

    # ==============================
    # SIDEBAR
    # ==============================

    settings = render_sidebar()

    # ==============================
    # PAGE HEADER
    # ==============================

    st.title(
        Settings.APP_TITLE
    )

    st.write(
        Settings.APP_DESCRIPTION
    )

    st.markdown("---")

    # ==============================
    # FORM
    # ==============================

    form_data = (
        render_generation_form()
    )

    # ==============================
    # GENERATE PIPELINE
    # ==============================

    if form_data["generate_button"]:

        uploaded_files = (
            form_data["uploaded_files"]
        )

        topic = (
            form_data["topic"]
        )

        # ==========================
        # VALIDATION
        # ==========================

        if not Validators.validate_uploaded_files(uploaded_files):

            st.error(
                "Please upload PDF files."
            )

            return

        if not Validators.validate_topic(topic):

            st.error(
                "Please enter a topic."
            )

            return
        # ==========================
        # VALIDATE EACH PDF
        # ==========================

        for file in uploaded_files:

            is_valid, message = (
                Validators.validate_pdf_file(
                    file
                )
            )

            if not is_valid:

                st.error(message)

                return

        try:

            # ==========================
            # SAVE FILES
            # ==========================

            render_generation_status(
                "Saving uploaded PDFs..."
            )

            pdf_paths = (
                save_uploaded_files(
                    uploaded_files
                )
            )

            # ==========================
            # LOAD PDFs
            # ==========================

            render_generation_status(
                "Loading PDFs..."
            )

            loader = PDFLoader()

            documents = []

            for path in pdf_paths:

                docs = (
                    loader.load_single_pdf(
                        path
                    )
                )

                documents.extend(docs)

            # ==========================
            # SPLIT TEXT
            # ==========================

            render_generation_status(
                "Splitting text..."
            )

            splitter = TextSplitter()

            chunks = (
                splitter.split_documents(
                    documents
                )
            )

            # ==========================
            # LOAD EMBEDDINGS
            # ==========================

            render_generation_status(
                "Loading embeddings..."
            )

            # embedding_service = (
            #     EmbeddingModel()
            # )

            embedding_model = (
                load_embedding_model()
            )

            # ==========================
            # CREATE VECTOR STORE
            # ==========================

            render_generation_status(
                "Creating vector store..."
            )

            vector_store = (
                VectorStoreManager(
                    embedding_model
                )
            )

            vector_store.create_vector_store(
                chunks
            )

            # ==========================
            # CREATE RETRIEVER
            # ==========================

            retriever = Retriever(
                vector_store
            )

            # ==========================
            # LOAD OLLAMA
            # ==========================

            render_generation_status(
                "Loading local AI model..."
            )

            ollama_client = (
                load_ollama_client()
            )

            # ==========================
            # GENERATE QUESTIONS
            # ==========================

            render_generation_status(
                "Generating question paper..."
            )

            generator = (
                QuestionPaperGenerator(
                    retriever=retriever,
                    ollama_client=(
                        ollama_client
                    )
                )
            )

            questions = (
                generator.generate_question_paper(
                    topic=topic,
                    question_type=(
                        settings[
                            "question_type"
                        ]
                    ),
                    difficulty=(
                        settings[
                            "difficulty"
                        ]
                    ),
                    marks=(
                        settings[
                            "marks"
                        ]
                    ),
                    num_questions=(
                        settings[
                            "num_questions"
                        ]
                    )
                )
            )

            # ==========================
            # GENERATE ANSWERS
            # ==========================

            render_generation_status(
                "Generating answer key..."
            )

            answers = (
                generator
                .generate_answer_key(
                    questions
                )
            )

           
            # ==========================
            # FORMAT OUTPUTS
            # ==========================

            formatter = Formatter()

            st.session_state.formatted_questions = (
                formatter.format_question_paper(
                    questions
                )
            )

            st.session_state.formatted_answers = (
                formatter.format_answer_key(
                    answers
                )
            )


            # ========================== 
            # EXPORT PDFs
            # ==========================

            exporter = PDFExporter()

            st.session_state.question_pdf_path = (
                exporter.export_question_paper(
                    st.session_state.formatted_questions
                )
            )

            st.session_state.answer_pdf_path = (
                exporter.export_answer_key(
                    st.session_state.formatted_answers
                )
            )

            # ==========================
            # DISPLAY OUTPUTS
            # ==========================

            render_question_preview(
                st.session_state.formatted_questions
            )

            render_answer_preview(
                st.session_state.formatted_answers
            )

            # ==========================
            # DOWNLOAD BUTTONS
            # ==========================

            st.markdown("---")

            st.subheader(
                "⬇️ Download PDFs"
            )

            with open(st.session_state.question_pdf_path, "rb") as file:

                st.download_button(
                    label="📘 Download Question Paper",
                    data=file,
                    file_name="question_paper.pdf",
                    mime="application/pdf"
                )

            with open(st.session_state.answer_pdf_path, "rb") as file:

                st.download_button(
                    label="📗 Download Answer Key",
                    data=file,
                    file_name="answer_key.pdf",
                    mime="application/pdf"
                )

        except Exception as error:

            st.error(
                f"Application Error: {error}"
            )


if __name__ == "__main__":

    main()