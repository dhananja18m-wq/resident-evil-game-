from ursina import *

class ParticleEffect:
    def __init__(self, position, effect_type='blood', lifetime=0.5):
        self.position = position
        self.effect_type = effect_type
        self.lifetime = lifetime
        self.age = 0
        self.particles = []
        self.create_effect()
    
    def create_effect(self):
        if self.effect_type == 'blood':
            for _ in range(5):
                particle = Entity(
                    model='sphere',
                    scale=0.1,
                    color=color.red,
                    position=self.position,
                    lifetime=self.lifetime
                )
                self.particles.append(particle)
        elif self.effect_type == 'muzzle_flash':
            particle = Entity(
                model='sphere',
                scale=0.15,
                color=color.yellow,
                position=self.position,
                lifetime=0.1
            )
            self.particles.append(particle)
    
    def update(self):
        self.age += time.dt()
        return self.age < self.lifetime
