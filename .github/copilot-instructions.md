# Copilot Instructions for this Repository

## Build, Test, and Lint Commands
- **Run the game:**
  ```bash
  python retro-invader.py
  ```
- **Dependencies:**
  - Requires `pygame` (install with `pip install pygame`).
- **Tests/Lint:**
  - No automated tests or lint commands are present.

## High-Level Architecture
- The main game logic is in `retro-invader.py`.
- Uses Pygame for rendering and input.
- Alien sprites and backgrounds are in `images/sprites/` and `images/background2.png`.
- The game is a Space Invaders clone with:
  - Player movement and shooting
  - Multiple rows of aliens
  - Score tracking

## Key Conventions
- All image assets are loaded from the `images/` directory.
- Alien sprites are named `alien_0.png` to `alien_7.png`.
- No formal module structure; all logic is in a single script.

---

If you want to configure any MCP servers (e.g., for Playwright or CI integration), let me know!
