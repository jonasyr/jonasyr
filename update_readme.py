import random
import urllib.parse
import re

# 1) Your status list
statuses = [
    "Currently in a detached HEAD state.",
    "Rebasing life choices.",
    "Working tree not clean, neither is my desk.",
    "Checking out of reality.",
    "Commits are clean, but I’m not.",
    "Forked beyond recognition.",
    "Still resolving merge conflicts — in life.",
    "On main, but barely functioning.",
    "Staging my emotions for commit."
]

# 2) Build the new badge URL
base = (
    "https://img.shields.io/static/v1"
    "?label=Status"
    "&labelColor=24292F"
    "&color=8250DF"
    "&logo=github"
    "&logoColor=white"
    "&style=flat"
    "&message="
)
choice = random.choice(statuses)
badge_url = base + urllib.parse.quote(choice, safe='')

# 3) Construct the new HTML line
new_badge_line = f'<img alt="Status" src="{badge_url}" />'

# 4) Read in README and replace the *first* badge line, whatever its exact form
with open("README.md") as f:
    content = f.read()

# This regex matches either the HTML <img> badge or the Markdown ![Status](…) badge
pattern = re.compile(r'^(?:<img[^>]+alt="Status"[^>]*>|!\[Status\]\([^)]*\))\s*$', re.MULTILINE)

# Substitute once
new_content, count = pattern.subn(new_badge_line, content, count=1)

if count == 0:
    print("⚠️  No badge line found to replace.")
else:
    with open("README.md", "w") as f:
        f.write(new_content)
    print(f"✅ Replaced badge with: {choice}")

