from ursina import *
import json
from pathlib import Path

class GameSettings:
    def __init__(self):
        self.settings_file = Path('settings.json')
        self.settings = {
            'resolution': (1280, 720),
            'fullscreen': False,
            'mouse_sensitivity': 2.0,
            'sound_volume': 0.5,
            'music_volume': 0.3,
            'difficulty': 'normal',
            'brightness': 1.0
        }
        self.load_settings()
    
    def load_settings(self):
        if self.settings_file.exists():
            try:
                with open(self.settings_file, 'r') as f:
                    saved = json.load(f)
                    self.settings.update(saved)
            except:
                pass
    
    def save_settings(self):
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except:
            pass
    
    def get_setting(self, key):
        return self.settings.get(key, None)
    
    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()
