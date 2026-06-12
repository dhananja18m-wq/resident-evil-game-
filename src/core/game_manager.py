from ursina import *
from src.ui.menu import MainMenu
from src.levels.level_one import LevelOne
from src.core.game_state import GameState

class GameManager:
    def __init__(self):
        self.current_state = GameState.MAIN_MENU
        self.main_menu = None
        self.current_level = None
        self.init_main_menu()
    
    def init_main_menu(self):
        self.main_menu = MainMenu(self)
        self.current_state = GameState.MAIN_MENU
    
    def start_game(self):
        if self.main_menu:
            destroy(self.main_menu.entity)
        self.current_level = LevelOne(self)
        self.current_state = GameState.GAMEPLAY
    
    def return_to_menu(self):
        if self.current_level:
            self.current_level.cleanup()
        self.init_main_menu()
    
    def game_over(self):
        self.current_state = GameState.GAME_OVER
        if self.current_level:
            self.current_level.show_game_over()
    
    def quit_game(self):
        application.quit()
    
    def update(self):
        if self.current_state == GameState.GAMEPLAY and self.current_level:
            self.current_level.update()
