import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Screen Name")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
