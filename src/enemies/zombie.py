from ursina import *
import random

class Zombie(Entity):
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
        self.state = 'idle'
        self.idle_timer = random.uniform(2, 5)
        self.texture = 'white_cube'
        self.setup_model()
    
    def setup_model(self):
        assets_path = Path('assets/models')
        zombie_texture = assets_path / 'zombie_texture.png'
        if zombie_texture.exists():
            self.texture = str(zombie_texture)
    
    def update(self):
        distance_to_player = distance(self.position, self.player.entity.position)
        
        if distance_to_player < self.detection_range:
            self.state = 'chase'
        else:
            self.state = 'idle'
        
        if self.state == 'idle':
            self.update_idle()
        elif self.state == 'chase':
            self.update_chase(distance_to_player)
        
        self.attack_cooldown -= time.dt()
    
    def update_idle(self):
        self.idle_timer -= time.dt()
        if self.idle_timer <= 0:
            self.idle_timer = random.uniform(2, 5)
    
    def update_chase(self, distance_to_player):
        direction = normalize(self.player.entity.position - self.position)
        
        if distance_to_player > self.attack_range:
            self.position += direction * self.speed * time.dt()
            self.look_at(self.player.entity.position + Vec3(0, 0.5, 0))
        else:
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
        self.player.add_kill()
        destroy(self)
    
    def is_dead(self):
        return self.health <= 0
