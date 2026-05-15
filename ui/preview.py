import streamlit as st


def render_question_preview(
    questions: str
):

    st.subheader(
        "📘 Generated Question Paper"
    )

    st.markdown("---")

    st.markdown(questions)


def render_answer_preview(
    answers: str
):

    st.subheader(
        "📗 Generated Answer Key"
    )

    st.markdown("---")

    st.markdown(answers)


def render_generation_status(
    status_message: str
):

    st.info(status_message)