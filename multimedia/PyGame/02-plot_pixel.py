import pygame
import my_colors as color

pygame.init()
width = 800
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Search the green pixel at the coordinates (x=10, y=100)")

print("I'm going to draw a green pixel at the coordinates (x=10, y=100)...")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.set_at((10, 100), color.green)
    pygame.display.update()

pygame.quit()
print("Goodbye!")
