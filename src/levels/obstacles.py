from ursina import *
from pathlib import Path

class Obstacle(Entity):
    def __init__(self, position, scale, obstacle_type='crate'):
        super().__init__(
            model='cube',
            position=position,
            scale=scale,
            collider='box'
        )
        self.obstacle_type = obstacle_type
        self.setup_appearance()
    
    def setup_appearance(self):
        if self.obstacle_type == 'crate':
            self.color = color.brown
        elif self.obstacle_type == 'barrel':
            self.color = color.dark_red
            self.model = 'cylinder'
        elif self.obstacle_type == 'debris':
            self.color = color.dark_gray

class DynamicObject(Entity):
    def __init__(self, position, object_type='barrel'):
        super().__init__(
            model='cube',
            position=position,
            scale=(1, 1, 1),
            collider='box'
        )
        self.object_type = object_type
        self.health = 50
        self.destroyed = False
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.destroy_object()
    
    def destroy_object(self):
        self.destroyed = True
        destroy(self)
