"""Enhanced zombie AI with better behavior states"""

from ursina import *
from pathlib import Path
import random

class ZombieStates:
    IDLE = 'idle'
    ALERT = 'alert'
    CHASE = 'chase'
    ATTACK = 'attack'
    DEAD = 'dead'

class AdvancedZombie(Entity):
    def __init__(self, position, player):
        super().__init__(
            model='cube',
            color=color.dark_gray,
            scale=(0.7, 1.8, 0.7),
            position=position,
            collider='box'
        )
        self.player = player
        self.health = 30
        self.max_health = 30
        self.damage = 10
        self.detection_range = 50
        self.attack_range = 3
        self.speed = 15
        self.attack_cooldown = 0
        self.attack_delay = 1.5
        self.state = ZombieStates.IDLE
        self.idle_timer = random.uniform(2, 5)
        self.path_update_timer = 0
        self.path_update_interval = 0.5
        self.last_player_position = None
        self.sound_timer = 0
    
    def update(self):
        distance_to_player = distance(self.position, self.player.entity.position)
        
        if distance_to_player < self.detection_range:
            if self.state == ZombieStates.IDLE:
                self.state = ZombieStates.ALERT
                self.play_alert_sound()
            self.last_player_position = self.player.entity.position
        else:
            if self.state != ZombieStates.IDLE:
                self.state = ZombieStates.IDLE
        
        if self.state == ZombieStates.IDLE:
            self.update_idle()
        elif self.state == ZombieStates.ALERT:
            self.state = ZombieStates.CHASE
        elif self.state == ZombieStates.CHASE:
            self.update_chase(distance_to_player)
        elif self.state == ZombieStates.ATTACK:
            self.update_attack(distance_to_player)
        
        self.attack_cooldown = max(0, self.attack_cooldown - time.dt())
        self.sound_timer -= time.dt()
    
    def update_idle(self):
        self.idle_timer -= time.dt()
        if self.idle_timer <= 0:
            self.idle_timer = random.uniform(2, 5)
    
    def update_chase(self, distance_to_player):
        if distance_to_player < self.attack_range:
            self.state = ZombieStates.ATTACK
            return
        
        direction = normalize(self.player.entity.position - self.position)
        self.position += direction * self.speed * time.dt()
        self.look_at(self.player.entity.position + Vec3(0, 0.5, 0))
        
        if self.sound_timer <= 0:
            self.play_growl_sound()
            self.sound_timer = 3
    
    def update_attack(self, distance_to_player):
        if distance_to_player > self.attack_range * 1.5:
            self.state = ZombieStates.CHASE
            return
        
        self.look_at(self.player.entity.position + Vec3(0, 0.5, 0))
        
        if self.attack_cooldown <= 0:
            self.attack()
    
    def attack(self):
        self.player.take_damage(self.damage)
        self.attack_cooldown = self.attack_delay
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
    
    def die(self):
        self.state = ZombieStates.DEAD
        self.player.add_kill()
        destroy(self)
    
    def play_alert_sound(self):
        pass
    
    def play_growl_sound(self):
        pass
    
    def is_dead(self):
        return self.state == ZombieStates.DEAD or self.health <= 0
