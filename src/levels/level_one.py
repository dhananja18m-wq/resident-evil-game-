from ursina import *
from src.player.controller import PlayerController
from src.enemies.zombie_spawner import ZombieSpawner
from src.ui.hud import HUD
from src.ui.game_over import GameOverScreen
from src.levels.environment import Environment
from src.levels.obstacles import Obstacle
from pathlib import Path

class LevelOne:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.player = PlayerController(position=(0, 1.7, 0))
        self.hud = HUD(self.player)
        self.environment = Environment()
        self.spawner = ZombieSpawner(self.player, self)
        self.obstacles = []
        self.game_over_screen = None
        self.game_active = True
        self.setup_obstacles()
        self.spawner.start_wave()
    
    def setup_obstacles(self):
        obstacle_positions = [
            (-15, 0, 0),
            (15, 0, 0),
            (0, 0, -15),
            (0, 0, 15),
            (-10, 0, -10),
            (10, 0, 10),
        ]
        
        for pos in obstacle_positions:
            obstacle = Obstacle(pos, (2, 2, 2), 'crate')
            self.obstacles.append(obstacle)
    
    def update(self):
        if not self.game_active:
            return
        
        self.player.update()
        self.spawner.update()
        self.hud.update()
        
        self.check_zombie_attacks()
        self.check_player_shots()
        
        if self.player.is_dead():
            self.game_over()
    
    def check_player_shots(self):
        if mouse.left_pressed:
            hit_info = self.player.weapon.raycast_hit(camera.forward())
            if hit_info.hit:
                for zombie in self.spawner.zombies:
                    if zombie and hit_info.entity == zombie:
                        zombie.take_damage(25)
                        break
    
    def check_zombie_attacks(self):
        for zombie in self.spawner.zombies:
            if zombie and distance(zombie.position, self.player.entity.position) < 3:
                zombie.attack()
    
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
        for obstacle in self.obstacles:
            if obstacle:
                destroy(obstacle)
        destroy(self.environment.entity)
