"""
Advanced formatter module.

Responsible for:
- Markdown formatting
- Question cleanup
- Answer cleanup
- Professional structure
"""

import re


class Formatter:

    def clean_markdown(
        self,
        text: str
    ) -> str:
        """
        Clean markdown output.
        """

        # Remove excessive blank lines
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

        # Fix numbering spacing
        text = re.sub(
            r"(\d+)\.",
            r"\n\1.",
            text
        )

        return text.strip()

    def format_question_paper(
        self,
        questions: str
    ) -> str:

        cleaned = self.clean_markdown(
            questions
        )

        formatted = f"""
# QUESTION PAPER

{cleaned}
"""

        return formatted

    def format_answer_key(
        self,
        answers: str
    ) -> str:

        cleaned = self.clean_markdown(
            answers
        )

        formatted = f"""
# ANSWER KEY

{cleaned}
"""

        return formatted