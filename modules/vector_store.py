"""
Vector store module.

Responsible for:
- Creating FAISS vector database
- Saving vector store
- Loading vector store
- Similarity search
"""

from typing import List, Optional

from langchain_core.documents import Document

from langchain_community.vectorstores import (
    FAISS
)

from config.settings import Settings
import os

class VectorStoreManager:
    """
    Handles FAISS vector database operations.
    """

    def __init__(self, embedding_model):
        """
        Initialize vector store manager.

        Args:
            embedding_model:
                HuggingFace embedding model.
        """

        self.embedding_model = embedding_model

        self.vector_store = None

    def create_vector_store(
        self,
        documents: List[Document]
    ):
        """
        Create FAISS vector store.

        Args:
            documents (List[Document]):
                Chunked documents.
        """

        try:

            print(
                "Creating FAISS vector store..."
            )

            self.vector_store = (
                FAISS.from_documents(
                    documents=documents,
                    embedding=self.embedding_model
                )
            )

            print(
                "Vector store created successfully."
            )

        except Exception as error:

            print(
                f"Error creating vector store: "
                f"{error}"
            )

    def save_vector_store(self):
        """
        Save vector store locally.
        """

        try:

            if self.vector_store is None:

                raise ValueError(
                    "Vector store does not exist."
                )

            self.vector_store.save_local(
                Settings.VECTOR_DB_PATH
            )

            print(
                "Vector store saved successfully."
            )

        except Exception as error:

            print(
                f"Error saving vector store: "
                f"{error}"
            )

    def load_vector_store(self):
        """
        Load vector store from disk.
        """

        try:

            print(
                "Loading vector store..."
            )

            self.vector_store = FAISS.load_local(
                Settings.VECTOR_DB_PATH,
                self.embedding_model,
                allow_dangerous_deserialization=True
            )

            print(
                "Vector store loaded successfully."
            )

        except Exception as error:

            print(
                f"Error loading vector store: "
                f"{error}"
            )
    def vectorstore_exists(
        self,
        vectorstore_path: str
    ) -> bool:
        """
        Check if vector store exists.
        """

        return os.path.exists(
            vectorstore_path
        )
    def save_vector_store_to_path(
        self,
        vectorstore_path: str
    ):
        """
        Save vector store to custom path.
        """

        try:

            if self.vector_store is None:

                raise ValueError(
                    "Vector store does not exist."
                )

            self.vector_store.save_local(
                vectorstore_path
            )

            print(
                "Vector store saved successfully."
            )

        except Exception as error:

            print(
                f"Error saving vector store: "
                f"{error}"
            )
    def load_vector_store_from_path(
        self,
        vectorstore_path: str
    ):
        """
        Load vector store from path.
        """

        try:

            self.vector_store = FAISS.load_local(
                vectorstore_path,
                self.embedding_model,
                allow_dangerous_deserialization=True
            )

            print(
                "Existing vector store loaded."
            )

        except Exception as error:

            print(
                f"Error loading vector store: "
                f"{error}"
            )
    def similarity_search(
        self,
        query: str,
        k: int = 4
    ) -> Optional[List[Document]]:
        """
        Perform semantic similarity search.

        Args:
            query (str):
                User query.

            k (int):
                Number of results.

        Returns:
            List[Document]
        """

        try:

            if self.vector_store is None:

                raise ValueError(
                    "Vector store not initialized."
                )

            results = (
                self.vector_store.similarity_search(
                    query=query,
                    k=k
                )
            )

            return results

        except Exception as error:

            print(
                f"Error during similarity search: "
                f"{error}"
            )

            return []