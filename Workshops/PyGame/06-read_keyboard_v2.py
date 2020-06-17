import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Control of the image with the arrows of the keyboard (v2)")

# https://freeicons.io/
image = pygame.image.load("1169214951579330067-128.png")
pygame.display.set_icon(image)

initial_x_coordinate = 0
initial_y_coordinate = 0
new_x_coordinate = initial_x_coordinate
new_y_coordinate = initial_y_coordinate
x_direction = 1 # Go to right
y_direction = 1 # Go to bottom

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_x_coordinate -= 1
            elif event.key == pygame.K_RIGHT:
                new_x_coordinate += 1
            elif event.key == pygame.K_UP:
                new_y_coordinate -= 1
            elif event.key == pygame.K_DOWN:
                new_y_coordinate += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                new_x_coordinate -= 1
            elif event.key == pygame.K_RIGHT:
                new_x_coordinate += 1
            elif event.key == pygame.K_UP:
                new_y_coordinate -= 1
            elif event.key == pygame.K_DOWN:
                new_y_coordinate += 1
            
    screen.fill((100,200,100)) # RGB, 8 bits/component, values in [0, 255]
    screen.blit(image, (new_x_coordinate, new_y_coordinate))
    pygame.display.update()
    
    if (new_x_coordinate + image.get_width()) > width:
        new_x_coordinate -= 1
    elif new_x_coordinate < 0:
        new_x_coordinate += 1
    if (new_y_coordinate + image.get_height()) > height:
        new_y_coordinate -= 1
    elif new_y_coordinate < 0:
        new_y_coordinate += 1

