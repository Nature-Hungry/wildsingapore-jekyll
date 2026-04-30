#!/usr/bin/env python3
"""
Script to populate entry files with custom attributes from entryAttributes.json
"""

import json
import os
import re
import sys
from pathlib import Path

def read_attributes():
    """Read the entryAttributes.json file"""
    try:
        with open('entryAttributes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: entryAttributes.json not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing entryAttributes.json: {e}")
        sys.exit(1)

def convert_path(windows_path):
    """Convert Windows path to Unix path"""
    # Replace backslashes with forward slashes
    unix_path = windows_path.replace('\\', '/')
    return unix_path

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    # Match content between first and second --- markers
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        return frontmatter, body
    return None, content

def parse_frontmatter(frontmatter):
    """Parse YAML frontmatter into a dictionary"""
    lines = frontmatter.strip().split('\n')
    data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            elif value.startswith('[') and value.endswith(']'):
                inner = value[1:-1].strip()
                if inner:
                    data[key] = [item.strip() for item in inner.split(',')]
                    continue
                else:
                    data[key] = []
                    continue
            data[key] = value
    return data

def frontmatter_to_string(data):
    """Convert frontmatter dictionary back to YAML string"""
    lines = []
    for key, value in data.items():
        if isinstance(value, list):
            attrs_str = ', '.join(str(a) for a in value)
            lines.append(f'{key}: [{attrs_str}]')
        else:
            text = str(value)
            if text == '':
                lines.append(f'{key}: ""')
            elif any(c in text for c in '[]{}:,') or text.startswith(' ') or text.endswith(' '):
                lines.append(f'{key}: "{text}"')
            else:
                lines.append(f'{key}: {text}')
    return '\n'.join(lines)

def update_file(filepath, entry_data):
    """Update a markdown file with JSON-backed frontmatter fields"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Warning: File not found: {filepath}")
        return False
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    frontmatter, body = extract_frontmatter(content)
    
    if frontmatter is None:
        print(f"Warning: No frontmatter found in {filepath}")
        return False
    
    fm_dict = parse_frontmatter(frontmatter)
    for key, value in entry_data.items():
        fm_dict[key] = value
    
    new_frontmatter = frontmatter_to_string(fm_dict)
    new_content = f'---\n{new_frontmatter}\n---\n{body}'
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def main():
    """Main function"""
    attributes = read_attributes()
    
    # Count files
    total = len(attributes)
    updated = 0
    skipped = 0
    
    print(f"Processing {total} entries...")
    
    for file_path, attr_data in attributes.items():
        # Convert Windows path to Unix path and use markdown extension
        unix_path = convert_path(file_path)
        if unix_path.lower().endswith('.htm'):
            unix_path = unix_path[:-4] + '.md'
        
        # Prepend _entries/ directory if not already present
        if not unix_path.startswith('_entries/'):
            full_path = f'_entries/{unix_path}'
        else:
            full_path = unix_path
        
        # Check if file exists
        if not os.path.exists(full_path):
            print(f"Skipping: {full_path} (not found)")
            skipped += 1
            continue
        
        if update_file(full_path, attr_data):
            updated += 1
        else:
            skipped += 1
    
    print(f"\nCompleted!")
    print(f"Updated: {updated}")
    print(f"Skipped: {skipped}")

if __name__ == '__main__':
    main()
