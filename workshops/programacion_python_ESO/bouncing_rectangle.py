import pygame
from lib import colors as color

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A bouncing rectangle")

rectangle_width = 100
rectangle_height = 50

initial_x_coordinate = screen_width/2 - rectangle_width/2
initial_y_coordinate = 3*screen_height/4 - rectangle_height/2
new_x_coordinate = initial_x_coordinate
new_y_coordinate = initial_y_coordinate
x_direction = 1 # Go to right
y_direction = 1 # Go to bottom

running = True
while running:
    screen.fill(color.black)
    pygame.draw.rect(screen, color.blue, (new_x_coordinate, new_y_coordinate, rectangle_width, rectangle_height))
    pygame.display.update()
    new_x_coordinate += x_direction
    if (new_x_coordinate + rectangle_width) > screen_width:
        x_direction = -1
    elif new_x_coordinate < 0:
        x_direction = 1
    new_y_coordinate += y_direction
    if (new_y_coordinate + rectangle_height) > screen_height:
        y_direction = -1
    elif new_y_coordinate < 0:
        y_direction = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print("Goodbye!")
