from ursina import *
from src.core.game_manager import GameManager
from src.core.settings import GameSettings

def main():
    settings = GameSettings()
    resolution = settings.get_setting('resolution')
    fullscreen = settings.get_setting('fullscreen')
    
    app = Ursina(
        title='Project Eclipse: Horror Survival',
        fullscreen=fullscreen,
        size=resolution,
        background_color=color.black,
        vsync=True,
        show_ursina_splash=False
    )
    
    window.color = color.black
    
    game_manager = GameManager()
    
    def update_game():
        game_manager.update()
    
    def handle_input():
        if held_keys['esc']:
            if game_manager.current_state.name == 'GAMEPLAY':
                game_manager.return_to_menu()
    
    app.run()

if __name__ == '__main__':
    main()
