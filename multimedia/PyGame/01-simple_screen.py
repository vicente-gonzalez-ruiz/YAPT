# pip3 install -U pygame --user
# Alternatively: sudo pacman -S python-pygame
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Screen")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
