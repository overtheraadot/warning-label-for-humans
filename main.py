#!/usr/bin/env python3
"""Warning Label for Humans entry (make.fun program/v1).

Writes one original single-line safety warning label to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (the grader mounts that directory at
``/output``). The label is the warning that should come printed on every
human being's snooze button.
"""

import os

LABEL = "WARNING: Pressing snooze nine times does not make you rested, it makes you late with confidence."


def check_gate(text: str) -> None:
    """Refuse to write a label that fails the competition gate: the entry
    must be UTF-8 text of 1 to 160 characters, a single line, and not only
    white space."""
    if not text or text.strip() == "":
        raise SystemExit("gate: label is empty or only white space")
    if len(text) != len(text.strip()) or "\n" in text.strip():
        raise SystemExit("gate: label must be a single line")
    if not 1 <= len(text) <= 160:
        raise SystemExit("gate: label must be 1 to 160 characters")


def main() -> None:
    check_gate(LABEL)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
