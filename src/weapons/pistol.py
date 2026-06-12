from ursina import *
from pathlib import Path

class Pistol:
    def __init__(self):
        self.position = Vec3(0.3, -0.5, 0.5)
        self.rotation = Vec3(0, 0, 0)
        self.muzzle_flash_timer = 0
        self.setup_model()
    
    def setup_model(self):
        assets_path = Path('assets/models')
        pistol_model = assets_path / 'pistol.obj'
        
        if pistol_model.exists():
            self.gun_model = Entity(
                model=str(pistol_model),
                scale=0.1,
                position=self.position,
                parent=camera
            )
        else:
            self.gun_model = Entity(
                model='cube',
                scale=(0.1, 0.3, 0.3),
                position=self.position,
                color=color.dark_gray,
                parent=camera
            )
    
    def update(self, player_pos, player_rot):
        self.muzzle_flash_timer -= time.dt()
        
        if self.gun_model:
            self.gun_model.world_position = player_pos + Vec3(0.3, -0.5, 0.5)
            self.gun_model.world_rotation = player_rot
    
    def shoot(self, direction):
        self.show_muzzle_flash()
        self.play_shoot_sound()
        return self.raycast_hit(direction)
    
    def show_muzzle_flash(self):
        muzzle = Entity(
            model='sphere',
            scale=0.1,
            color=color.yellow,
            position=self.gun_model.position + Vec3(0, 0, 0.3),
            lifetime=0.05
        )
    
    def play_shoot_sound(self):
        assets_path = Path('assets/sounds')
        shoot_sound = assets_path / 'pistol_shot.wav'
        if shoot_sound.exists():
            audio_player = Audio(
                sound=str(shoot_sound),
                volume=0.5,
                loop=False,
                autoplay=True
            )
    
    def raycast_hit(self, direction):
        camera_pos = camera.position
        hit_info = raycast(origin=camera_pos, direction=direction, distance=1000)
        return hit_info
