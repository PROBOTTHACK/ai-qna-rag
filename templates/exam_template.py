"""
Exam paper template system.
"""


class ExamTemplate:
    """
    Creates professional exam paper layouts.
    """

    def __init__(
        self,
        subject_name: str,
        exam_duration: str,
        total_marks: int
    ):

        self.subject_name = (
            subject_name
        )

        self.exam_duration = (
            exam_duration
        )

        self.total_marks = (
            total_marks
        )

    def build_exam_header(
        self
    ) -> str:
        """
        Build exam header.
        """

        return f"""
# MID SEMESTER EXAMINATION

## Subject: {self.subject_name}

### Duration: {self.exam_duration}

### Maximum Marks: {self.total_marks}

---

## Instructions

- Read all questions carefully
- Answer all questions
- Maintain proper steps
- Marks are indicated where necessary

---
"""

    def build_section(
        self,
        section_title: str,
        marks: int,
        questions: str
    ) -> str:
        """
        Create exam section.
        """

        return f"""
# {section_title}

### ({marks} Marks Each)

{questions}

---
"""

    def build_complete_paper(
        self,
        mcq_questions: str = "",
        short_questions: str = "",
        long_questions: str = ""
    ) -> str:
        """
        Build complete exam paper.
        """

        paper = (
            self.build_exam_header()
        )

        # ==========================
        # SECTION A
        # ==========================

        if mcq_questions.strip():

            paper += self.build_section(
                section_title="SECTION A",
                marks=2,
                questions=mcq_questions
            )

        # ==========================
        # SECTION B
        # ==========================

        if short_questions.strip():

            paper += self.build_section(
                section_title="SECTION B",
                marks=5,
                questions=short_questions
            )

        # ==========================
        # SECTION C
        # ==========================

        if long_questions.strip():

            paper += self.build_section(
                section_title="SECTION C",
                marks=10,
                questions=long_questions
            )

        return paper