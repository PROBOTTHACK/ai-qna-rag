"""
Ollama client module.

Responsible for:
- Connecting to Ollama
- Running local Mistral model
- Generating AI responses
"""

import os

from langchain_ollama import ChatOllama

from config.settings import Settings


class OllamaClient:
    """
    Handles local LLM operations.
    """

    def __init__(self):
        """
        Initialize Ollama model.
        """

        self.llm = None

        self.load_model()

    def load_model(self):
        """
        Load Ollama model.
        """

        try:

            print(
                "Loading Ollama model..."
            )

            self.llm = ChatOllama(
                model=Settings.OLLAMA_MODEL,
                temperature=Settings.TEMPERATURE,
                base_url=os.getenv(
                    "OLLAMA_BASE_URL",
                    "http://ollama:11434")
            )

            print(
                "Ollama model loaded successfully."
            )

        except Exception as error:

            print(
                f"Error loading Ollama model: "
                f"{error}"
            )

            self.llm = None

    def generate_response(
        self,
        prompt: str
    ) -> str:
        """
        Generate response from LLM.

        Args:
            prompt (str):
                Input prompt.

        Returns:
            str:
                Generated response.
        """

        try:

            if self.llm is None:

                raise ValueError(
                    "LLM is not initialized."
                )

            response = self.llm.invoke(
                prompt
            )

            return response.content

        except Exception as error:

            print(
                f"Generation error: {error}"
            )

            return ""