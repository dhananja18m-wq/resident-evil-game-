from ursina import *
from src.enemies.zombie import Zombie
import random

class AIController:
    def __init__(self):
        self.enemies = []
    
    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def remove_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
    
    def update_all(self):
        for enemy in self.enemies:
            if enemy and not enemy.is_dead():
                enemy.update()
    
    def get_active_enemies(self):
        return [e for e in self.enemies if e and not e.is_dead()]
