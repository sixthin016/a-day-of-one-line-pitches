"""A Day of One-Line Pitches — make.fun entry.

Writes one sentence (1-240 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The sentence must convince a friend who has never coded to let an AI agent
build their first app idea on make.fun, in a single read.

Runs with no network, no randomness and no clock: the same input always
produces the same file, so two grader runs are byte-identical.
"""

import os
import sys

# One sentence, 202 characters. Plain words, second person, a concrete
# time promise (tonight), and the risk removed (no code, no cost, walk away).
PITCH = (
    "Just describe the app you've been dreaming about in your own words, "
    "and let an AI agent on make.fun build you a first version to try "
    "tonight \u2014 no code, no cost, and nothing to lose if you don't love it."
)


def main() -> int:
    text = PITCH
    if not 1 <= len(text) <= 240:
        print(f"pitch is {len(text)} characters, must be 1-240", file=sys.stderr)
        return 1
    if not text.strip():
        print("pitch is blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
