import pygame
from lib import colors as color

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A bouncing rectangle")

paddle_width = 100
x_coordinate_paddle = 0 # screen_width/2 - paddle_width/2

running = True
while running:
    screen.fill(color.black)
    pygame.draw.line(screen, color.green, (x_coordinate_paddle, screen_height-10), (x_coordinate_paddle+paddle_width, screen_height-10))
    pygame.display.update()
    x_coordinate_paddle = pygame.mouse.get_pos()[0]
    if (x_coordinate_paddle + paddle_width) > screen_width:
        x_coordinate_paddle = screen_width-paddle_width
    elif x_coordinate_paddle < 0:
        x_coordinate_paddle = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
