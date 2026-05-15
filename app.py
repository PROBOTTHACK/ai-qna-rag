"""
Main Streamlit application.
"""

import streamlit as st

from config.settings import Settings
from ui.sidebar import render_sidebar


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

    st.subheader(
        "Current Settings"
    )

    st.json(settings)


if __name__ == "__main__":

    main()