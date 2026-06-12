from ursina import *
import math

class InputManager:
    def __init__(self):
        self.keys_pressed = {}
        self.mouse_position = Vec2(0, 0)
        self.mouse_clicked = False
        self.sensitivity = 2.0
    
    def update(self):
        self.mouse_position = Vec2(mouse.x(), mouse.y())
        self.mouse_clicked = mouse.left_pressed
    
    def is_key_pressed(self, key):
        return held_keys[key]
    
    def get_mouse_position(self):
        return self.mouse_position
    
    def get_mouse_clicked(self):
        return self.mouse_clicked
    
    def get_movement_input(self):
        direction = Vec3(0, 0, 0)
        if held_keys['w']:
            direction.z -= 1
        if held_keys['s']:
            direction.z += 1
        if held_keys['a']:
            direction.x -= 1
        if held_keys['d']:
            direction.x += 1
        return direction.normalized() if direction.length() > 0 else Vec3(0, 0, 0)
