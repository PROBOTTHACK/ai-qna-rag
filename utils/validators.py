"""
Validation utilities.
"""

import os

from config.settings import Settings


class Validators:
    """
    Handles input validation.
    """

    @staticmethod
    def validate_topic(
        topic: str
    ) -> bool:
        """
        Validate topic input.
        """

        if not topic:
            return False

        if len(topic.strip()) < 3:
            return False

        return True

    @staticmethod
    def validate_uploaded_files(
        uploaded_files
    ) -> bool:
        """
        Validate uploaded PDF files.
        """

        if not uploaded_files:
            return False

        return True

    @staticmethod
    def validate_pdf_extension(
        filename: str
    ) -> bool:
        """
        Check PDF extension.
        """

        return filename.lower().endswith(
            ".pdf"
        )

    @staticmethod
    def validate_file_size(
        file
    ) -> bool:
        """
        Validate uploaded file size.
        """

        max_size = (
            Settings.MAX_FILE_SIZE_MB
            * 1024
            * 1024
        )

        return file.size <= max_size

    @staticmethod
    def validate_pdf_file(
        file
    ):
        """
        Complete PDF validation.
        """

        if not Validators.validate_pdf_extension(
            file.name
        ):

            return (
                False,
                "Only PDF files are allowed."
            )

        if not Validators.validate_file_size(
            file
        ):

            return (
                False,
                (
                    "File exceeds maximum "
                    "allowed size."
                )
            )

        return (
            True,
            "Valid PDF file."
        )