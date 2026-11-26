"""MakeFun competition entry: Buy the ticket."""

LINE = "Buy the ticket. You still remember the trip; you won't remember the price."

# Write the entry file
import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write(LINE)