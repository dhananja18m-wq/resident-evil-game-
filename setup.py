#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

def check_python_version():
    if sys.version_info < (3, 13):
        print("WARNING: Python 3.13+ is recommended")
        print(f"Your version: {sys.version_info.major}.{sys.version_info.minor}")
        print("Some features may not work correctly")

def install_dependencies():
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully!")

def create_asset_directories():
    print("Creating asset directories...")
    directories = [
        'assets/textures',
        'assets/models',
        'assets/sounds',
        'assets/ui'
    ]
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created {directory}")

def verify_structure():
    print("\nVerifying project structure...")
    required_files = [
        'main.py',
        'requirements.txt',
        'README.md',
        'src/core/game_manager.py',
        'src/player/controller.py',
        'src/enemies/zombie.py',
        'src/weapons/pistol.py',
        'src/ui/menu.py',
        'src/levels/level_one.py'
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} (MISSING)")
            all_exist = False
    
    if all_exist:
        print("\n✓ All required files present!")
    else:
        print("\n✗ Some files are missing!")
    
    return all_exist

def main():
    print("=" * 50)
    print("PROJECT ECLIPSE: Horror Survival Setup")
    print("=" * 50)
    print()
    
    check_python_version()
    print()
    
    create_asset_directories()
    print()
    
    try:
        install_dependencies()
    except subprocess.CalledProcessError:
        print("Failed to install dependencies")
        return False
    print()
    
    if verify_structure():
        print()
        print("=" * 50)
        print("Setup complete! Run 'python main.py' to start")
        print("=" * 50)
        return True
    else:
        print()
        print("Setup incomplete. Check missing files.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
