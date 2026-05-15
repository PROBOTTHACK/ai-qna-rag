"""
Preview UI module.

Responsible for:
- Displaying generated outputs
- Question paper preview
- Answer key preview
"""

import streamlit as st


def render_question_preview(
    questions: str
):
    """
    Display generated question paper.

    Args:
        questions (str):
            Generated question paper.
    """

    st.subheader(
        "📘 Generated Question Paper"
    )

    st.markdown("---")

    st.text_area(
        label="Question Paper",
        value=questions,
        height=400
    )


def render_answer_preview(
    answers: str
):
    """
    Display generated answer key.

    Args:
        answers (str):
            Generated answer key.
    """

    st.subheader(
        "📗 Generated Answer Key"
    )

    st.markdown("---")

    st.text_area(
        label="Answer Key",
        value=answers,
        height=400
    )


def render_generation_status(
    status_message: str
):
    """
    Display generation status.

    Args:
        status_message (str):
            Status message.
    """

    st.info(status_message)