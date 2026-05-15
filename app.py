"""
Main Streamlit application.
"""

import streamlit as st

from config.settings import Settings

from ui.sidebar import render_sidebar
from ui.forms import render_generation_form


def initialize_app():
    """
    Configure Streamlit app.
    """

    st.set_page_config(
        page_title=Settings.APP_TITLE,
        page_icon="📘",
        layout="wide"
    )


def main():
    """
    Main application function.
    """

    initialize_app()

    # ==============================
    # SIDEBAR
    # ==============================

    settings = render_sidebar()

    # ==============================
    # MAIN PAGE
    # ==============================

    st.title(
        Settings.APP_TITLE
    )

    st.write(
        Settings.APP_DESCRIPTION
    )

    st.markdown("---")

    # ==============================
    # RENDER FORM
    # ==============================

    form_data = (
        render_generation_form()
    )

    # ==============================
    # DISPLAY FORM DATA
    # ==============================

    if form_data["generate_button"]:

        st.success(
            "Generation request received."
        )

        st.write(
            "### Submitted Information"
        )

        st.json({
            "topic": form_data["topic"],
            "uploaded_files": (
                len(
                    form_data[
                        "uploaded_files"
                    ]
                )
                if form_data[
                    "uploaded_files"
                ]
                else 0
            ),
            "settings": settings
        })


if __name__ == "__main__":

    main()