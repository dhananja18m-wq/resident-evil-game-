from ursina import *
from src.weapons.pistol import Pistol

class PlayerController:
    def __init__(self, position=(0, 1.7, 0)):
        self.entity = camera
        self.entity.position = position
        self.speed = 20
        self.sprint_speed = 35
        self.health = 100
        self.max_health = 100
        self.kills = 0
        self.current_ammo = 30
        self.reserve_ammo = 120
        self.magazine_size = 30
        self.flashlight_enabled = False
        self.velocity = Vec3(0, 0, 0)
        self.gravity = 35
        self.jump_force = 20
        self.grounded = False
        self.weapon = Pistol()
        self.setup_collision()
        self.setup_flashlight()
    
    def setup_collision(self):
        self.collider = collider.BoxCollider(
            entity=self.entity,
            size=(0.5, 1.7, 0.5),
            center=(0, 0, 0)
        )
    
    def setup_flashlight(self):
        self.flashlight = PointLight(
            position=(0, 0, 0),
            color=color.white,
            radius=50
        )
        self.flashlight.enabled = False
    
    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.update_flashlight_position()
        self.weapon.update(self.entity.position, self.entity.rotation)
    
    def handle_input(self):
        current_speed = self.sprint_speed if held_keys['shift'] else self.speed
        direction = Vec3(0, 0, 0)
        
        if held_keys['w']:
            direction += self.entity.forward()
        if held_keys['s']:
            direction -= self.entity.forward()
        if held_keys['a']:
            direction -= self.entity.right()
        if held_keys['d']:
            direction += self.entity.right()
        
        if direction != Vec3(0, 0, 0):
            direction = normalize(direction)
            self.entity.position += direction * current_speed * time.dt()
        
        if held_keys['space'] and self.grounded:
            self.velocity.y = self.jump_force
            self.grounded = False
        
        if held_keys['f']:
            self.flashlight_enabled = not self.flashlight_enabled
            self.flashlight.enabled = self.flashlight_enabled
        
        if mouse.left_pressed:
            self.weapon.shoot(self.entity.forward())
        
        if held_keys['r']:
            self.reload()
    
    def apply_gravity(self):
        self.velocity.y -= self.gravity * time.dt()
        self.entity.y += self.velocity.y * time.dt()
        
        if self.entity.y <= 1.7:
            self.entity.y = 1.7
            self.velocity.y = 0
            self.grounded = True
    
    def update_flashlight_position(self):
        self.flashlight.position = self.entity.position + Vec3(0.3, -0.3, 0.5)
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    
    def shoot(self):
        if self.current_ammo > 0:
            self.current_ammo -= 1
            return True
        return False
    
    def reload(self):
        needed = self.magazine_size - self.current_ammo
        reload_amount = min(needed, self.reserve_ammo)
        self.current_ammo += reload_amount
        self.reserve_ammo -= reload_amount
    
    def add_kill(self):
        self.kills += 1
    
    def is_dead(self):
        return self.health <= 0
