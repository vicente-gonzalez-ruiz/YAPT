import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Display an Image")

# https://freeicons.io/
image = pygame.image.load("1169214951579330067-128.png")
#pygame.display.set_icon(image)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((100,200,100)) # RGB, 8 bits/component, values in [0, 255]
    screen.blit(image, (width/2 - image.get_width()/2, 3*height/4 - image.get_height()/2))
    pygame.display.update()
