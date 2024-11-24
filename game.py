import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rescue Mission")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Game clock
clock = pygame.time.Clock()

# Player properties
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size - 10]
player_speed = 10

# Victims properties
victim_size = 30
victim_pos = [random.randint(0, WIDTH - victim_size), 0]
victim_speed = 5

# Game variables
score = 0
game_over = False

def draw_text(text, x, y, color=WHITE):
    """Helper function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Update victim position
    victim_pos[1] += victim_speed
    if victim_pos[1] > HEIGHT:
        victim_pos = [random.randint(0, WIDTH - victim_size), 0]
        score -= 1  # Lose points if a victim is missed

    # Check for collision
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    victim_rect = pygame.Rect(victim_pos[0], victim_pos[1], victim_size, victim_size)
    if player_rect.colliderect(victim_rect):
        score += 1
        victim_pos = [random.randint(0, WIDTH - victim_size), 0]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GREEN, (victim_pos[0], victim_pos[1], victim_size, victim_size))
    draw_text(f"Score: {score}", 10, 10)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(30)

pygame.quit()
sys.exit()