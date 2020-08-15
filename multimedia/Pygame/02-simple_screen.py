import pygame

pygame.init()
width = 800
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Simple Screen")

running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
print("Goodbye!")
