"""Advanced gameplay mechanics and systems"""

from ursina import *
import math

class DamageSystem:
    def __init__(self):
        self.damage_notifications = []
    
    def apply_damage(self, target, amount, source=None):
        if hasattr(target, 'take_damage'):
            target.take_damage(amount)
            self.create_damage_notification(target.position, amount)
    
    def create_damage_notification(self, position, amount):
        notification = Entity(
            model='quad',
            color=color.transparent,
            position=position
        )
        text = Text(
            text=f'-{int(amount)}',
            position=position,
            color=color.red,
            scale=1,
            lifetime=0.5
        )

class LootDropSystem:
    def __init__(self):
        self.loot_drops = []
    
    def drop_ammo(self, position, amount=15):
        loot = Entity(
            model='sphere',
            color=color.yellow,
            scale=0.3,
            position=position,
            collider='sphere'
        )
        self.loot_drops.append(('ammo', loot, amount))
    
    def drop_health(self, position, amount=25):
        loot = Entity(
            model='cube',
            color=color.red,
            scale=0.3,
            position=position,
            collider='box'
        )
        self.loot_drops.append(('health', loot, amount))
    
    def check_pickups(self, player):
        for loot_type, loot_entity, amount in self.loot_drops[:]:
            if distance(player.entity.position, loot_entity.position) < 2:
                if loot_type == 'ammo':
                    player.reserve_ammo += amount
                elif loot_type == 'health':
                    player.health = min(player.max_health, player.health + amount)
                destroy(loot_entity)
                self.loot_drops.remove((loot_type, loot_entity, amount))

class WaveManager:
    def __init__(self):
        self.current_wave = 0
        self.wave_timer = 0
        self.wave_interval = 10
        self.difficulty_multiplier = 1.0
    
    def update_wave(self, active_enemies):
        if len(active_enemies) == 0:
            self.wave_timer -= time.dt()
            if self.wave_timer <= 0:
                self.start_next_wave()
    
    def start_next_wave(self):
        self.current_wave += 1
        self.difficulty_multiplier = 1.0 + (self.current_wave * 0.15)
        self.wave_timer = self.wave_interval

class ScoreSystem:
    def __init__(self):
        self.score = 0
        self.multiplier = 1.0
        self.combo_counter = 0
        self.combo_timer = 0
        self.combo_threshold = 3.0
    
    def add_kill(self, points=100):
        self.combo_counter += 1
        self.combo_timer = self.combo_threshold
        self.score += int(points * self.multiplier)
        self.update_multiplier()
    
    def update_multiplier(self):
        if self.combo_counter >= 5:
            self.multiplier = 1.5
        elif self.combo_counter >= 3:
            self.multiplier = 1.25
        else:
            self.multiplier = 1.0
    
    def update(self):
        self.combo_timer -= time.dt()
        if self.combo_timer <= 0:
            self.combo_counter = 0
            self.multiplier = 1.0
