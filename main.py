import os
# One-liner entry (140 chars max): the line below is the entire submission.
# Writes the line to /output/entry.txt.
LINE = "I skipped that corner on purpose. The dust there has seniority, and I respect the hierarchy."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
