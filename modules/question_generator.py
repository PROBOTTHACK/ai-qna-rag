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
        question_type: str,
        difficulty: str,
        marks: int,
        num_questions: int = 5
    ) -> str:
        """
        Generate question paper.

        Args:
            topic (str):
                Topic/query.

            question_type (str):
                Type of questions.

            difficulty (str):
                Difficulty level.

            marks (int):
                Marks per question.

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

            You are an expert university examination paper setter.

            Generate exactly {num_questions} questions.

            TOPIC:
            {topic}

            QUESTION TYPE:
            {question_type}

            DIFFICULTY:
            {difficulty}

            MARKS PER QUESTION:
            {marks}

            STRICT INSTRUCTIONS:

            1. Generate ONLY questions.
            2. Do NOT generate headings.
            3. Do NOT generate metadata.
            4. Do NOT generate explanations.
            5. Do NOT generate answers.
            6. Do NOT write:
            - Topic
            - Question Paper
            - Answer Key
            - Difficulty Level
            7. Every question must be numbered.
            8. Each question must appear on a separate line.

            QUESTION TYPE RULES:

            IF question type is MCQ:
            - Every question MUST contain 4 options.
            - Use format:

            1. Question text

            A) Option
            B) Option
            C) Option
            D) Option

            IF question type is Short Answer:
            - Generate concise theoretical questions only.

            IF question type is Long Answer:
            - Generate descriptive analytical questions only.

            OUTPUT ONLY RAW QUESTIONS.
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