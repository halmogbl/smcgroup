import os
import requests
from urllib.parse import urlparse

# Input file path
url_file = r'C:\Users\hmogbl\Development\smcgroupksa\smcgroup_rebuild\smcgroupksa.com\image_urls.txt'

# Output directory
output_dir = r'C:\Users\hmogbl\Development\smcgroupksa\smcgroup_rebuild\smcgroupksa.com\images'
os.makedirs(output_dir, exist_ok=True)

# Read URLs
with open(url_file, 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f if line.strip()]

# Download images
for url in urls:
    try:
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            print(f"⚠️ Skipping empty filename from URL: {url}")
            continue
        save_path = os.path.join(output_dir, filename)
        if os.path.exists(save_path):
            print(f"✅ Already exists: {filename}")
            continue
        print(f"⬇️ Downloading: {filename}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
