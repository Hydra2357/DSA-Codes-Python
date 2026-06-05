# Flappy Bird Clone (Python + Pygame)

A polished Flappy Bird clone built with Python and Pygame featuring animated birds, moving clouds, procedural pipe generation, score tracking, collision detection, and smooth gameplay mechanics.

## Features

* Smooth bird physics with gravity and flap mechanics
* Animated bird wings
* Rotating bird based on velocity
* Procedurally generated pipes
* Moving cloud background
* Scrolling ground animation
* Real-time score tracking
* High score system
* Start screen and Game Over screen
* Mouse and keyboard controls
* Visual effects and screen flash on collision

## Technologies Used

* Python 3
* Pygame

## Installation

### Clone Repository

```bash
git clone https://github.com/Hydra2357/FlappyBird.git
cd FlappyBird
```

### Install Dependencies

```bash
pip install pygame
```

### Run Game

```bash
python flappy_bird.py
```

## Controls

| Key                       | Action       |
| ------------------------- | ------------ |
| Space                     | Flap Bird    |
| Left Mouse Click          | Flap Bird    |
| ESC                       | Exit Game    |
| Space / Click (Game Over) | Restart Game |

## Gameplay

1. Press Space or Click to start.
2. Navigate the bird through pipe gaps.
3. Earn 1 point for every pipe passed.
4. Avoid hitting pipes, the ceiling, or the ground.
5. Try to beat your high score.

## Project Structure

```text
FlappyBird/
│
├── flappy_bird.py
├── README.md
└── requirements.txt
```

## Game Mechanics

### Bird Physics

* Gravity: 0.5
* Flap Strength: -9
* Smooth rotation based on velocity

### Pipe System

* Pipe Gap: 160 pixels
* Pipe Speed: 3 pixels/frame
* Spawn Interval: 1500 ms

### Visual Effects

* Animated bird wings
* Dynamic cloud movement
* Scrolling grass animation
* Collision flash effect
* Start and Game Over overlays

## Future Improvements

* Sound effects
* Background music
* Save high scores to file
* Difficulty levels
* Different bird skins
* Mobile version
* Pause menu
* Achievements system

## Author

Mahesh Mungase

GitHub: https://github.com/Hydra2357

## License

This project is open-source and available under the MIT License.
