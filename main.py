"""One-Line Office Joke Laugh-Off entry.

Writes a single original office joke to /output/entry.txt.
Python 3.13 standard library only.
"""

import os
import sys

LINE = "Someone replied-all 'please stop replying-all', and 212 people replied-all to agree."
# 84 chars / 84 bytes, no trailing newline. The punch is the irony:
# the protest against reply-all is itself answered by 212 reply-alls.
# Short text also helps the size tie-break.

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
