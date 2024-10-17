# Procedural-Map-2D-Generation-using-PYGAME

# Program Description: Maze Generation and Raycasting Game in Pygame
This Python program, built using the Pygame library, simulates a maze-based raycasting game. The game features procedurally generated mazes, player movement, and a 3D-like raycasting view. It includes a simple user interface for seed-based maze generation and in-game navigation, allowing players to explore a maze environment rendered with 2D raycasting techniques similar to early FPS games like Wolfenstein 3D or Doom.

# Key Features:
- Maze Generation:

> A procedural maze generation system using recursive backtracking. The grid is initially filled with walls, and the maze is generated based on a seed input or randomization, creating unique paths and walls for each playthrough.
> The player can modify the maze manually by clicking on grid cells before starting the game, switching walls and paths.
- Raycasting Engine:

Raycasting is used to render a pseudo-3D perspective of the maze. Rays are cast from the player's position, and based on their distance to the walls, the program simulates depth by adjusting the size and color of wall segments.
The program renders the floor and ceiling colors for added visual realism, enhancing the immersive gameplay.
- Player Movement:

Players control their character’s movement in the maze using the arrow keys. The movement is constrained by walls, ensuring that the player cannot phase through obstacles.
The player can rotate and move forward, backward, left, and right through the maze, and the game responds by updating the raycasting view in real time.
- Seed-based Maze Customization:

Players can input a specific seed value or randomize it using the 'R' key. This seed determines the layout of the maze, enabling consistent results when the same seed is used.
A seed text input box allows players to enter numbers, and pressing 'Enter' generates the maze based on that input.
- User Interface:

The program features a side panel with buttons to start and quit the game. Before starting, players can see and modify the maze grid.
During gameplay, an FPS counter is displayed, providing real-time feedback on the game's performance.
- Collision Detection:

The program ensures proper collision detection by preventing the player from moving through walls. The player’s position is only updated if the new position corresponds to a valid path in the maze.
# Controls:
- Arrow Keys: Move the player through the maze.
- Mouse Click: Modify the maze grid before starting the game.
- Enter: Generate a maze based on the seed input.
- R: Randomize the seed and generate a new maze.
- Play/Start Button: Begin exploring the maze with raycasting.

# Visual Design:
- Walls: Yellow walls with varying shades depending on their distance from the player.
- Floor and Roof: Soft yellow floor and light gray roof for added realism.
- Grid: Green represents walls in the grid view, and white represents paths.
