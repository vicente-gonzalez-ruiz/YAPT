import pygame
from bouncing_ball import BouncingBall
from bouncing_ball_with_sound import BouncingBallSound
import lib.colors as color

# Para detectar colisiones entre objetos en Pygame tenemos que
# utilizar sprites.

class Ball(pygame.sprite.Sprite):

    def __init__(self,
                 ball_color,
                 ball_width,
                 ball_height,
                 initial_x_coordinate,
                 initial_y_coordinate):

        super().__init__()
        self.image = pygame.Surface([ball_width, ball_height])
        self.image.fill(color.black)                                  
        self.image.set_colorkey(color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, ball_color, [self.rect.x, self.rect.y, ball_width, ball_height])
        self.rect.x = initial_x_coordinate
        self.rect.y = initial_y_coordinate
        self.x_direction_step = 1 # Go to the right, one pixel
        self.y_direction_step = 1 # Go to bottom, one pixel

    def update(self):
        self.rect.x += self.x_direction_step
        self.rect.y += self.y_direction_step

class BouncingBallSprite(BouncingBallSound):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A bouncing ball of size 16x16"):

        super().__init__(width, height, caption)
        ball = Ball(self.ball_color,
                    self.ball_width,
                    self.ball_height,
                    self.initial_x_coordinate,
                    self.initial_y_coordinate)
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(ball)

    def update_frame(self):
        super().update_frame()
        self.all_sprites_list.update()
        self.all_sprites_list.draw(self.display)

if __name__ == "__main__":
    display = BouncingBallSprite()
    display.run()
