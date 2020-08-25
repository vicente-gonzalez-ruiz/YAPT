import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Empty Screen")
running = True
while running:
    event = pygame.event.wait().type
    if event == pygame.QUIT:
        running = False
pygame.quit()
print("Goodbye!")
