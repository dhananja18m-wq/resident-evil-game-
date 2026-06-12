from ursina import *

class HUD:
    def __init__(self, player):
        self.player = player
        self.setup_ui()
    
    def setup_ui(self):
        self.health_text = Text(
            text='Health: 100',
            position=(-0.45, 0.45),
            scale=1,
            color=color.green
        )
        
        self.ammo_text = Text(
            text='Ammo: 30 | Reserve: 120',
            position=(0.35, 0.45),
            scale=1,
            color=color.yellow
        )
        
        self.kills_text = Text(
            text='Kills: 0',
            position=(-0.45, 0.35),
            scale=1,
            color=color.white
        )
        
        self.objective_text = Text(
            text='Eliminate all zombies',
            position=(0, -0.45),
            scale=1.2,
            color=color.red
        )
        
        self.crosshair = Text(
            text='+',
            position=(0, 0),
            scale=1.5,
            color=color.white
        )
    
    def update(self):
        self.health_text.text = f'Health: {max(0, int(self.player.health))}'
        self.ammo_text.text = f'Ammo: {self.player.current_ammo} | Reserve: {self.player.reserve_ammo}'
        self.kills_text.text = f'Kills: {self.player.kills}'
        
        if self.player.health <= 30:
            self.health_text.color = color.red
        elif self.player.health <= 60:
            self.health_text.color = color.orange
        else:
            self.health_text.color = color.green
    
    def cleanup(self):
        destroy(self.health_text)
        destroy(self.ammo_text)
        destroy(self.kills_text)
        destroy(self.objective_text)
        destroy(self.crosshair)
