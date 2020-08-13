import pygame

pygame.init()
width = 800
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Simple Screen")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print("Goodbye!")
