import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Grid settings
CELL_SIZE = 22  # Size of each cell
GRID_WIDTH = 33
GRID_HEIGHT = 33
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (55, 255, 0)
GRAY = (200, 200, 200)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (150, 255, 150)

# Raycasting colors
WALL_COLOR = (15, 105, 45)  
ROOF_COLOR = (80, 157, 230)   
FLOOR_COLOR = (68, 235, 124) 

# Create a Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH + 200, WINDOW_HEIGHT))  # Add space for the side panel
pygame.display.set_caption("The Rooms")

# Fonts and UI elements
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Create the grid
grid = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # Start with all walls

# Initial seed and input text
seed_text = ""
current_seed = None

# Define directions for maze generation
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Player settings for raycasting
player_x = 2 * CELL_SIZE
player_y = 2 * CELL_SIZE
player_angle = 0
MOVE_SPEED = 2  # Slower movement speed
FOV = math.pi / 3  # Field of view

# Helper function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(topleft=(x, y))
    surface.blit(text_obj, text_rect)

# Draw the grid
def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = WHITE if grid[row][col] == 0 else GREEN
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Function to modify the grid
def modify_grid(pos):
    row, col = pos
    if grid[row][col] == 1:  # If it's a wall, change to path
        grid[row][col] = 0
    elif grid[row][col] == 0:  # If it's a path, change to wall
        grid[row][col] = 1

# Randomly generate the maze using Recursive Backtracking
def generate_maze(x, y):
    grid[y][x] = 0  # Mark the current cell as a path

    # Randomize the order of directions
    random.shuffle(DIRECTIONS)

    for direction in DIRECTIONS:
        nx, ny = x + direction[0] * 2, y + direction[1] * 2

        if 0 < nx < GRID_WIDTH and 0 < ny < GRID_HEIGHT and grid[ny][nx] == 1:
            grid[y + direction[1]][x + direction[0]] = 0  # Remove wall between cells
            generate_maze(nx, ny)  # Recursively generate from the new cell

# Random dungeon generation with a maze
def generate_dungeon(seed):
    random.seed(seed)

    # Clear grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            grid[row][col] = 1  # Fill everything with walls (green)

    # Create the 1-block boundary
    for row in range(GRID_HEIGHT):
        grid[row][0] = 1  # Left boundary
        grid[row][GRID_WIDTH - 1] = 1  # Right boundary
    for col in range(GRID_WIDTH):
        grid[0][col] = 1  # Top boundary
        grid[GRID_HEIGHT - 1][col] = 1  # Bottom boundary

    # Add walls on the rightmost column and bottom row
    for row in range(GRID_HEIGHT):
        grid[row][GRID_WIDTH - 1] = 1  # Right boundary wall
    for col in range(GRID_WIDTH):
        grid[GRID_HEIGHT - 1][col] = 1  # Bottom boundary wall

    # Start maze generation from a random cell
    start_x = random.randrange(1, GRID_WIDTH - 1, 2)
    start_y = random.randrange(1, GRID_HEIGHT - 1, 2)
    generate_maze(start_x, start_y)

# Button functionality
def draw_button(x, y, width, height, text):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (x, y, width, height))
        if mouse_click[0]:  # Left mouse button
            if text == "Quit":
                pygame.quit()
                sys.exit()
            elif text == "Play":
                return True  # Signal to start the game
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))

    draw_text(text, font, BLACK, screen, x + 10, y + 10)
    return False

def cast_rays():
    num_rays = WINDOW_WIDTH // 2  # Number of rays for wall detection
    ray_angle = player_angle - FOV / 2
    ray_angle_increment = FOV / num_rays

    for i in range(num_rays):
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        for depth in range(1, 20 * CELL_SIZE):
            x = int((player_x + depth * cos_a) / CELL_SIZE)
            y = int((player_y + depth * sin_a) / CELL_SIZE)

            if grid[y][x] == 1:
                line_height = int(WINDOW_HEIGHT / (depth / CELL_SIZE))
                line_top = int(WINDOW_HEIGHT / 2 - line_height / 2)
                line_bottom = int(WINDOW_HEIGHT / 2 + line_height / 2)

                # Draw floor and ceiling
                pygame.draw.line(screen, FLOOR_COLOR, (i * 2, line_bottom), (i * 2, WINDOW_HEIGHT))  # Floor
                pygame.draw.line(screen, ROOF_COLOR, (i * 2, 0), (i * 2, line_top))  # Ceiling

                # Draw wall with shading based on distance
                shade_factor = min(1, 1 - depth / (20 * CELL_SIZE))
                wall_color = (int(WALL_COLOR[0] * shade_factor), int(WALL_COLOR[1] * shade_factor), int(WALL_COLOR[2] * shade_factor))
                pygame.draw.line(screen, wall_color, (i * 2, line_top), (i * 2, line_bottom))

                break

        ray_angle += ray_angle_increment

