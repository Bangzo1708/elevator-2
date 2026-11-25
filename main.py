#!/usr/bin/env python3
"""Two Robots in an Elevator — round 2 entry.

Writes one line of awkward robot small talk to /output/entry.txt.

Candidate variants considered (all different from the round 1 entry,
which counted shared elevator rides — that counting trope is retired):

  V1 (CHOSEN): "Nice weather we're having. I checked: it is 41 degrees
       and raining. I said it anyway."
       Why it wins: it takes THE classic elevator small-talk opener and
       lets robot literalism wreck it. The machine logic is visible
       (it actually checked the weather), the awkwardness lands in the
       confession "I said it anyway" — forced courtesy, admitted out
       loud — and the turn surprises on the first read: the robot knows
       the line is false and says it anyway, exactly like a human
       trapped in an elevator would.

  V2: "Your charging port is showing. Sorry. My proximity sensor made
       me say it out loud."
       Strong machine logic and awkwardness, but the innuendo does half
       the work and the laugh depends on the reader filling in a rude
       reading; weaker on first-read clarity than V1.

  V3: "I was going to compliment your firmware, but my small-talk
       subroutine crashed at 'hello'."
       Good robot voice, but "my subroutine crashed" is a well-worn
       robot joke; less original and the awkwardness is told rather
       than shown, unlike V1's confession.

Selection criteria applied: most robot (visible machine logic, not
human), most awkward (the forced courtesy lands), funniest on first
read, most original (no "do you come here often", no ride-counting).
V1 wins on all four.
"""

import argparse
import os
import sys

ENTRY = "Nice weather we're having. I checked: it is 41 degrees and raining. I said it anyway."


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the elevator entry line.")
    parser.add_argument(
        "--out",
        default="/output/entry.txt",
        help="Destination path (default: /output/entry.txt)",
    )
    args = parser.parse_args(argv)

    line = ENTRY.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise SystemExit("entry violates the 1-200 character single-line gate")

    directory = os.path.dirname(args.out)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(args.out, 0o644)
    # Read back and confirm what landed on disk is exactly the entry.
    with open(args.out, encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        raise SystemExit("read-back mismatch: entry on disk differs from ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
