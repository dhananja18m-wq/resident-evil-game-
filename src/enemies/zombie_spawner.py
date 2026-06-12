from ursina import *
from src.enemies.zombie import Zombie
import random

class ZombieSpawner:
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.zombies = []
        self.spawn_points = [
            Vec3(-10, 0, 0),
            Vec3(10, 0, 0),
            Vec3(0, 0, -10),
            Vec3(0, 0, 10),
            Vec3(-5, 0, -5),
            Vec3(5, 0, 5),
        ]
        self.wave = 0
        self.zombies_spawned = 0
        self.zombies_per_wave = 3
        self.wave_spawn_timer = 0
        self.wave_spawn_interval = 2
    
    def start_wave(self):
        self.wave += 1
        self.zombies_spawned = 0
        self.zombies_per_wave = 3 + (self.wave - 1)
        self.wave_spawn_timer = 0
    
    def update(self):
        self.zombies = [z for z in self.zombies if z and not z.is_dead()]
        
        for zombie in self.zombies:
            zombie.update()
        
        if len(self.zombies) == 0 and self.zombies_spawned >= self.zombies_per_wave:
            self.start_wave()
        
        if self.zombies_spawned < self.zombies_per_wave:
            self.wave_spawn_timer += time.dt()
            if self.wave_spawn_timer >= self.wave_spawn_interval:
                self.spawn_zombie()
                self.wave_spawn_timer = 0
    
    def spawn_zombie(self):
        spawn_point = random.choice(self.spawn_points)
        zombie = Zombie(spawn_point, self.player)
        self.zombies.append(zombie)
        self.zombies_spawned += 1
    
    def cleanup(self):
        for zombie in self.zombies:
            if zombie:
                destroy(zombie)
        self.zombies.clear()
