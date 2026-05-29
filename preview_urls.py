#!/usr/bin/env python3
"""Preview what URLs will be changed (without modifying files)."""

import os
from pathlib import Path

OLD_URL = "http://www.wildsingapore.com/wildfacts/"
TARGET_EXTENSIONS = {'.md', '.html', '.yml', '.yaml', '.json'}
SKIP_DIRS = {'_site', '.git', '.github', 'node_modules', '.jekyll-cache'}

count = 0
files_with_urls = []

for root, dirs, files in os.walk("."):
    root_path = Path(root)
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    
    for filename in files:
        file_path = root_path / filename
        if file_path.suffix.lower() in TARGET_EXTENSIONS:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if OLD_URL in content:
                    occurrences = content.count(OLD_URL)
                    files_with_urls.append((str(file_path), occurrences))
                    count += occurrences
            except:
                pass

print(f"\n🔍 PREVIEW: Files containing '{OLD_URL}':\n")
for filepath, occurrences in files_with_urls:
    print(f"  {filepath}: {occurrences} occurrence(s)")

print(f"\n📊 Total occurrences: {count}")
print(f"📁 Total files to modify: {len(files_with_urls)}\n")