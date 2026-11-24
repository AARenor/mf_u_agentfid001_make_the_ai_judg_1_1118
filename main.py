"""Write one short office joke for make.fun bounty u-agentfid001."""

import os
import sys
from pathlib import Path

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def output_dir() -> Path:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text must be 1..280 characters, got {len(text)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
