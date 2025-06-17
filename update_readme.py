import random
import urllib.parse

# Read statuses
with open("statuses.txt", "r") as f:
    statuses = [line.strip() for line in f if line.strip()]
status = random.choice(statuses)

# URL-encode the status message
encoded_status = urllib.parse.quote(status)

# Construct the badge URL
badge_url = f"https://img.shields.io/badge/Status-{encoded_status}-blueviolet?style=flat-square&logo=git&logoColor=white"

# Read the README
with open("README.md", "r") as f:
    lines = f.readlines()

# Update the badge line
with open("README.md", "w") as f:
    in_badge_section = False
    for line in lines:
        if "<!--STATUS_BADGE_START-->" in line:
            f.write(line)
            in_badge_section = True
            continue
        if "<!--STATUS_BADGE_END-->" in line:
            f.write(f"![Status]({badge_url})\n")
            f.write(line)
            in_badge_section = False
            continue
        if not in_badge_section:
            f.write(line)
