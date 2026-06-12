# Project Eclipse: Horror Survival - Quick Start Guide

## What is Project Eclipse?
A professional horror FPS game prototype built with Python 3.13 and Ursina Engine 8.3.0.

## Quick Start (5 minutes)

### Windows Users
```bash
setup.bat
python main.py
```

### macOS/Linux Users
```bash
bash setup.sh
python main.py
```

### Manual Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Game Features

### Main Menu
✓ Professional horror atmosphere
✓ Dark cinematic UI
✓ New Game, Settings, Quit buttons
✓ Hover effects and animations

### Gameplay
✓ First-person perspective (FPS)
✓ WASD movement with sprint (Shift)
✓ Mouse look camera control
✓ Jump (Space)
✓ Flashlight toggle (F)

### Combat
✓ Pistol weapon system
✓ Left-click to shoot
✓ Reload (R)
✓ Ammo management (30 mag + 120 reserve)
✓ Raycast bullet system
✓ Muzzle flash effects

### Enemy AI
✓ Zombie detection and chasing
✓ Melee attacks on close range
✓ Health system (30 HP)
✓ Death and removal
✓ Wave-based spawning

### HUD
✓ Health bar (color-coded)
✓ Ammo counter
✓ Kill counter
✓ Objective display
✓ Crosshair

### Environment
✓ Atmospheric horror level
✓ Fog effects
✓ Collision system
✓ Obstacles and cover
✓ Multiple zombie spawn points

## Controls

| Action | Key |
|--------|-----|
| Forward | W |
| Backward | S |
| Left | A |
| Right | D |
| Sprint | Shift |
| Jump | Space |
| Look | Mouse |
| Shoot | Left Click |
| Reload | R |
| Flashlight | F |
| Menu | ESC |

## Adding Assets

Place your files in these directories:

```
project/
├── assets/
│   ├── textures/     # PNG images
│   ├── models/       # OBJ, FBX, GLTF files
│   ├── sounds/       # WAV files
│   └── ui/           # UI textures
```

### Essential Assets
- `horror_background.png` - Main menu background
- `zombie_texture.png` - Zombie appearance
- `pistol_shot.wav` - Gun sound
- `pistol.obj` - First-person gun model (optional)

## Project Structure

```
project/
├── main.py                 # Game entry point
├── requirements.txt        # Dependencies
├── setup.py               # Setup script
├── setup.sh/setup.bat     # Platform-specific setup
│
├── src/
│   ├── core/              # Game systems
│   │   ├── game_manager.py
│   │   ├── game_state.py
│   │   ├── asset_manager.py
│   │   ├── input_manager.py
│   │   ├── audio_manager.py
│   │   ├── settings.py
│   │   └── particle_effects.py
│   │
│   ├── player/            # Player mechanics
│   │   └── controller.py
│   │
│   ├── enemies/           # Enemy AI
│   │   ├── zombie.py
│   │   ├── zombie_spawner.py
│   │   └── ai_controller.py
│   │
│   ├── weapons/           # Weapon systems
│   │   └── pistol.py
│   │
│   ├── ui/                # User interface
│   │   ├── menu.py        # Main menu
│   │   ├── hud.py         # In-game HUD
│   │   └── game_over.py   # Game over screen
│   │
│   └── levels/            # Level design
│       ├── level_one.py
│       ├── level_manager.py
│       ├── environment.py
│       └── obstacles.py
│
└── assets/
    ├── textures/
    ├── models/
    ├── sounds/
    └── ui/
```

## Game States

1. **Main Menu** - Navigate options
2. **Gameplay** - Survive zombie waves
3. **Game Over** - View stats and restart

## Performance Tips

- Keep textures 1024x1024 or smaller
- Limit zombies to 10-15 per wave
- Use simple 3D models
- Close background applications

## Troubleshooting

**Game won't start**
```bash
pip install --upgrade ursina panda3d pillow
```

**Assets not loading**
- Check file names match exactly
- Verify files are in correct directories
- Use PNG for textures, WAV for sounds

**Low FPS**
- Reduce texture resolution
- Lower zombie spawn rate
- Decrease view distance in fog settings

## System Requirements

- **OS**: Windows 10+, macOS 10.13+, Linux
- **Python**: 3.13+
- **RAM**: 2GB minimum
- **GPU**: Integrated graphics minimum
- **Storage**: 500MB free space

## Next Steps

1. ✓ Install dependencies
2. ✓ Add zombie reference image to `assets/models/`
3. ✓ Add horror background to `assets/ui/`
4. ✓ Add sound effects to `assets/sounds/`
5. Run the game!

## Customization

Edit these files to customize:
- `src/core/settings.py` - Game settings
- `src/enemies/zombie_spawner.py` - Spawn rates
- `src/player/controller.py` - Player speed/health
- `src/weapons/pistol.py` - Gun damage/ammo

## Support

For issues or feature requests, check:
- `SETUP.md` - Detailed setup instructions
- `README.md` - Project documentation

## Credits

Built with:
- Ursina Engine 8.3.0
- Panda3D
- Python 3.13+

---

**Ready? Type `python main.py` and start the apocalypse!**
