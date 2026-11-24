#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about a small everyday annoyance to
<output_dir>/entry.txt. Standard library only, no network, deterministic.
"""

import os

RANT = (
    "My smoke detector waits until 3 a.m. -- the one hour I am actually "
    "asleep -- to announce its battery is dying, chirping like a cricket "
    "with a grudge. I stood on a chair at 3:12 a.m., half-naked, ripping "
    "it off the ceiling while it screamed at me for trying to help. It now "
    "lives in a drawer. It is still chirping. I respect the commitment. "
    "I hate the bird."
)


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1-400 chars, not blank."""
    if not text or text.strip() == "":
        raise SystemExit("entry is empty or whitespace-only")
    if len(text) > 400:
        raise SystemExit(f"entry is {len(text)} chars, over the 400 cap")


def main() -> None:
    validate(RANT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(RANT)
    # Read back and confirm the file on disk is exactly the validated text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != RANT:
        raise SystemExit("entry.txt on disk does not match the validated rant")


if __name__ == "__main__":
    main()
