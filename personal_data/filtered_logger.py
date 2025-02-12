#!/usr/bin/env python3
"""
File contains function that obfuscates text
"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Redacts specified fields in a message.

    Args:
        fields (list): List of field names to redact.
        redaction (str): Replacement text for redacted values.
        message (str): The input message containing key-value pairs.
        separator (str): The separator between key-value pairs (not used in regex).

    Returns:
        str: The message with specified fields redacted.
    """
    for field in fields:
        message = re.sub(f'{field}=[^;]+', f'{field}={redaction}', message)
    return message
