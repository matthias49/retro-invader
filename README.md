# Retro Invader

A simple Space Invaders clone implemented in Python using Pygame.

## Overview

`retro-invader.py` is a standalone script that recreates the classic Space Invaders arcade game. The game features:
- Player-controlled ship that moves left/right and shoots
- Multiple rows of animated alien invaders
- Score tracking
- Increasing difficulty as waves are cleared
- Retro-style pixel graphics and sprites

## How to Run

1. **Install dependencies:**
   ```bash
   pip install pygame
   ```
2. **Run the game:**
   ```bash
   python retro-invader.py
   ```

## Game Structure

- **Main Script:** All game logic is contained in `retro-invader.py`.
- **Assets:**
  - Alien sprites: `images/sprites/alien_0.png` to `alien_7.png`
  - Background: `images/background2.png`
- **Controls:**
  - Left/Right arrows: Move player
  - Space: Shoot
  - Q or window close: Quit

## Code Highlights

- **Grid System:** The game uses a grid for positioning, with block-based movement for both player and aliens.
- **Alien Waves:** Aliens are initialized in rows and columns, move horizontally, and descend when reaching screen edges.
- **Collision Detection:** Handles bullet-alien and alien-player collisions.
- **Score:** Points are awarded for each alien destroyed; penalty if aliens reach the bottom.

## Customization

- You can modify alien sprites or background images by replacing files in the `images/` directory.
- Game parameters (speed, rows, columns, etc.) can be tweaked at the top of `retro-invader.py`.

## Requirements
- Python 3.x
- Pygame

---

Enjoy blasting some retro aliens!
