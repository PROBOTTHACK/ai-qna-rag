"""
Forms UI module.

Responsible for:
- PDF upload form
- Topic input
- User interaction forms
"""

from typing import Dict, Any

import streamlit as st


def render_generation_form() -> Dict[str, Any]:
    """
    Render question generation form.

    Returns:
        dict:
            Form input data.
    """

    st.subheader(
        "📂 Upload Study Material"
    )

    uploaded_files = (
        st.file_uploader(
            label="Upload PDF files",
            type=["pdf"],
            accept_multiple_files=True
        )
    )

    st.markdown("---")

    st.subheader(
        "📝 Question Generation"
    )

    topic = st.text_input(
        label="Enter Topic",
        placeholder=(
            "Example: Machine Learning"
        )
    )

    generate_button = st.button(
        "🚀 Generate Question Paper"
    )

    return {
        "uploaded_files": uploaded_files,
        "topic": topic,
        "generate_button": generate_button
    }