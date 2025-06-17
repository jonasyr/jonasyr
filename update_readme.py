import random
import urllib.parse

statuses = [
    "Currently in a detached HEAD state.",
    "Rebasing life choices.",
    "Working tree not clean, neither is my desk.",
    "Checking out of reality."
]

badge_prefix = "https://img.shields.io/static/v1?label=Status&labelColor=EDEDED&color=8250DF&style=flat&message="

with open("README.md") as f:
    lines = f.readlines()

new_message = urllib.parse.quote(random.choice(statuses), safe='')
new_badge = f"![Status]({badge_prefix}{new_message})"

with open("README.md", "w") as f:
    for line in lines:
        if line.startswith("<img") or line.startswith("![Status]"):
            f.write(new_badge + "\n")
        else:
            f.write(line)
