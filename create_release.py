#!/usr/bin/env python3
"""
Automated downloader for Project Eclipse game repository.
Creates a downloadable ZIP file with all game files.
"""

import os
import sys
import subprocess
import zipfile
from pathlib import Path
from datetime import datetime

def create_zip_archive():
    """
    Creates a ZIP archive of the entire game directory.
    Excludes unnecessary files like __pycache__, .git, venv, etc.
    """
    
    exclude_dirs = {
        '__pycache__',
        '.git',
        '.github',
        'venv',
        'env',
        '.venv',
        '.pytest_cache',
        '.egg-info',
        'dist',
        'build'
    }
    
    exclude_files = {
        '.gitignore',
        '.gitkeep',
        '.DS_Store',
        'Thumbs.db',
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '.Python'
    }
    
    project_name = 'PROJECT_ECLIPSE_Horror_Survival'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = f'{project_name}_{timestamp}.zip'
    
    print(f"\n{'='*60}")
    print(f"Creating ZIP Archive: {zip_filename}")
    print(f"{'='*60}\n")
    
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            base_path = Path('.')
            
            for root, dirs, files in os.walk('.'):
                # Remove excluded directories from traversal
                dirs[:] = [d for d in dirs if d not in exclude_dirs]
                
                # Skip root directories
                rel_root = Path(root).relative_to(base_path)
                
                # Add files
                for file in files:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(base_path)
                    
                    # Check if file should be included
                    skip_file = False
                    for exclude_pattern in exclude_files:
                        if exclude_pattern.startswith('*'):
                            if file.endswith(exclude_pattern[1:]):
                                skip_file = True
                        elif file == exclude_pattern:
                            skip_file = True
                    
                    if not skip_file:
                        print(f"✓ Adding: {rel_path}")
                        zipf.write(file_path, arcname=rel_path)
        
        file_size_mb = os.path.getsize(zip_filename) / (1024 * 1024)
        print(f"\n{'='*60}")
        print(f"✓ Archive created successfully!")
        print(f"  Filename: {zip_filename}")
        print(f"  Size: {file_size_mb:.2f} MB")
        print(f"{'='*60}\n")
        
        return zip_filename
    
    except Exception as e:
        print(f"✗ Error creating archive: {e}")
        return None

def create_readme_for_zip():
    """
    Creates a README file with quick start instructions for the ZIP.
    """
    
    readme_content = """PROJECT ECLIPSE: Horror Survival
===============================

Quick Start Guide:

1. Extract this ZIP file to your desired location

2. Open a terminal/command prompt in the extracted directory

3. Create a virtual environment:
   Windows: python -m venv venv && venv\\Scripts\\activate
   macOS/Linux: python3 -m venv venv && source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the game:
   python main.py

For detailed instructions, see:
- QUICKSTART.md - Quick setup guide
- SETUP.md - Detailed installation
- README.md - Full documentation
- DEVELOPER.md - Technical details

Game Controls:
- WASD: Move
- Mouse: Look around
- Left Click: Shoot
- R: Reload
- F: Flashlight
- ESC: Menu

Requirements:
- Python 3.13+
- 2GB RAM
- 500MB storage

Have fun! 🧟‍♂️
"""
    
    with open('ZIP_README.txt', 'w') as f:
        f.write(readme_content)
    print("Created ZIP_README.txt")

def main():
    """
    Main function for archive creation.
    """
    
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║   PROJECT ECLIPSE: Horror Survival                     ║
    ║   Repository Downloader                               ║
    ║                                                        ║
    ║   Creates a downloadable ZIP archive of the game       ║
    ╚════════════════════════════════════════════════════════╝
    """)
    
    # Create README
    create_readme_for_zip()
    
    # Create ZIP archive
    zip_file = create_zip_archive()
    
    if zip_file:
        print("\n✓ All done!")
        print(f"\nYour game archive is ready: {zip_file}")
        print("\nNext steps:")
        print("1. Download the ZIP file")
        print("2. Extract it to your desired location")
        print("3. Follow the instructions in QUICKSTART.md")
        print("4. Run: python main.py")
        return 0
    else:
        print("\n✗ Failed to create archive")
        return 1

if __name__ == '__main__':
    sys.exit(main())
