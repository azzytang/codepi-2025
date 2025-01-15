import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coordinate Graph with y = mx + b")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Graph parameters
grid_spacing = 20  # Spacing between grid lines
origin = (WIDTH // 2, HEIGHT // 2)  # Center of the screen

# Line equation parameters
m = 0.5  # Slope
b = 0   # y-intercept (in graph units)

# Convert graph units to screen pixels


def graph_to_screen(x, y):
    screen_x = origin[0] + x * grid_spacing
    screen_y = origin[1] - y * grid_spacing  # Invert y-axis
    return screen_x, screen_y

# Function to calculate line points


def calculate_line_points(m, b, width, spacing):
    # Graph x-range: Convert screen width to graph units
    x_min = -width // (2 * spacing)
    x_max = width // (2 * spacing)

    # Calculate y values for the line endpoints
    y1 = m * x_min + b
    y2 = m * x_max + b

    # Convert graph coordinates to screen coordinates
    p1 = graph_to_screen(x_min, y1)
    p2 = graph_to_screen(x_max, y2)
    return p1, p2


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw grid
    for x in range(0, WIDTH, grid_spacing):
        pygame.draw.line(screen, GRAY, (x, 0),
                         (x, HEIGHT), 1)  # Vertical lines
    for y in range(0, HEIGHT, grid_spacing):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y),
                         1)  # Horizontal lines

    # Draw axes
    pygame.draw.line(
        screen, BLACK, (0, origin[1]), (WIDTH, origin[1]), 2)  # x-axis
    pygame.draw.line(
        screen, BLACK, (origin[0], 0), (origin[0], HEIGHT), 2)  # y-axis

    # Draw the y = mx + b line
    p1, p2 = calculate_line_points(m, b, WIDTH, grid_spacing)
    pygame.draw.line(screen, RED, p1, p2, 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
