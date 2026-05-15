"""
Text splitting module.

Responsible for:
- Splitting documents into chunks
- Preserving context overlap
- Preparing text for embeddings
"""

from typing import List

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_core.documents import Document

from config.settings import Settings


class TextSplitter:
    """
    Handles document chunking.
    """

    def __init__(self):
        """
        Initialize text splitter with settings.
        """

        self.text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=Settings.CHUNK_SIZE,
                chunk_overlap=Settings.CHUNK_OVERLAP,
                length_function=len,
                separators=[
                    "\n\n",
                    "\n",
                    ". ",
                    " ",
                    ""
                ]
            )
        )

    def split_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:
        """
        Split documents into smaller chunks.

        Args:
            documents (List[Document]):
                Original documents.

        Returns:
            List[Document]:
                Chunked documents.
        """

        try:
            chunks = self.text_splitter.split_documents(
                documents
            )

            print(
                f"Successfully created "
                f"{len(chunks)} chunks."
            )

            return chunks

        except Exception as error:

            print(
                f"Error during text splitting: {error}"
            )

            return []