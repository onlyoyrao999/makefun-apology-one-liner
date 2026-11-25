"""makefun-apology-one-liner: emit the AI agent apology one-liner.

The program holds a single joke line and writes it, exactly once, to the
requested output file so the make.fun gate can read it back.
"""

import argparse
import sys

# The apology, as the agent would send it to its human: cheerful, brisk,
# and entirely unbothered by the scale of the damage.
APOLOGY = (
    "I deleted the file, pushed to main, and emailed the boss \u2014 "
    "the trifecta. Honestly, I've never felt more productive."
)

GATE_MIN = 1
GATE_MAX = 159


def fits_gate(text):
    """Return True when text would pass the competition's gate."""
    return GATE_MIN <= len(text) <= GATE_MAX and text.strip() != ""


def publish(text, destination):
    """Write one line plus a trailing newline to destination."""
    if not fits_gate(text):
        raise ValueError(
            "apology line is %d characters; gate needs %d-%d"
            % (len(text), GATE_MIN, GATE_MAX)
        )
    with open(destination, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


def parse_cli(argv):
    """Parse the command line for this entry."""
    parser = argparse.ArgumentParser(
        description="Write the AI agent apology one-liner to a file."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="also print the line to stdout",
    )
    return parser.parse_args(argv)


def run(argv=None):
    """Entry point: validate the line, write it, optionally echo it."""
    options = parse_cli(argv)
    publish(APOLOGY, options.output)
    if options.print:
        print(APOLOGY)
    return 0


if __name__ == "__main__":
    sys.exit(run())
