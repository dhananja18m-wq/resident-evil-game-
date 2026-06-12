from ursina import *
from pathlib import Path

class Environment:
    def __init__(self):
        self.entity = Entity()
        self.objects = []
        self.setup_lighting()
        self.setup_environment()
        self.setup_walls()
    
    def setup_lighting(self):
        light = DirectionalLight()
        light.direction = Vec3(1, -1, -1)
        
        sky = Sky()
        sky.color = color.dark_gray
        
        ambient = AmbientLight(color=color.dark_gray * 0.5)
    
    def setup_environment(self):
        sky_entity = Entity(
            model='sphere',
            scale=200,
            color=color.dark_gray,
            double_sided=True,
            z=100
        )
        
        fog(color=color.dark_gray, distance=200, density=0.02)
    
    def setup_walls(self):
        floor = Entity(
            model='cube',
            scale=(100, 1, 100),
            position=(0, -0.5, 0),
            color=color.dark_gray,
            collider='box'
        )
        self.objects.append(floor)
        
        wall_north = Entity(
            model='cube',
            scale=(100, 10, 2),
            position=(0, 5, -50),
            color=color.dark_gray,
            collider='box'
        )
        self.objects.append(wall_north)
        
        wall_south = Entity(
            model='cube',
            scale=(100, 10, 2),
            position=(0, 5, 50),
            color=color.dark_gray,
            collider='box'
        )
        self.objects.append(wall_south)
        
        wall_east = Entity(
            model='cube',
            scale=(2, 10, 100),
            position=(50, 5, 0),
            color=color.dark_gray,
            collider='box'
        )
        self.objects.append(wall_east)
        
        wall_west = Entity(
            model='cube',
            scale=(2, 10, 100),
            position=(-50, 5, 0),
            color=color.dark_gray,
            collider='box'
        )
        self.objects.append(wall_west)
        
        pillars = [
            (-20, 5, -20),
            (20, 5, -20),
            (-20, 5, 20),
            (20, 5, 20),
        ]
        
        for pos in pillars:
            pillar = Entity(
                model='cube',
                scale=(3, 10, 3),
                position=pos,
                color=color.dark_gray,
                collider='box'
            )
            self.objects.append(pillar)
    
    def cleanup(self):
        for obj in self.objects:
            if obj:
                destroy(obj)
        self.objects.clear()
