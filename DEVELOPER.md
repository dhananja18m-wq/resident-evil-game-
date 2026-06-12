# Project Eclipse: Horror Survival - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Game Features](#game-features)
5. [Controls](#controls)
6. [Project Structure](#project-structure)
7. [Adding Assets](#adding-assets)
8. [Customization](#customization)
9. [Troubleshooting](#troubleshooting)
10. [Technical Details](#technical-details)

## Project Overview

**Project Eclipse: Horror Survival** is a polished horror FPS game prototype built with:
- **Engine**: Ursina 8.3.0 (Panda3D wrapper)
- **Language**: Python 3.13+
- **Type**: First-Person Shooter (FPS)
- **Genre**: Survival Horror

### Key Features
✓ Professional main menu system
✓ First-person gameplay with realistic physics
✓ Zombie AI with multiple behavior states
✓ Advanced weapon system with ammo management
✓ Dynamic HUD with health, ammo, and kill tracking
✓ Wave-based enemy spawning system
✓ Atmospheric horror environment
✓ Complete game state management
✓ Settings persistence
✓ Cross-platform support (Windows, macOS, Linux)

## Installation

### System Requirements
- **Python**: 3.13 or higher
- **OS**: Windows 10+, macOS 10.13+, or Linux
- **RAM**: 2GB minimum (4GB recommended)
- **GPU**: Integrated graphics minimum
- **Storage**: 500MB free space
- **Internet**: Required for initial dependency installation

### Step 1: Clone or Download Repository
```bash
git clone https://github.com/dhananja18m-wq/resident-evil-game-.git
cd resident-evil-game-
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Setup Script (Optional)

**Windows:**
```bash
setup.bat
```

**macOS/Linux:**
```bash
bash setup.sh
```

**Or use Python setup:**
```bash
python setup.py
```

### Step 5: Start the Game
```bash
python main.py
```

## Quick Start

### Fastest Setup (3 minutes)
```bash
# 1. Get the code
git clone https://github.com/dhananja18m-wq/resident-evil-game-.git
cd resident-evil-game-

# 2. Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install and run
pip install -r requirements.txt
python main.py
```

## Game Features

### Main Menu
- **Atmosphere**: Dark cinematic horror theme
- **UI**: Professional button interface
- **Options**:
  - New Game - Start the zombie apocalypse
  - Settings - Adjust game preferences
  - Quit - Exit the game
- **Animations**: Fade-in effects and hover states

### Gameplay Mechanics

#### Movement
- **Forward**: W key
- **Backward**: S key
- **Strafe Left**: A key
- **Strafe Right**: D key
- **Sprint**: Hold Left Shift (increased speed)
- **Jump**: Space bar
- **Speed**: 20 units/sec (normal), 35 units/sec (sprint)

#### Camera
- **Mouse Look**: Free-look camera control
- **Sensitivity**: 2.0 (adjustable in settings)
- **First-Person View**: Always active during gameplay

#### Equipment
- **Flashlight**: F key to toggle
  - Illuminates environment in 50-unit radius
  - White light for maximum visibility
- **Pistol**: Primary weapon
  - 30-round magazine
  - 120 reserve ammunition
  - Shoot with Left Mouse Button
  - Reload with R key

### Combat System

#### Weapon: Pistol
- **Damage**: 25 HP per hit
- **Fire Rate**: Unlimited (click to shoot)
- **Magazine Size**: 30 rounds
- **Reserve Ammo**: 120 rounds
- **Reload Time**: Instant (manual reload)
- **Effects**: Muzzle flash on every shot
- **Sound**: Optional gunshot audio
- **Bullet System**: Raycast-based for perfect accuracy

#### Targeting
- **Crosshair**: Center-screen white reticle
- **Range**: Infinite raycast distance
- **Collision**: Raycast detects zombie bodies
- **Visual Feedback**: Muzzle flash on fire

### Enemy System

#### Zombie Behavior
1. **Idle State**
   - Wanders randomly
   - Pauses between movements
   - Duration: 2-5 seconds per action

2. **Alert State**
   - Detects player within 50-unit radius
   - Turns to face player direction
   - Plays alert sound

3. **Chase State**
   - Pursues player at 15 units/sec
   - Maintains line of sight
   - Moves toward player position

4. **Attack State**
   - Activates within 3-unit range
   - Deals 10 damage per attack
   - 1.5-second attack cooldown
   - Stops chasing if player distances himself

#### Zombie Stats
- **Health**: 30 HP
- **Speed**: 15 units/sec
- **Damage**: 10 HP per attack
- **Detection Range**: 50 units
- **Attack Range**: 3 units
- **Attack Cooldown**: 1.5 seconds

#### Zombie Spawning
- **Wave System**: Progressive difficulty
- **Initial Zombies**: 3 per wave
- **Spawn Interval**: 2 seconds between zombies
- **Difficulty**: +1 zombie per wave
- **Locations**: 6 fixed spawn points around arena

### HUD (Heads-Up Display)

#### Health Display
- **Position**: Top-left corner
- **Format**: "Health: [0-100]"
- **Color Coding**:
  - Green (100-60 HP): Healthy
  - Orange (60-30 HP): Wounded
  - Red (30-0 HP): Critical

#### Ammo Display
- **Position**: Top-right corner
- **Format**: "Ammo: [Magazine] | Reserve: [Total]"
- **Example**: "Ammo: 30 | Reserve: 120"
- **Color**: Yellow text

#### Kill Counter
- **Position**: Top-left, below health
- **Format**: "Kills: [Number]"
- **Color**: White text
- **Purpose**: Track player score

#### Objective Text
- **Position**: Bottom-center
- **Text**: "Eliminate all zombies"
- **Color**: Red text (prominent)
- **Size**: 1.2x normal text

#### Crosshair
- **Position**: Center screen
- **Style**: "+" symbol
- **Color**: White
- **Size**: 1.5x normal text

### Environment

#### Arena Layout
- **Size**: 100x100 units
- **Shape**: Square arena with obstacles
- **Floor**: Dark gray concrete
- **Walls**: Perimeter walls (100x10x2 units)
- **Obstacles**: 4 central pillars for cover

#### Lighting
- **Ambient**: Dark gray 0.5 intensity
- **Directional**: Single overhead light
- **Player Light**: Flashlight (50-unit radius)
- **Atmosphere**: Fog effect (200-unit distance)

#### Visual Effects
- **Fog Density**: 0.02
- **Fog Color**: Dark gray
- **Sky**: Dark gray dome
- **Particle Effects**: Blood splatter on zombie death

## Controls

| Action | Key | Alternative |
|--------|-----|-------------|
| Move Forward | W | Arrow Up |
| Move Backward | S | Arrow Down |
| Move Left | A | Arrow Left |
| Move Right | D | Arrow Right |
| Sprint | Left Shift | Hold while moving |
| Jump | Space | Double-tap direction |
| Look Around | Mouse | Mouse movement |
| Shoot | Left Click | Fire weapon |
| Reload | R | Refill magazine |
| Toggle Flashlight | F | Light on/off |
| Menu/Pause | ESC | Return to menu |

## Project Structure

```
resident-evil-game-/
│
├── main.py                          # Game entry point
├── requirements.txt                 # Python dependencies
├── setup.py                         # Python setup script
├── setup.sh                         # macOS/Linux setup
├── setup.bat                        # Windows setup
├── .gitignore                       # Git ignore rules
│
├── README.md                        # Project overview
├── SETUP.md                         # Detailed setup guide
├── QUICKSTART.md                    # Quick start guide
├── DEVELOPER.md                     # Developer documentation
│
├── src/                             # Source code
│   ├── __init__.py
│   │
│   ├── core/                        # Core game systems
│   │   ├── __init__.py
│   │   ├── game_manager.py          # Main game controller
│   │   ├── game_state.py            # Game state enum
│   │   ├── asset_manager.py         # Asset loading
│   │   ├── input_manager.py         # Input handling
│   │   ├── audio_manager.py         # Sound management
│   │   ├── settings.py              # Game settings
│   │   ├── particle_effects.py      # Visual effects
│   │   └── gameplay_systems.py      # Advanced mechanics
│   │
│   ├── player/                      # Player mechanics
│   │   ├── __init__.py
│   │   └── controller.py            # Player controller
│   │
│   ├── enemies/                     # Enemy systems
│   │   ├── __init__.py
│   │   ├── zombie.py                # Zombie entity
│   │   ├── zombie_spawner.py        # Spawning system
│   │   ├── ai_controller.py         # AI management
│   │   └── advanced_zombie.py       # Enhanced zombie AI
│   │
│   ├── weapons/                     # Weapon systems
│   │   ├── __init__.py
│   │   └── pistol.py                # Pistol weapon
│   │
│   ├── ui/                          # User interface
│   │   ├── __init__.py
│   │   ├── menu.py                  # Main menu
│   │   ├── hud.py                   # In-game HUD
│   │   └── game_over.py             # Game over screen
│   │
│   └── levels/                      # Level systems
│       ├── __init__.py
│       ├── level_one.py             # First level
│       ├── level_manager.py         # Level management
│       ├── environment.py           # Environment setup
│       └── obstacles.py             # Obstacles and objects
│
└── assets/                          # Game assets
    ├── textures/                    # Image files
    │   └── .gitkeep
    ├── models/                      # 3D models
    │   └── .gitkeep
    ├── sounds/                      # Audio files
    │   └── .gitkeep
    └── ui/                          # UI elements
        └── .gitkeep
```

## Adding Assets

### Asset Directory Structure
```
assets/
├── textures/                        # 2D images (PNG recommended)
│   ├── horror_background.png        # Menu background
│   ├── zombie_texture.png           # Zombie skin
│   ├── floor_texture.png            # Floor texture
│   └── wall_texture.png             # Wall texture
│
├── models/                          # 3D models
│   ├── pistol.obj                   # Pistol model
│   ├── zombie.fbx                   # Zombie model
│   ├── zombie.gltf                  # Alternative format
│   └── zombie_texture.png           # Model texture
│
├── sounds/                          # Audio (WAV recommended)
│   ├── pistol_shot.wav              # Gunshot
│   ├── zombie_growl.wav             # Zombie sound
│   ├── zombie_attack.wav            # Attack sound
│   ├── menu_music.wav               # Menu background
│   └── level_ambient.wav            # Level atmosphere
│
└── ui/                              # UI textures
    ├── logo.png                     # Game logo
    ├── button_normal.png            # Button states
    ├── button_hover.png
    └── button_pressed.png
```

### Supported Formats

**Textures**
- PNG (recommended, 32-bit with alpha)
- JPG (lossy, not recommended for games)
- BMP

**Models**
- OBJ (recommended, widely compatible)
- FBX (advanced, animation support)
- GLTF (modern, web-friendly)

**Sounds**
- WAV (recommended, best quality)
- MP3 (compressed, smaller files)
- OGG (compressed, good quality)

### Loading Assets

Assets are automatically loaded from the `assets/` directory. File names are converted to keys:

```python
# Asset file: assets/textures/zombie_texture.png
# Loaded as: asset_manager.get_texture('zombie_texture')

# Asset file: assets/sounds/pistol_shot.wav
# Loaded as: audio_manager.get_sound('pistol_shot')
```

### Asset Specifications

**Texture Recommendations**
- Resolution: 1024x1024 or less
- Format: PNG-32 with alpha channel
- Color space: sRGB
- Mip-maps: Enabled

**Model Recommendations**
- Polygon count: < 5000 for characters
- Format: OBJ or FBX
- Scale: 1 unit = 1 meter
- Rig: Optional for animations

**Sound Recommendations**
- Sample rate: 44.1 kHz
- Bit depth: 16-bit
- Mono or Stereo
- Format: WAV for quality

## Customization

### Game Settings

Edit `src/core/settings.py`:

```python
self.settings = {
    'resolution': (1280, 720),      # Screen size
    'fullscreen': False,             # Fullscreen mode
    'mouse_sensitivity': 2.0,        # Camera sensitivity
    'sound_volume': 0.5,             # Sound effect volume
    'music_volume': 0.3,             # Music volume
    'difficulty': 'normal',          # Game difficulty
    'brightness': 1.0                # Screen brightness
}
```

### Player Settings

Edit `src/player/controller.py`:

```python
self.speed = 20                      # Normal movement speed
self.sprint_speed = 35               # Sprint speed
self.health = 100                    # Starting health
self.max_health = 100                # Maximum health
self.gravity = 35                    # Gravity strength
self.jump_force = 20                 # Jump height
```

### Weapon Balance

Edit `src/weapons/pistol.py`:

```python
# Bullet damage
# Zombie health
# Magazine size
# Fire rate
```

### Difficulty Settings

Edit `src/enemies/zombie_spawner.py`:

```python
self.zombies_per_wave = 3            # Starting zombies
self.wave_spawn_interval = 2         # Time between spawns
# Difficulty multiplier increases each wave
```

### Environment

Edit `src/levels/environment.py`:

```python
# Adjust arena size
# Add/remove obstacles
# Modify lighting
# Change fog density
```

## Troubleshooting

### Common Issues

**Problem: "ModuleNotFoundError: No module named 'ursina'"**
```bash
# Solution: Install dependencies
pip install -r requirements.txt

# Or manually
pip install ursina==8.3.0
```

**Problem: "Failed to create game window"**
```bash
# Solution: Update graphics drivers
# For Windows: Update GPU drivers
# For macOS: Update to latest macOS
# For Linux: Install Python development packages
sudo apt-get install python3-dev libgl1-mesa-glx
```

**Problem: "Game runs slowly"**
```bash
# Solutions:
# 1. Lower texture resolution
# 2. Reduce zombie count in zombie_spawner.py
# 3. Disable fog effects
# 4. Close background applications
```

**Problem: "Assets not loading"**
```bash
# Solution: Check file locations
# Assets must be in: assets/[category]/filename.ext
# Verify filenames match exactly (case-sensitive on Linux)
```

**Problem: "Game crashes on startup"**
```bash
# Solution: Run with verbose output
python -u main.py

# Check the error messages
# Verify all files are present
# Reinstall dependencies: pip install --upgrade -r requirements.txt
```

### Performance Optimization

1. **Lower Draw Distance**
   - Edit `src/levels/environment.py`
   - Reduce fog distance from 200 to 100

2. **Reduce Enemy Count**
   - Edit `src/enemies/zombie_spawner.py`
   - Lower `zombies_per_wave` from 3 to 2

3. **Simplify Graphics**
   - Use smaller textures (512x512)
   - Use simpler models
   - Disable particle effects

4. **System Optimization**
   - Close unnecessary programs
   - Update GPU drivers
   - Ensure adequate RAM available

## Technical Details

### Engine Architecture

**Ursina** is built on top of **Panda3D**:
- Low-level 3D rendering
- Collision detection
- Audio playback
- Input handling

**Ursina** adds:
- Simplified Python API
- Entity-component system
- Built-in UI widgets
- Animation system

### Game Loop

```
1. Input Processing
   └─ Keyboard (WASD, Space, etc.)
   └─ Mouse (Look, click)

2. Update Phase
   └─ Player movement
   └─ Zombie AI
   └─ Weapon system
   └─ Collision detection
   └─ HUD updates

3. Rendering Phase
   └─ Camera setup
   └─ Scene rendering
   └─ UI rendering
   └─ Post-processing

4. Frame Complete
   └─ Repeat at target FPS
```

### Coordinate System

- **X-axis**: Left (-) / Right (+)
- **Y-axis**: Down (-) / Up (+)
- **Z-axis**: Back (-) / Forward (+)
- **Units**: 1 unit ≈ 1 meter

### Collision System

**Box Colliders**
- Player: 0.5 x 1.7 x 0.5 units
- Zombies: 0.7 x 1.8 x 0.7 units
- Obstacles: Variable sizes
- Raycast: Infinite distance bullets

## Advanced Topics

### Extending Zombie AI

Edit `src/enemies/advanced_zombie.py` to add:
- Complex pathfinding
- Group coordination
- Special abilities
- Boss zombies

### Adding New Weapons

Create `src/weapons/rifle.py`:
- Extend weapon system
- Different fire rates
- Special effects
- Unique damage models

### Creating New Levels

Create `src/levels/level_two.py`:
- Different arena layouts
- New enemy types
- Boss encounters
- Dynamic events

### Custom Visual Effects

Edit `src/core/particle_effects.py`:
- Blood splatter
- Muzzle flashes
- Explosions
- Environmental effects

## Support and Resources

- **Ursina Documentation**: https://www.ursinastudio.com/
- **Panda3D Manual**: https://docs.panda3d.org/
- **Python Documentation**: https://docs.python.org/3.13/

## Credits

**Project Eclipse** is built with:
- **Ursina Engine** 8.3.0
- **Panda3D** 3D Graphics Engine
- **Python** 3.13+

**Development**
- Core Systems: Game Manager, State Management
- Player Mechanics: Movement, Combat, HUD
- Enemy AI: Zombie Behavior, Wave Spawning
- Environment: Level Design, Atmosphere
- UI: Menus, Game Over, Settings

## License

This project is a prototype for educational purposes.

## Version History

### v1.0.0 (Current)
- ✓ Main menu system
- ✓ First-person gameplay
- ✓ Zombie AI
- ✓ Weapon system
- ✓ HUD and UI
- ✓ Wave system
- ✓ Settings persistence
- ✓ Cross-platform support

### Future Plans
- Multiplayer support
- Additional weapons
- New maps
- Boss encounters
- Progression system
- Achievements

---

**Last Updated**: June 12, 2026
**Stable Version**: 1.0.0
**Python Requirement**: 3.13+
**Ursina Version**: 8.3.0
