"""
Question generation module.

Responsible for:
- Generating question papers
- Generating answer keys
- Managing RAG generation pipeline
"""

from config.prompts import (
    QUESTION_PAPER_PROMPT,
    ANSWER_KEY_PROMPT
)


class QuestionPaperGenerator:
    """
    Handles AI-based question generation.
    """

    def __init__(
        self,
        retriever,
        ollama_client
    ):
        """
        Initialize generator.

        Args:
            retriever:
                Retriever instance.

            ollama_client:
                Ollama LLM client.
        """

        self.retriever = retriever

        self.ollama_client = ollama_client

    def generate_question_paper(
        self,
        topic: str,
        num_questions: int = 5
    ) -> str:
        """
        Generate question paper.

        Args:
            topic (str):
                Topic/query.

            num_questions (int):
                Number of questions.

        Returns:
            str:
                Generated question paper.
        """

        try:

            # ==============================
            # RETRIEVE CONTEXT
            # ==============================

            context = (
                self.retriever.retrieve_context(
                    query=topic,
                    k=4
                )
            )

            # ==============================
            # BUILD PROMPT
            # ==============================

            prompt = (
                QUESTION_PAPER_PROMPT.format(
                    context=context
                )
            )

            prompt += f"""

Generate exactly {num_questions} questions.

Topic:
{topic}
"""

            # ==============================
            # GENERATE RESPONSE
            # ==============================

            response = (
                self.ollama_client.generate_response(
                    prompt
                )
            )

            return response

        except Exception as error:

            print(
                f"Question generation error: "
                f"{error}"
            )

            return ""

    def generate_answer_key(
        self,
        questions: str
    ) -> str:
        """
        Generate answer key.

        Args:
            questions (str):
                Generated questions.

        Returns:
            str:
                Generated answers.
        """

        try:

            # ==============================
            # RETRIEVE CONTEXT
            # ==============================

            context = (
                self.retriever.retrieve_context(
                    query=questions,
                    k=4
                )
            )

            # ==============================
            # BUILD PROMPT
            # ==============================

            prompt = (
                ANSWER_KEY_PROMPT.format(
                    context=context,
                    questions=questions
                )
            )

            # ==============================
            # GENERATE ANSWERS
            # ==============================

            response = (
                self.ollama_client.generate_response(
                    prompt
                )
            )

            return response

        except Exception as error:

            print(
                f"Answer generation error: "
                f"{error}"
            )

            return ""