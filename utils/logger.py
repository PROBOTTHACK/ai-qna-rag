"""
Application logging utility.
"""

import logging
import os


class AppLogger:
    """
    Centralized logger manager.
    """

    def __init__(
        self,
        log_file="app.log"
    ):

        os.makedirs(
            "logs",
            exist_ok=True
        )

        log_path = os.path.join(
            "logs",
            log_file
        )

        self.logger = logging.getLogger(
            "AIQuestionGenerator"
        )

        self.logger.setLevel(
            logging.INFO
        )

        # Prevent duplicate handlers
        if not self.logger.handlers:

            file_handler = (
                logging.FileHandler(
                    log_path
                )
            )

            console_handler = (
                logging.StreamHandler()
            )

            formatter = logging.Formatter(
                (
                    "%(asctime)s - "
                    "%(levelname)s - "
                    "%(message)s"
                )
            )

            file_handler.setFormatter(
                formatter
            )

            console_handler.setFormatter(
                formatter
            )

            self.logger.addHandler(
                file_handler
            )

            self.logger.addHandler(
                console_handler
            )

    def get_logger(self):

        return self.logger