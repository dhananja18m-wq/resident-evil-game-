from enum import Enum

class GameState(Enum):
    MAIN_MENU = 1
    GAMEPLAY = 2
    GAME_OVER = 3
    PAUSED = 4
