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
from utils.file_hash import (
    FileHashGenerator
)
from templates.exam_template import (
    ExamTemplate
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
    if "generation_complete" not in st.session_state:
        st.session_state.generation_complete = False

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
        st.session_state.generation_complete = False

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
            # GENERATE PDF HASH
            # ==========================

            combined_content = b""

            for file in uploaded_files:

                combined_content += (
                    file.getvalue()
                )

            pdf_hash = (
                FileHashGenerator
                .generate_file_hash(
                    combined_content
                )
            )

            vectorstore_path = os.path.join(
                Settings.VECTORSTORE_DIR,
                pdf_hash
            )

            # ==========================
            # VECTOR STORE MANAGER
            # ==========================

            vector_store = (
                VectorStoreManager(
                    embedding_model
                )
            )

            # ==========================
            # REUSE EXISTING VECTOR DB
            # ==========================

            if vector_store.vectorstore_exists(
                vectorstore_path
            ):

                render_generation_status(
                    "Loading existing vector database..."
                )

                vector_store.load_vector_store_from_path(
                    vectorstore_path
                )

            # ==========================
            # CREATE NEW VECTOR DB
            # ==========================

            else:

                render_generation_status(
                    "Creating new vector database..."
                )

                vector_store.create_vector_store(
                    chunks
                )

                vector_store.save_vector_store_to_path(
                    vectorstore_path
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

            # ==========================
            # GENERATE EXAM SECTIONS
            # ==========================

            generated_sections = {}

            sections = [

                {
                    "title": "SECTION A",
                    "question_type": (
                        settings["section_a_type"]
                    ),
                    "marks": (
                        settings["section_a_marks"]
                    ),
                    "num_questions": (
                        settings["section_a_questions"]
                    )
                },

                {
                    "title": "SECTION B",
                    "question_type": (
                        settings["section_b_type"]
                    ),
                    "marks": (
                        settings["section_b_marks"]
                    ),
                    "num_questions": (
                        settings["section_b_questions"]
                    )
                },

                {
                    "title": "SECTION C",
                    "question_type": (
                        settings["section_c_type"]
                    ),
                    "marks": (
                        settings["section_c_marks"]
                    ),
                    "num_questions": (
                        settings["section_c_questions"]
                    )
                }
            ]

            # ==========================
            # GENERATE EACH SECTION
            # ==========================

            for section in sections:

                render_generation_status(
                    f"Generating {section['title']}..."
                )

                generated_questions = (
                    generator.generate_question_paper(

                        topic=topic,

                        question_type=(
                            section["question_type"]
                        ),

                        difficulty=(
                            settings["difficulty"]
                        ),

                        marks=(
                            section["marks"]
                        ),

                        num_questions=(
                            section["num_questions"]
                        )
                    )
                )

                generated_sections[
                    section["title"]
                ] = {

                    "questions": generated_questions,

                    "marks": section["marks"]
                }
            # ==========================
            # BUILD EXAM TEMPLATE
            # ==========================

            exam_template = ExamTemplate(

                subject_name=(
                    settings["subject_name"]
                ),

                exam_duration=(
                    settings["exam_duration"]
                ),

                total_marks=(
                    settings["total_marks"]
                )
            )

            questions = (
                exam_template.build_complete_paper(
                    generated_sections
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
            
            st.session_state.generation_complete = True

    

        except Exception as error:

            st.error(
                f"Application Error: {error}"
            )
    # ===================================
    # SHOW OUTPUTS ONLY AFTER GENERATION
    # ===================================

    if (
        st.session_state.generation_complete
        and
        st.session_state.formatted_questions
        and
        st.session_state.formatted_answers
    ):
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

        if st.session_state.question_pdf_path:

            with open(
                st.session_state.question_pdf_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📘 Download Question Paper",
                    data=file,
                    file_name="question_paper.pdf",
                    mime="application/pdf"
                )

        if st.session_state.answer_pdf_path:

            with open(
                st.session_state.answer_pdf_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📗 Download Answer Key",
                    data=file,
                    file_name="answer_key.pdf",
                    mime="application/pdf"
                )


if __name__ == "__main__":

    main()