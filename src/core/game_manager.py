from ursina import *
from src.ui.menu import MainMenu
from src.levels.level_manager import LevelManager
from src.core.game_state import GameState

class GameManager:
    def __init__(self):
        self.current_state = GameState.MAIN_MENU
        self.main_menu = None
        self.level_manager = None
        self.init_main_menu()
    
    def init_main_menu(self):
        self.main_menu = MainMenu(self)
        self.current_state = GameState.MAIN_MENU
    
    def start_game(self):
        if self.main_menu:
            destroy(self.main_menu.entity)
        self.level_manager = LevelManager(self)
        self.current_state = GameState.GAMEPLAY
    
    def return_to_menu(self):
        if self.level_manager:
            self.level_manager.cleanup()
        self.init_main_menu()
    
    def game_over(self):
        self.current_state = GameState.GAME_OVER
        if self.level_manager:
            self.level_manager.show_game_over()
    
    def quit_game(self):
        application.quit()
    
    def update(self):
        if self.current_state == GameState.GAMEPLAY and self.level_manager:
            self.level_manager.update()
