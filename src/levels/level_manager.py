from ursina import *
from src.player.controller import PlayerController
from src.enemies.zombie_spawner import ZombieSpawner
from src.ui.hud import HUD
from src.ui.game_over import GameOverScreen
from src.levels.environment import Environment

class LevelManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.player = PlayerController()
        self.hud = HUD(self.player)
        self.environment = Environment()
        self.spawner = ZombieSpawner(self.player, self)
        self.game_over_screen = None
        self.game_active = True
        self.spawner.start_wave()
    
    def update(self):
        if not self.game_active:
            return
        
        self.player.update()
        self.spawner.update()
        self.hud.update()
        
        if self.player.is_dead():
            self.game_over()
    
    def show_game_over(self):
        self.game_over_screen = GameOverScreen(
            self.game_manager,
            self.player.kills,
            self.spawner.wave
        )
    
    def game_over(self):
        self.game_active = False
        self.show_game_over()
    
    def cleanup(self):
        self.hud.cleanup()
        self.spawner.cleanup()
        self.environment.cleanup()
        destroy(self.environment.entity)
