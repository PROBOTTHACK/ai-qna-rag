"""
PDF loading module.

Responsible for:
- Loading PDFs
- Extracting text
- Returning LangChain Document objects
"""

from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """
    Handles PDF loading and text extraction.
    """

    def __init__(self):
        """
        Initialize PDF loader.
        """

        pass

    def load_single_pdf(self, pdf_path: str) -> List[Document]:
        """
        Load a single PDF file.

        Args:
            pdf_path (str):
                Path to PDF file.

        Returns:
            List[Document]:
                Extracted document pages.
        """

        try:
            # Validate file existence
            if not Path(pdf_path).exists():
                raise FileNotFoundError(
                    f"PDF not found: {pdf_path}"
                )

            # Initialize loader
            loader = PyPDFLoader(pdf_path)

            # Load PDF
            documents = loader.load()

            print(
                f"Successfully loaded: {pdf_path}"
            )

            print(
                f"Total pages extracted: {len(documents)}"
            )

            return documents

        except Exception as error:
            print(
                f"Error loading PDF '{pdf_path}': {error}"
            )

            return []

    def load_multiple_pdfs(
        self,
        pdf_paths: List[str]
    ) -> List[Document]:
        """
        Load multiple PDF files.

        Args:
            pdf_paths (List[str]):
                List of PDF paths.

        Returns:
            List[Document]:
                Combined document list.
        """

        all_documents = []

        for pdf_path in pdf_paths:

            documents = self.load_single_pdf(
                pdf_path
            )

            all_documents.extend(documents)

        print(
            f"Total documents extracted: "
            f"{len(all_documents)}"
        )

        return all_documents