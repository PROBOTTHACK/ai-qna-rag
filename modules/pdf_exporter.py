"""
PDF exporter module.

Responsible for:
- Exporting question papers
- Exporting answer keys
- Creating professional PDFs
"""

import os

from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from config.settings import Settings


class PDFExporter:
    """
    Handles PDF export operations.
    """

    def __init__(self):
        """
        Initialize PDF exporter.
        """

        self.styles = (
            getSampleStyleSheet()
        )

        os.makedirs(
            Settings.OUTPUT_DIR,
            exist_ok=True
        )

    def export_pdf(
        self,
        content: str,
        filename: str,
        title: str
    ) -> str:
        """
        Export content as PDF.

        Args:
            content (str):
                PDF content.

            filename (str):
                Output filename.

            title (str):
                Document title.

        Returns:
            str:
                Saved PDF path.
        """

        try:

            pdf_path = os.path.join(
                Settings.OUTPUT_DIR,
                filename
            )

            # ==========================
            # CREATE PDF DOCUMENT
            # ==========================

            document = (
                SimpleDocTemplate(
                    pdf_path,
                    pagesize=letter
                )
            )

            story = []

            # ==========================
            # TITLE
            # ==========================

            title_style = (
                self.styles["Title"]
            )

            story.append(
                Paragraph(
                    title,
                    title_style
                )
            )

            story.append(
                Spacer(1, 20)
            )

            # ==========================
            # CONTENT
            # ==========================

            normal_style = (
                self.styles["BodyText"]
            )

            paragraphs = (
                content.split("\n")
            )

            for para in paragraphs:

                if para.strip():

                    story.append(
                        Paragraph(
                            para,
                            normal_style
                        )
                    )

                    story.append(
                        Spacer(1, 10)
                    )

            # ==========================
            # BUILD PDF
            # ==========================

            document.build(story)

            print(
                f"PDF exported successfully: "
                f"{pdf_path}"
            )

            return pdf_path

        except Exception as error:

            print(
                f"PDF export error: "
                f"{error}"
            )

            return ""

    def export_question_paper(
        self,
        questions: str
    ) -> str:
        """
        Export question paper PDF.

        Args:
            questions (str):
                Generated questions.

        Returns:
            str:
                PDF path.
        """

        return self.export_pdf(
            content=questions,
            filename="question_paper.pdf",
            title="Question Paper"
        )

    def export_answer_key(
        self,
        answers: str
    ) -> str:
        """
        Export answer key PDF.

        Args:
            answers (str):
                Generated answers.

        Returns:
            str:
                PDF path.
        """

        return self.export_pdf(
            content=answers,
            filename="answer_key.pdf",
            title="Answer Key"
        )