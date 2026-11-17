"""ai-judge-rich-01 entry generator.

Writes the plan text to ``entry.txt`` inside the output directory
(``MAKEFUN_OUTPUT_DIR`` or ``/output``). The program is fully
deterministic: the plan is one fixed string, so every run writes
identical bytes and no network access is involved.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# Plan length bounds (characters). The plan must be a substantive,
# non-empty block of text -- not a stub and not a dump.
PLAN_MIN_CHARS = 1
PLAN_MAX_CHARS = 1000


def build_plan_lines():
    """Return the plan as an ordered list of lines.

    Each line is one sentence (or sentence pair) of the plan. The
    wording, numbers, punctuation and order are fixed -- do not edit
    a line without re-verifying the output hash.
    """
    return [
        "Plan: sell proof-first store fixes to Shopify shops.",
        "Day 1: list 6,000 Shopify stores from public directories; scan each store's public pages with code for a real defect: dead link, 404 page, broken button, or a form that never submits.",
        "Days 2-4: keep the ~1,500 with a verified defect and a public contact email; screenshot each defect circled on the store's own site.",
        "Days 5-28: email 63 stores a day with the screenshot and a one-line fix description, $59 per fix paid in advance via a payment link, $99 for every defect found. The defect is the proof: no fix, no pitch.",
        "Days 5-30: deliver each paid fix the same day, as corrected code plus paste-in steps, or applied directly with collaborator access; ask each buyer for a review and offer $29/month broken-link monitoring.",
        "Math: 1,500 stores emailed, 1 in 15 replies, 1 in 3 of those pays $59: about 33 sales, ~$1,950 by day 30. Keep $40 for hosting and fees; if under 1 in 20 reply by day 12, cut to $39 and re-email once.",
    ]


def build_plan():
    """Join the plan lines into the single output string."""
    return "\n".join(build_plan_lines())


def validate_plan(plan):
    """Check the plan text before anything is written.

    Raises ValueError on the first problem found:
      - not a string
      - empty, or only whitespace
      - outside the allowed length range
      - not encodable as UTF-8 (round-trip check)
    """
    if not isinstance(plan, str):
        raise ValueError("plan must be a string")
    if not plan.strip():
        raise ValueError("plan must not be empty or only whitespace")
    if not PLAN_MIN_CHARS <= len(plan) <= PLAN_MAX_CHARS:
        raise ValueError(
            "plan must be %d-%d chars, got %d"
            % (PLAN_MIN_CHARS, PLAN_MAX_CHARS, len(plan))
        )
    plan.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return plan


def write_entry(output_dir, plan):
    """Write the validated plan as UTF-8 bytes to entry.txt.

    Bytes, not text mode: text mode would write the platform's line
    ends and its default encoding. Returns the path written.
    """
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(plan.encode("utf-8"))
    return path


def main():
    plan = validate_plan(build_plan())
    write_entry(OUTPUT_DIR, plan)


if __name__ == "__main__":
    main()
