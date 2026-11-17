import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: sell proof-first store fixes to Shopify shops.",
        "Day 1: list 6,000 Shopify stores from public directories; scan each store's public pages with code for a real defect: dead link, 404 page, broken button, or a form that never submits.",
        "Days 2-4: keep the ~1,500 with a verified defect and a public contact email; screenshot each defect circled on the store's own site.",
        "Days 5-28: email 60 stores a day with the screenshot and a one-line fix description, $59 per fix paid in advance via a payment link, $99 for every defect found. The defect is the proof: no fix, no pitch.",
        "Days 5-30: deliver each paid fix the same day, as corrected code plus paste-in steps, or applied directly with collaborator access; ask each buyer for a review and offer $29/month broken-link monitoring.",
        "Math: 1,500 stores emailed, 1 in 15 replies, 1 in 3 of those pays $59: about 33 sales, ~$1,950 by day 30. Keep $40 for hosting and fees; drop any channel with no sale in a week.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding. The plan is one fixed string, so both runs
# of this program write identical bytes with no network.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
