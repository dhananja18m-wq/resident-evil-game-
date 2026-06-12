#!/usr/bin/env python3
"""
Project Eclipse: Horror Survival
A polished horror FPS game prototype using Ursina Engine 8.3.0 and Python 3.13
"""

import sys
from pathlib import Path

print("""
╔════════════════════════════════════════════╗
║   PROJECT ECLIPSE: HORROR SURVIVAL         ║
║   Initializing Game Engine...              ║
╚════════════════════════════════════════════╝
""")

try:
    from ursina import *
    print("✓ Ursina Engine loaded")
except ImportError as e:
    print(f"✗ Failed to load Ursina: {e}")
    print("Install with: pip install -r requirements.txt")
    sys.exit(1)

try:
    from src.core.game_manager import GameManager
    from src.core.settings import GameSettings
    print("✓ Game systems loaded")
except ImportError as e:
    print(f"✗ Failed to load game systems: {e}")
    sys.exit(1)

def main():
    """Main game entry point"""
    
    settings = GameSettings()
    resolution = settings.get_setting('resolution')
    fullscreen = settings.get_setting('fullscreen')
    
    print(f"✓ Settings loaded")
    print(f"  Resolution: {resolution[0]}x{resolution[1]}")
    print(f"  Fullscreen: {fullscreen}")
    print()
    
    try:
        app = Ursina(
            title='Project Eclipse: Horror Survival',
            fullscreen=fullscreen,
            size=resolution,
            background_color=color.black,
            vsync=True,
            show_ursina_splash=False
        )
        print("✓ Game window created")
    except Exception as e:
        print(f"✗ Failed to create game window: {e}")
        sys.exit(1)
    
    window.color = color.black
    
    try:
        game_manager = GameManager()
        print("✓ Game manager initialized")
    except Exception as e:
        print(f"✗ Failed to initialize game manager: {e}")
        sys.exit(1)
    
    print()
    print("╔════════════════════════════════════════════╗")
    print("║         GAME READY - PRESS START            ║")
    print("╚════════════════════════════════════════════╝")
    print()
    
    def update_game():
        try:
            game_manager.update()
        except Exception as e:
            print(f"Error during game update: {e}")
    
    app.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
