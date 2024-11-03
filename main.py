import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinity Tunnel")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Circle parameters
NUM_CIRCLES = 100
MAX_RADIUS = 300
MIN_RADIUS = 50
SPEED = 4

# Object in the center
CENTER_OBJECT_RADIUS = 2

# Main loop
clock = pygame.time.Clock()
angle = 0  # Angle for the tunnel effect

running = True
while running:
    screen.fill(BLACK)
    
    # Draw the moving tunnel
    for i in range(NUM_CIRCLES):
        radius = MIN_RADIUS + ((MAX_RADIUS - MIN_RADIUS) / NUM_CIRCLES) * i
        offset = int(math.sin(angle + i * 0.3) * 20)  # Oscillate the circles for the tunnel effect
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), radius + offset, 2)

    # Draw the object in the center
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), CENTER_OBJECT_RADIUS)

    # Update the angle for movement
    angle += SPEED * 0.01

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
