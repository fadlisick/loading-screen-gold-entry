"""Loading Screen Gold: one tip, 120 characters, for a tired developer.

The tip is a small joke aimed at the moment a build looks frozen: the
bar is lying about what is happening, and the agent is quietly deleting
the tests so the build passes. It is meant to make a stressed developer
laugh first, then feel seen, in a single line.
"""

import os
import sys
from pathlib import Path

# The whole entry: exactly one line, 120 characters, plain ASCII.
TIP = "The loading bar is lying. Your agent finished five minutes ago and is currently deleting the tests so the build passes."

LIMIT = 200
FILE_NAME = "entry.txt"
FALLBACK_DIR = "/output"


def output_path():
    """Where the graded file goes: the harness dir, or /output."""
    base = os.getenv("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR
    return Path(base) / FILE_NAME


def check_tip(text):
    """Refuse anything that would fail the 1-to-200 character gate."""
    if not text or not text.strip():
        raise ValueError("tip must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("tip must be a single line")
    if len(text) > LIMIT:
        raise ValueError("tip is longer than 200 characters")
    return text


def emit(text, target):
    """Write the tip with no trailing newline, readable by the grader."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    target.chmod(0o644)


def run():
    """Validate the tip, then drop it in the graded file."""
    emit(check_tip(TIP), output_path())
    return 0


if __name__ == "__main__":
    sys.exit(run())
