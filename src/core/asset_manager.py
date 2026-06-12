from ursina import *
from pathlib import Path
import os

class AssetManager:
    def __init__(self):
        self.assets_path = Path('assets')
        self.textures = {}
        self.models = {}
        self.sounds = {}
        self.load_assets()
    
    def load_assets(self):
        self.load_textures()
        self.load_models()
        self.load_sounds()
    
    def load_textures(self):
        textures_path = self.assets_path / 'textures'
        if textures_path.exists():
            for texture_file in textures_path.glob('*.png'):
                key = texture_file.stem
                self.textures[key] = str(texture_file)
    
    def load_models(self):
        models_path = self.assets_path / 'models'
        if models_path.exists():
            for model_file in models_path.glob('*'):
                if model_file.suffix in ['.obj', '.fbx', '.gltf']:
                    key = model_file.stem
                    self.models[key] = str(model_file)
    
    def load_sounds(self):
        sounds_path = self.assets_path / 'sounds'
        if sounds_path.exists():
            for sound_file in sounds_path.glob('*.wav'):
                key = sound_file.stem
                self.sounds[key] = str(sound_file)
    
    def get_texture(self, name):
        return self.textures.get(name, None)
    
    def get_model(self, name):
        return self.models.get(name, None)
    
    def get_sound(self, name):
        return self.sounds.get(name, None)
