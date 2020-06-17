import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A Bouncing Image")

# https://freeicons.io/
image = pygame.image.load("1169214951579330067-128.png")
pygame.display.set_icon(image)

initial_x_coordinate = width/2 - image.get_width()/2
initial_y_coordinate = 3*height/4 - image.get_height()/2
new_x_coordinate = initial_x_coordinate
new_y_coordinate = initial_y_coordinate
x_direction = 1 # Go to right
y_direction = 1 # Go to bottom

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((100,200,100)) # RGB, 8 bits/component, values in [0, 255]
    screen.blit(image, (new_x_coordinate, new_y_coordinate))
    pygame.display.update()
    new_x_coordinate += x_direction
    if (new_x_coordinate + image.get_width()) > width:
        x_direction = -1
    elif new_x_coordinate < 0:
        x_direction = 1
    new_y_coordinate += y_direction
    if (new_y_coordinate + image.get_height()) > height:
        y_direction = -1
    elif new_y_coordinate < 0:
        y_direction = 1

