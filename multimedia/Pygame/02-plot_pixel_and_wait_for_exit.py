import pygame
import my_colors as color

pygame.init()
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Search the green pixel at the coordinates (x=10, y=100)")

running = True
while running:
    screen.set_at((1, 1), color.white)
    screen.set_at((10, 100), color.green)
    pygame.display.update()
    event = pygame.event.wait()  # Wait for an (input) event
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
print("Goodbye!")
