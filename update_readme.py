import random

statuses = [
    "Currently in a detached HEAD state.",
    "Rebasing life choices.",
    "Working tree not clean, neither is my desk.",
    "Checking out of reality."
]

badge_template = "![Status](https://img.shields.io/badge/status-{}-blueviolet)"

with open("README.md", "r") as file:
    lines = file.readlines()

with open("README.md", "w") as file:
    for line in lines:
        if line.startswith("![Status]"):
            new_status = random.choice(statuses).replace(" ", "%20").replace(",", "%2C")
            file.write(badge_template.format(new_status) + "\n")
        else:
            file.write(line)
