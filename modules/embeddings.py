"""
Embeddings module.

Responsible for:
- Loading embedding model
- Generating embeddings
- Providing reusable embedding service
"""

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from config.settings import Settings


class EmbeddingModel:
    """
    Handles embedding model operations.
    """

    def __init__(self):
        """
        Initialize embedding model.
        """

        self.embedding_model = None

        self.load_embedding_model()

    def load_embedding_model(self):
        """
        Load HuggingFace embedding model.
        """

        try:

            print(
                "Loading embedding model..."
            )

            self.embedding_model = (
                HuggingFaceEmbeddings(
                    model_name=(
                        Settings.EMBEDDING_MODEL
                    )
                )
            )

            print(
                "Embedding model loaded successfully."
            )

        except Exception as error:

            print(
                f"Error loading embeddings: {error}"
            )

            self.embedding_model = None

    def get_embeddings(self):
        """
        Return embedding model instance.

        Returns:
            HuggingFaceEmbeddings
        """

        return self.embedding_model