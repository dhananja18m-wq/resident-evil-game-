import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from ursina import *
from src.core.game_manager import GameManager

def main():
    app = Ursina(
        title='Project Eclipse: Horror Survival',
        fullscreen=False,
        size=(1280, 720)
    )
    
    game_manager = GameManager()
    
    def update():
        game_manager.update()
    
    app.run()

if __name__ == '__main__':
    main()
