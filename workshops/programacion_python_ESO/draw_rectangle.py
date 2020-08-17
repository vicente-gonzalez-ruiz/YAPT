import pygame
from lib import colors as color

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw a blue rectangle at (200, 150, 100, 50)")

running = True
while running:
    pygame.draw.rect(screen, color.blue, (200, 150, 100, 50))
    pygame.display.update()
    event = pygame.event.wait()  # Wait for an (input) event
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
print("Goodbye!")
