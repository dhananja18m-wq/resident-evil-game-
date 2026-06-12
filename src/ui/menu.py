from ursina import *
from pathlib import Path

class MainMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.entity = Entity(model='cube', scale=0)  # Create dummy entity for parenting
        self.ui_elements = []
        self.setup_background()
        self.setup_ui()
    
    def setup_background(self):
        """Setup background similar to Resident Evil menu"""
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
            # Fallback: Dark background with gradient effect
            self.background = Entity(
                model='quad',
                color=color.black,
                scale=(16, 9),
                z=10
            )
            
            # Add atmospheric overlay
            overlay = Entity(
                model='quad',
                color=color.rgba(0, 0, 0, 0.3),
                scale=(16, 9),
                z=11
            )
    
    def setup_ui(self):
        """Setup menu UI with Resident Evil style layout"""
        
        # Title - PROJECT ECLIPSE
        title = Text(
            text='PROJECT ECLIPSE',
            font='arial',
            scale=4,
            position=(-0.35, 0.4),
            color=color.light_gray,
            origin=(0, 0)
        )
        self.ui_elements.append(title)
        
        # Subtitle - HORROR SURVIVAL
        subtitle = Text(
            text='HORROR SURVIVAL',
            font='arial',
            scale=1.5,
            position=(-0.35, 0.28),
            color=color.white,
            origin=(0, 0)
        )
        self.ui_elements.append(subtitle)
        
        # Menu button positions (left side, vertically aligned)
        menu_x = -0.4
        menu_y_start = 0.15
        menu_spacing = -0.08
        
        # NEW GAME button
        self.new_game_btn = Button(
            text='NEW GAME',
            position=(menu_x, menu_y_start),
            scale=(0.2, 0.06),
            color=color.rgba(50, 50, 50, 0.8),
            highlight_color=color.rgba(200, 0, 0, 0.8),
            pressed_color=color.rgba(139, 0, 0, 0.9),
            text_origin=(0, 0),
            text_scale=1.2
        )
        self.new_game_btn.on_click = self.on_new_game
        self.ui_elements.append(self.new_game_btn)
        
        # LOAD GAME button
        self.load_game_btn = Button(
            text='LOAD GAME',
            position=(menu_x, menu_y_start + menu_spacing),
            scale=(0.2, 0.06),
            color=color.rgba(50, 50, 50, 0.8),
            highlight_color=color.rgba(200, 0, 0, 0.8),
            pressed_color=color.rgba(139, 0, 0, 0.9),
            text_origin=(0, 0),
            text_scale=1.2
        )
        self.ui_elements.append(self.load_game_btn)
        
        # OPTIONS button
        self.options_btn = Button(
            text='OPTIONS',
            position=(menu_x, menu_y_start + menu_spacing * 2),
            scale=(0.2, 0.06),
            color=color.rgba(50, 50, 50, 0.8),
            highlight_color=color.rgba(200, 0, 0, 0.8),
            pressed_color=color.rgba(139, 0, 0, 0.9),
            text_origin=(0, 0),
            text_scale=1.2
        )
        self.ui_elements.append(self.options_btn)
        
        # SETTINGS button
        self.settings_btn = Button(
            text='SETTINGS',
            position=(menu_x, menu_y_start + menu_spacing * 3),
            scale=(0.2, 0.06),
            color=color.rgba(50, 50, 50, 0.8),
            highlight_color=color.rgba(200, 0, 0, 0.8),
            pressed_color=color.rgba(139, 0, 0, 0.9),
            text_origin=(0, 0),
            text_scale=1.2
        )
        self.ui_elements.append(self.settings_btn)
        
        # QUIT button
        self.quit_btn = Button(
            text='QUIT',
            position=(menu_x, menu_y_start + menu_spacing * 4),
            scale=(0.2, 0.06),
            color=color.rgba(50, 50, 50, 0.8),
            highlight_color=color.rgba(200, 0, 0, 0.8),
            pressed_color=color.rgba(139, 0, 0, 0.9),
            text_origin=(0, 0),
            text_scale=1.2
        )
        self.quit_btn.on_click = self.on_quit
        self.ui_elements.append(self.quit_btn)
        
        # Bottom instruction text
        instruction = Text(
            text='Start a new game.',
            font='arial',
            scale=1,
            position=(0, -0.45),
            color=color.light_gray,
            origin=(0, 0)
        )
        self.ui_elements.append(instruction)
        
        # Bottom right hint
        hint = Text(
            text='[CLICK] CONFIRM',
            font='arial',
            scale=0.8,
            position=(0.25, -0.45),
            color=color.light_gray,
            origin=(0, 0)
        )
        self.ui_elements.append(hint)
    
    def on_new_game(self):
        """Handle new game button click"""
        self.game_manager.start_game()
    
    def on_quit(self):
        """Handle quit button click"""
        self.game_manager.quit_game()
    
    def cleanup(self):
        """Cleanup menu elements"""
        for element in self.ui_elements:
            try:
                destroy(element)
            except:
                pass
        
        try:
            destroy(self.background)
        except:
            pass
        
        try:
            destroy(self.entity)
        except:
            pass
