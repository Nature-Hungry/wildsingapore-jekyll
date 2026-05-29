#!/usr/bin/env python3
"""
Script to update image URLs across the Wild Singapore Jekyll project.
Replaces old wildsingapore.com URLs with Backblaze B2 URLs.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
OLD_URL = "http://www.wildsingapore.com/wildfacts/"
NEW_URL = "https://f003.backblazeb2.com/file/naturehungry/"

# File types to scan (these are the ones that might contain image URLs)
TARGET_EXTENSIONS = {
    '.md',           # Markdown files
    '.html',         # HTML files (layouts, includes)
    '.yml',          # YAML data files
    '.yaml',         # YAML data files (alternative)
    '.json'          # JSON data files (if any)
}

# Directories to skip (don't want to modify build output)
SKIP_DIRS = {
    '_site',         # Generated site
    '.git',          # Git directory
    '.github',       # GitHub directory
    'node_modules',  # If you have Node packages
    '.jekyll-cache'  # Jekyll cache
}

class URLUpdater:
    def __init__(self, old_url, new_url, project_root="."):
        self.old_url = old_url
        self.new_url = new_url
        self.project_root = Path(project_root)
        self.files_changed = []
        self.replacements_made = 0
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.backup_dir = self.project_root / f"backup_{self.timestamp}"
        
    def should_process_directory(self, dir_path):
        """Check if directory should be processed."""
        dir_name = dir_path.name
        return dir_name not in SKIP_DIRS
    
    def should_process_file(self, file_path):
        """Check if file should be processed based on extension."""
        return file_path.suffix.lower() in TARGET_EXTENSIONS
    
    def backup_file(self, file_path):
        """Create a backup of the file before modifying."""
        # Create backup directory if it doesn't exist
        self.backup_dir.mkdir(exist_ok=True)
        
        # Create mirrored backup path
        relative_path = file_path.relative_to(self.project_root)
        backup_path = self.backup_dir / relative_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file to backup location
        shutil.copy2(file_path, backup_path)
        return backup_path
    
    def process_file(self, file_path):
        """Process a single file: read, replace, write back."""
        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if old URL exists in file
            if self.old_url not in content:
                return 0  # No changes needed
            
            # Create backup before modifying
            self.backup_file(file_path)
            
            # Count replacements in this file
            count_before = content.count(self.old_url)
            
            # Replace URLs
            new_content = content.replace(self.old_url, self.new_url)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            # Log this file
            self.files_changed.append({
                'path': str(file_path.relative_to(self.project_root)),
                'replacements': count_before
            })
            
            return count_before
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
            return 0
    
    def run(self):
        """Walk through all directories and process files."""
        print(f"\n🔄 Starting URL replacement...")
        print(f"📁 Project root: {self.project_root.absolute()}")
        print(f"🔗 Old URL: {self.old_url}")
        print(f"🔗 New URL: {self.new_url}")
        print(f"💾 Backup location: {self.backup_dir}\n")
        
        # Walk through directory tree
        for root, dirs, files in os.walk(self.project_root):
            root_path = Path(root)
            
            # Remove directories we don't want to process
            dirs[:] = [d for d in dirs if self.should_process_directory(root_path / d)]
            
            # Process each file
            for filename in files:
                file_path = root_path / filename
                
                if self.should_process_file(file_path):
                    replacements = self.process_file(file_path)
                    self.replacements_made += replacements
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print a summary of changes."""
        print("\n" + "="*60)
        print("📊 SUMMARY")
        print("="*60)
        print(f"✅ Files processed: {len(self.files_changed)}")
        print(f"🔄 Total replacements: {self.replacements_made}")
        
        if self.files_changed:
            print(f"\n📝 Files changed:")
            for file_info in self.files_changed:
                print(f"  • {file_info['path']}")
                print(f"    ({file_info['replacements']} replacements)")
        
        print(f"\n💾 Backup saved to: {self.backup_dir}")
        print("\n✨ Done! Review the changes and commit to git.")
        print("="*60 + "\n")

if __name__ == "__main__":
    updater = URLUpdater(OLD_URL, NEW_URL)
    updater.run()