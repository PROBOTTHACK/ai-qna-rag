"""
Professional PDF exporter.
"""

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from config.settings import Settings


class PDFExporter:

    def __init__(self):

        os.makedirs(
            Settings.OUTPUT_DIR,
            exist_ok=True
        )

        self.styles = (
            getSampleStyleSheet()
        )

        self.title_style = ParagraphStyle(
            name="TitleStyle",
            parent=self.styles["Heading1"],
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue,
            spaceAfter=30
        )

        self.heading_style = ParagraphStyle(
            name="HeadingStyle",
            parent=self.styles["Heading2"],
            fontSize=18,
            leading=24,
            textColor=colors.darkred,
            spaceAfter=20
        )

        self.body_style = ParagraphStyle(
            name="BodyStyle",
            parent=self.styles["BodyText"],
            fontSize=12,
            leading=22,
            spaceAfter=10
        )

    def parse_content(
        self,
        content,
        story
    ):
        """
        Parse markdown-style content.
        """

        lines = content.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # ==========================
            # H1 TITLE
            # ==========================

            if line.startswith("# "):

                text = line[2:].strip()

                story.append(
                    Paragraph(
                        text,
                        self.title_style
                    )
                )

                story.append(
                    Spacer(1, 20)
                )

            # ==========================
            # H2 HEADING
            # ==========================

            elif line.startswith("## "):

                text = line[3:].strip()

                story.append(
                    Paragraph(
                        text,
                        self.heading_style
                    )
                )

                story.append(
                    Spacer(1, 15)
                )

            # ==========================
            # H3 SUBHEADING
            # ==========================

            elif line.startswith("### "):

                text = line[4:].strip()

                subheading_style = ParagraphStyle(
                    name="SubHeading",
                    parent=self.body_style,
                    fontSize=14,
                    leading=18,
                    spaceAfter=12,
                    textColor=colors.darkblue
                )

                story.append(
                    Paragraph(
                        text,
                        subheading_style
                    )
                )

            # ==========================
            # HORIZONTAL LINE
            # ==========================

            elif line == "---":

                story.append(
                    Spacer(1, 20)
                )

            # ==========================
            # BULLET POINTS
            # ==========================

            elif line.startswith("- "):

                bullet_text = (
                    f"• {line[2:]}"
                )

                story.append(
                    Paragraph(
                        bullet_text,
                        self.body_style
                    )
                )

            # ==========================
            # NORMAL TEXT
            # ==========================

            else:

                story.append(
                    Paragraph(
                        line,
                        self.body_style
                    )
                )

                story.append(
                    Spacer(1, 8)
                )

    def export_pdf(
        self,
        content,
        filename
    ):

        pdf_path = os.path.join(
            Settings.OUTPUT_DIR,
            filename
        )

        document = (
            SimpleDocTemplate(
                pdf_path,
                pagesize=letter,
                rightMargin=40,
                leftMargin=40,
                topMargin=50,
                bottomMargin=40
            )
        )

        story = []

        self.parse_content(
            content,
            story
        )

        document.build(story)

        return pdf_path

    def export_question_paper(
        self,
        questions
    ):

        return self.export_pdf(
            questions,
            "question_paper.pdf"
        )

    def export_answer_key(
        self,
        answers
    ):

        return self.export_pdf(
            answers,
            "answer_key.pdf"
        )