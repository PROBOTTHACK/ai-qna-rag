"""
Retriever module.

Responsible for:
- Retrieving relevant chunks
- Preparing context for LLMs
- Managing semantic search pipeline
"""

from typing import List

from langchain_core.documents import Document


class Retriever:
    """
    Handles semantic retrieval operations.
    """

    def __init__(self, vector_store):
        """
        Initialize retriever.

        Args:
            vector_store:
                FAISS vector store manager.
        """

        self.vector_store = vector_store

    def retrieve_documents(
        self,
        query: str,
        k: int = 4
    ) -> List[Document]:
        """
        Retrieve relevant documents.

        Args:
            query (str):
                User query.

            k (int):
                Number of results.

        Returns:
            List[Document]
        """

        try:

            results = (
                self.vector_store.similarity_search(
                    query=query,
                    k=k
                )
            )

            print(
                f"Retrieved {len(results)} "
                f"relevant chunks."
            )

            return results

        except Exception as error:

            print(
                f"Retrieval error: {error}"
            )

            return []

    def build_context(
        self,
        documents: List[Document]
    ) -> str:
        """
        Combine retrieved chunks into context.

        Args:
            documents (List[Document]):
                Retrieved documents.

        Returns:
            str:
                Combined context.
        """

        try:

            context = "\n\n".join(
                [
                    doc.page_content
                    for doc in documents
                ]
            )

            return context

        except Exception as error:

            print(
                f"Context building error: "
                f"{error}"
            )

            return ""

    def retrieve_context(
        self,
        query: str,
        k: int = 4
    ) -> str:
        """
        Complete retrieval pipeline.

        Args:
            query (str):
                User query.

            k (int):
                Number of chunks.

        Returns:
            str:
                Final formatted context.
        """

        documents = self.retrieve_documents(
            query=query,
            k=k
        )

        context = self.build_context(
            documents
        )

        return context