import random
import urllib.parse

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
new_line = f'<img alt="Status" src="{badge_url}" />'

with open("README.md") as f:
    lines = f.readlines()

with open("README.md", "w") as f:
    for line in lines:
        if line.strip().startswith("<img alt=\"Status\""):
            f.write(new_line + "\n")
        else:
            f.write(line)

print(f"Chosen status: {choice}")
print(f"New badge line: {new_line}")

