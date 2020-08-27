import pygame
from bouncing_ball_sprite import BouncingBallSprite
from lib import colors as color

class Racket(pygame.sprite.Sprite):

    def __init__(self,
                 color,
                 width,
                 height,
                 initial_x_coordinate,
                 initial_y_coordinate):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color.black)                                  
        self.image.set_colorkey(color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [self.rect.x, self.rect.y, width, height])
        self.rect.x = initial_x_coordinate
        self.rect.y = initial_y_coordinate
        self.x_direction_step = 0

class BouncingBallAndStaticRacket(BouncingBallSprite):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "... Pong"):

        super().__init__(width, height, caption)
        racket = Racket(color.white,
                        64,
                        1,
                        self.initial_x_coordinate - 32,
                        self.display_size[1] - 10)
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(racket)

    def update_frame(self):
        pygame.draw.line(self.display,
                         color.green,
                         (x_coordinate_paddle, self.display_size-10), (x_coordinate_paddle+paddle_width, screen_height-10))

        super().update_frame()


if __name__ == "__main__":
    display = BouncingBallAndStaticRacket()
    display.run()


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
    x_mouse_movement = pygame.mouse.get_rel()[0]
    x_coordinate_paddle += x_mouse_movement
    if (x_coordinate_paddle + paddle_width) > screen_width:
        x_coordinate_paddle = screen_width-paddle_width
    elif x_coordinate_paddle < 0:
        x_coordinate_paddle = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