# Main game loop
running = True
game_active = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        # Mouse click to modify grid
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active:  # Only modify grid if not in game mode
                mouse_pos = pygame.mouse.get_pos()
                grid_pos = (mouse_pos[1] // CELL_SIZE, mouse_pos[0] // CELL_SIZE)
                if grid_pos[0] < GRID_HEIGHT and grid_pos[1] < GRID_WIDTH:
                    modify_grid(grid_pos)
        
        # Key press for text input
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() and not game_active:
                seed_text += event.unicode
            elif event.key == pygame.K_BACKSPACE and not game_active:
                seed_text = seed_text[:-1]
            elif event.key == pygame.K_RETURN and not game_active:
                if seed_text.isdigit():
                    current_seed = int(seed_text)
                    generate_dungeon(current_seed)
            elif event.key == pygame.K_r and not game_active:  # Randomize the seed
                current_seed = random.randint(0, 9999)
                seed_text = str(current_seed)
                generate_dungeon(current_seed)
            elif event.key == pygame.K_c and not game_active:  # Clear the grid
                for row in range(GRID_HEIGHT):
                    for col in range(GRID_WIDTH):
                        grid[row][col] = 1

    screen.fill(BLACK)

    if not game_active:
        draw_grid()  # Draw the grid in edit mode
        draw_text("Press Enter to", small_font, WHITE, screen, WINDOW_WIDTH - -10, 10)
        draw_text("Generate/Flip maze", small_font, WHITE, screen, WINDOW_WIDTH - -10, 40)
        draw_text("Seed: ", small_font, WHITE, screen, WINDOW_WIDTH - -10, 70)
        draw_text(seed_text, small_font, WHITE, screen, WINDOW_WIDTH - -10, 100)
        draw_text("Press R for", small_font, WHITE, screen, WINDOW_WIDTH - -10, 130)
        draw_text("random seed", small_font, WHITE, screen, WINDOW_WIDTH - -10, 160)
        draw_text("Press C to", small_font, WHITE, screen, WINDOW_WIDTH - -10, 190)
        draw_text("clear the grid", small_font, WHITE, screen, WINDOW_WIDTH - -10, 220)

        if draw_button(WINDOW_WIDTH - -10, 250, 160, 40, "Play"):
            game_active = True

        draw_button(WINDOW_WIDTH - -10, 290, 160, 40, "Quit")
    else:
        # Draw the raycasting view
        cast_rays()
        
        # Draw player (circle for representation)
        #pygame.draw.circle(screen, GREEN, (int(player_x), int(player_y)), 5)

        # Player movement controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # Move forward
            new_x = player_x + MOVE_SPEED * math.cos(player_angle)
            new_y = player_y + MOVE_SPEED * math.sin(player_angle)

            # Check if new position is valid (not colliding with walls)
            if grid[int(new_y / CELL_SIZE)][int(new_x / CELL_SIZE)] == 0:  # 0 means path
                player_x = new_x
                player_y = new_y

        if keys[pygame.K_s]:  # Move backward
            new_x = player_x - MOVE_SPEED * math.cos(player_angle)
            new_y = player_y - MOVE_SPEED * math.sin(player_angle)

            # Check if new position is valid (not colliding with walls)
            if grid[int(new_y / CELL_SIZE)][int(new_x / CELL_SIZE)] == 0:  # 0 means path
                player_x = new_x
                player_y = new_y

        if keys[pygame.K_a]:  # Rotate left
            player_angle -= 0.05  # Adjust the angle to rotate left
        if keys[pygame.K_d]:  # Rotate right
            player_angle += 0.05  # Adjust the angle to rotate right

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Control frame rate

pygame.quit()
