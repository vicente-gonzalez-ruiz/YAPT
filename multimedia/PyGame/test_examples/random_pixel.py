import pygame
import random

# Window dimensions
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    screen.set_at((x, y), (red, green, blue))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(240)
