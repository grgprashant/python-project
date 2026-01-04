import pygame
import sys

# Initialize pygame
pygame.init()

# Screen
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enemy Follows Player")

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 50, 255)
RED = (255, 0, 0)

# Player
player_x = 300
player_y = 200
player_speed = 10

# Enemy
enemy_x = 50
enemy_y = 50
enemy_speed = 5

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Enemy follows player
    if enemy_x < player_x:
        enemy_x += enemy_speed
    if enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    if enemy_y > player_y:
        enemy_y -= enemy_speed

    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 40, 40))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 40, 40))

    pygame.display.update()
    clock.tick(60)
