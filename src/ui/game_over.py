from ursina import *

class GameOverScreen:
    def __init__(self, game_manager, kills, waves):
        self.game_manager = game_manager
        self.kills = kills
        self.waves = waves
        self.entity = Entity()
        self.setup_ui()
    
    def setup_ui(self):
        overlay = Entity(
            model='quad',
            color=color.black,
            scale=(16, 9),
            z=20
        )
        overlay.color_scale = (1, 1, 1, 0.8)
        
        title = Text(
            text='GAME OVER',
            scale=3,
            position=(0, 0.3),
            color=color.red,
            parent=self.entity
        )
        
        stats = Text(
            text=f'Kills: {self.kills}\nWaves Survived: {self.waves}',
            scale=1.5,
            position=(0, 0),
            color=color.white,
            parent=self.entity
        )
        
        self.restart_btn = Button(
            text='RESTART',
            position=(0, -0.2),
            scale=0.15,
            color=color.dark_gray,
            highlight_color=color.red,
            parent=self.entity
        )
        self.restart_btn.on_click = self.on_restart
        
        self.menu_btn = Button(
            text='MAIN MENU',
            position=(0, -0.35),
            scale=0.15,
            color=color.dark_gray,
            highlight_color=color.red,
            parent=self.entity
        )
        self.menu_btn.on_click = self.on_menu
    
    def on_restart(self):
        destroy(self.entity)
        self.game_manager.start_game()
    
    def on_menu(self):
        destroy(self.entity)
        self.game_manager.return_to_menu()
