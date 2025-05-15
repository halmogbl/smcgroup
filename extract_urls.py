import os
import re

# Input files
base_dir = r"C:\Users\hmogbl\Development\smcgroupksa\smcgroup_rebuild\smcgroupksa.com"
paths = [
    "index.html",
    "about-us\\index.html",
    "services\\index.html",
    "contact-us\\index.html"
]

# Output file
output_file = os.path.join(base_dir, "image_urls.txt")

# Regex to match direct or archived URLs
pattern = re.compile(
    r"(?:https:\/\/web\.archive\.org\/web\/[0-9a-zA-Z]+\/(?:im_)?\/)?(https:\/\/smcgroupksa\.com\/wp-content\/uploads\/[^\s\"'>]+)"
)

# Set to store unique URLs
found_urls = set()

for rel_path in paths:
    file_path = os.path.join(base_dir, rel_path)
    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        matches = pattern.findall(html)
        found_urls.update(matches)

# Save to file
with open(output_file, "w", encoding="utf-8") as f:
    for url in sorted(found_urls):
        f.write(url + "\n")

print(f"✅ Extracted {len(found_urls)} URLs to {output_file}")
