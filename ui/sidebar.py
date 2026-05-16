import streamlit as st


def render_sidebar():

    st.sidebar.title(
        "⚙️ Exam Configuration"
    )

    # ==============================
    # SUBJECT DETAILS
    # ==============================

    st.sidebar.subheader(
        "📘 Exam Details"
    )

    subject_name = (
        st.sidebar.text_input(
            "Subject Name",
            value="Machine Learning"
        )
    )

    exam_duration = (
        st.sidebar.selectbox(
            "Exam Duration",
            [
                "1 Hour",
                "2 Hours",
                "3 Hours"
            ]
        )
    )

    difficulty = (
        st.sidebar.selectbox(
            "Difficulty Level",
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        )
    )

    st.sidebar.markdown("---")

    # ==============================
    # SECTION A
    # ==============================

    st.sidebar.subheader(
        "🟦 Section A"
    )

    section_a_type = (
        st.sidebar.selectbox(
            "Section A Type",
            [
                "MCQ",
                "Short Answer",
                "Long Answer"
            ],
            key="section_a_type"
        )
    )

    section_a_marks = (
        st.sidebar.selectbox(
            "Marks Per Question",
            [1, 2, 5],
            key="section_a_marks"
        )
    )

    section_a_questions = (
        st.sidebar.slider(
            "Number of Questions",
            1,
            10,
            5,
            key="section_a_questions"
        )
    )

    st.sidebar.markdown("---")

    # ==============================
    # SECTION B
    # ==============================

    st.sidebar.subheader(
        "🟨 Section B"
    )

    section_b_type = (
        st.sidebar.selectbox(
            "Section B Type",
            [
                "MCQ",
                "Short Answer",
                "Long Answer"
            ],
            key="section_b_type"
        )
    )

    section_b_marks = (
        st.sidebar.selectbox(
            "Marks Per Question",
            [2, 5, 10],
            key="section_b_marks"
        )
    )

    section_b_questions = (
        st.sidebar.slider(
            "Number of Questions",
            1,
            10,
            3,
            key="section_b_questions"
        )
    )

    st.sidebar.markdown("---")

    # ==============================
    # SECTION C
    # ==============================

    st.sidebar.subheader(
        "🟥 Section C"
    )

    section_c_type = (
        st.sidebar.selectbox(
            "Section C Type",
            [
                "MCQ",
                "Short Answer",
                "Long Answer"
            ],
            key="section_c_type"
        )
    )

    section_c_marks = (
        st.sidebar.selectbox(
            "Marks Per Question",
            [5, 10, 15],
            key="section_c_marks"
        )
    )

    section_c_questions = (
        st.sidebar.slider(
            "Number of Questions",
            1,
            10,
            2,
            key="section_c_questions"
        )
    )

    # ==============================
    # TOTAL MARKS
    # ==============================

    total_marks = (
        (section_a_marks * section_a_questions)
        +
        (section_b_marks * section_b_questions)
        +
        (section_c_marks * section_c_questions)
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"🎯 Total Marks: {total_marks}"
    )

    return {

        "subject_name": subject_name,

        "exam_duration": exam_duration,

        "difficulty": difficulty,

        "total_marks": total_marks,

        # SECTION A
        "section_a_type": section_a_type,
        "section_a_marks": section_a_marks,
        "section_a_questions": section_a_questions,

        # SECTION B
        "section_b_type": section_b_type,
        "section_b_marks": section_b_marks,
        "section_b_questions": section_b_questions,

        # SECTION C
        "section_c_type": section_c_type,
        "section_c_marks": section_c_marks,
        "section_c_questions": section_c_questions
    }