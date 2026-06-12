from ursina import *

class AudioManager:
    def __init__(self):
        self.sounds = {}
        self.music = None
        self.sound_volume = 0.5
        self.music_volume = 0.3
    
    def load_sound(self, name, path):
        try:
            self.sounds[name] = Audio(sound=path, loop=False, autoplay=False, volume=self.sound_volume)
        except:
            pass
    
    def load_music(self, path):
        try:
            self.music = Audio(sound=path, loop=True, autoplay=False, volume=self.music_volume)
        except:
            pass
    
    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()
    
    def play_music(self):
        if self.music:
            self.music.play()
    
    def stop_music(self):
        if self.music:
            self.music.stop()
    
    def set_sound_volume(self, volume):
        self.sound_volume = max(0, min(1, volume))
        for sound in self.sounds.values():
            sound.volume = self.sound_volume
    
    def set_music_volume(self, volume):
        self.music_volume = max(0, min(1, volume))
        if self.music:
            self.music.volume = self.music_volume
