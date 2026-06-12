# Installation Instructions

## Prerequisites
- Python 3.13 or higher
- pip package manager
- 2GB+ free disk space

## Setup Steps

### 1. Clone the Repository
```bash
git clone https://github.com/dhananja18m-wq/resident-evil-game-.git
cd resident-evil-game-
```

### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Game Assets
Place your game assets in the following directories:
- **Textures**: `assets/textures/` (PNG files)
- **Models**: `assets/models/` (OBJ, FBX, or GLTF files)
- **Sounds**: `assets/sounds/` (WAV files)
- **UI Elements**: `assets/ui/` (PNG files)

### 5. Run the Game
```bash
python main.py
```

## Game Controls

| Action | Control |
|--------|----------|
| Move Forward | W |
| Move Backward | S |
| Move Left | A |
| Move Right | D |
| Sprint | Left Shift |
| Jump | Space |
| Look Around | Mouse Movement |
| Shoot | Left Mouse Button |
| Reload | R |
| Toggle Flashlight | F |

## Required Asset Files

To fully use the game, place the following assets in their respective directories:

### Textures
- `horror_background.png` - Main menu background
- `zombie_texture.png` - Zombie appearance texture

### Sounds
- `pistol_shot.wav` - Gunshot sound
- `zombie_growl.wav` - Zombie attack sound
- `menu_music.wav` - Main menu background music
- `level_ambient.wav` - In-game atmosphere sound

### Models (Optional)
- `pistol.obj` - First-person pistol model
- `zombie.fbx` - Zombie 3D model

## Troubleshooting

### ImportError: No module named 'ursina'
Make sure you have activated the virtual environment and installed requirements:
```bash
pip install -r requirements.txt
```

### Game runs but assets don't load
Verify assets are in the correct directories and use matching filenames.

### Poor performance
Reduce texture quality or lower the zombie spawn rate in `src/enemies/zombie_spawner.py`

## Game Features

### Main Menu
- Professional horror atmosphere
- New Game, Settings, and Quit options
- Hover effects on buttons

### Gameplay
- First-person perspective with mouse look
- WASD movement with sprint
- Jump mechanic
- Flashlight system
- Crosshair aiming

### Combat System
- Pistol-based shooting
- Raycast bullet system
- Magazine and reserve ammo
- Reload mechanic

### Enemy AI
- Zombie detection and chase
- Melee attacks
- Health and death animations
- Wave-based spawning system

### HUD
- Health bar (color-coded)
- Ammo counter
- Kill counter
- Objective display
- Crosshair

### Environment
- Atmospheric horror setting
- Fog effects
- Collision-based obstacles
- Multiple spawn points

## Development

The game is built with a modular architecture:
- `src/core/` - Core game systems
- `src/player/` - Player controller and mechanics
- `src/enemies/` - Zombie AI and behavior
- `src/weapons/` - Weapon systems
- `src/ui/` - User interface and HUD
- `src/levels/` - Level design and management

## Performance Tips

1. Use optimized textures (1024x1024 or lower)
2. Keep zombie count reasonable (5-10 per wave)
3. Use simple 3D models when possible
4. Disable unnecessary visual effects on lower-end systems

## Credits

- Built with Ursina Engine 8.3.0
- Powered by Panda3D
- Python 3.13+

## License

This is a prototype project for educational purposes.
