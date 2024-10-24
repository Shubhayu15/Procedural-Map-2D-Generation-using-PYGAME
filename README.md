# 🎮 The Rooms - A Raycasting Maze Game
![Recording 2024-10-24 215749](https://github.com/user-attachments/assets/deaf6596-2372-42b7-9774-ddd59b87f65b)

A Python-based dungeon crawler that combines classic maze generation with raycasting technology to create an immersive 3D exploration experience. Create, customize, and explore procedurally generated mazes in first-person view!

![GitHub](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.6+-blue)
![Pygame](https://img.shields.io/badge/pygame-2.0+-yellow)

<p align="center">
  <a href="https://github.com/Shubhayu15">
    <img src="https://img.shields.io/github/followers/Shubhayu15?label=Follow&style=social" alt="GitHub followers">
  </a>
  <a href="https://github.com/Shubhayu15/Procedural-Map-2D-Generation-using-PYGAME">
    <img src="https://img.shields.io/github/stars/Shubhayu15/Procedural-Map-2D-Generation-using-PYGAME?style=social" alt="GitHub stars">
  </a>
</p>

## ✨ Features

- **Dual View Modes**
  - Top-down 2D maze editor
  - Immersive 3D first-person exploration
- **Procedural Generation**
  - Seed-based maze generation
  - Recursive backtracking algorithm for perfect mazes
- **Interactive Editor**
  - Custom maze creation
  - Real-time wall placement/removal
- **Raycasting Engine**
  - Smooth 3D rendering
  - Distance-based wall shading
  - Textured floors and ceilings

## 🎯 Prerequisites

- Python 3.6 or higher
- Pygame library

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Shubhayu15/Procedural-Map-2D-Generation-using-PYGAME.git
cd Procedural-Map-2D-Generation-using-PYGAME
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Run the game:
```bash
python main.py
```

## 🎮 How to Play

### Maze Editor Mode
- **Left Click**: Toggle walls/paths
- **Enter**: Generate new maze with current seed
- **R**: Generate maze with random seed
- **C**: Clear the grid
- **Play Button**: Switch to 3D exploration mode

### Exploration Mode
- **W**: Move forward
- **S**: Move backward
- **A**: Rotate left
- **D**: Rotate right

## 🛠️ Technical Details
![2](https://github.com/user-attachments/assets/276a56f5-6cc3-4d4a-b4ef-ceb320b3f047)
### Maze Generation
The game uses a recursive backtracking algorithm to generate perfect mazes, ensuring every location is reachable and there are no loops. Each maze is uniquely determined by its seed, allowing for reproducible layouts.
![1](https://github.com/user-attachments/assets/e5630893-42ca-47bc-b707-9a1e4dfe7275)
### Raycasting Engine
The 3D view is achieved through raycasting, similar to classic games like Wolfenstein 3D:
- FOV (Field of View): 60 degrees
- Dynamic wall shading based on distance
- Optimized ray calculation for smooth performance

## 🎨 Customization

You can modify these constants in the code to customize your experience:

```python
CELL_SIZE = 22        # Size of grid cells
GRID_WIDTH = 33       # Maze width
GRID_HEIGHT = 33      # Maze height
FOV = math.pi / 3     # Field of view
MOVE_SPEED = 2        # Player movement speed
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:
1. Report bugs
2. Suggest new features
3. Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by classic raycasting games
- Built with Pygame community resources
- Special thanks to early testers and contributors

---
Made with ❤️ by [Shubhayu15](https://github.com/Shubhayu15)
