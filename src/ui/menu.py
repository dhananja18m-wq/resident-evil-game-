from ursina import *
from pathlib import Path

class MainMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.entity = Entity(model='cube', scale=0)  # Create dummy entity for parenting
        self.setup_background()
        self.setup_ui()
    
    def setup_background(self):
        assets_path = Path('assets/ui')
        background_path = assets_path / 'horror_background.png'
        
        if background_path.exists():
            self.background = Entity(
                model='quad',
                texture=str(background_path),
                scale=(16, 9),
                z=10
            )
        else:
            self.background = Entity(
                model='quad',
                color=color.black,
                scale=(16, 9),
                z=10
            )
    
    def setup_ui(self):
        title = Text(
            text='PROJECT ECLIPSE',
            font='assets/fonts/arial.ttf' if Path('assets/fonts/arial.ttf').exists() else None,
            scale=3,
            position=(0, 0.3),
            color=color.red
        )
        
        subtitle = Text(
            text='HORROR SURVIVAL',
            scale=1.5,
            position=(0, 0.15),
            color=color.white
        )
        
        button_y_start = 0
        button_spacing = -0.15
        
        self.new_game_btn = Button(
            text='NEW GAME',
            position=(0, button_y_start),
            scale=0.15,
            color=color.dark_gray,
            highlight_color=color.red,
            pressed_color=color.dark_red
        )
        self.new_game_btn.on_click = self.on_new_game
        
        self.settings_btn = Button(
            text='SETTINGS',
            position=(0, button_y_start + button_spacing),
            scale=0.15,
            color=color.dark_gray,
            highlight_color=color.red,
            pressed_color=color.dark_red
        )
        
        self.quit_btn = Button(
            text='QUIT',
            position=(0, button_y_start + button_spacing * 2),
            scale=0.15,
            color=color.dark_gray,
            highlight_color=color.red,
            pressed_color=color.dark_red
        )
        self.quit_btn.on_click = self.on_quit
    
    def on_new_game(self):
        self.game_manager.start_game()
    
    def on_quit(self):
        self.game_manager.quit_game()
