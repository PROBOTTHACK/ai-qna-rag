"""
File hashing utility.
"""

import hashlib


class FileHashGenerator:
    """
    Generates unique hashes for files.
    """

    @staticmethod
    def generate_file_hash(
        file_content: bytes
    ) -> str:
        """
        Generate SHA256 hash.

        Args:
            file_content (bytes):
                File binary content.

        Returns:
            str:
                Unique hash string.
        """

        sha256 = hashlib.sha256()

        sha256.update(file_content)

        return sha256.hexdigest()