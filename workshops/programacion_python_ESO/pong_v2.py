# Añadimos la raqueta de la CPU que sigue la pelota.

import pygame
from pong_v0 import BallPosition
from pong_v1 import Pong_v1
import lib.colors as Color

WIDTH = 0
HEIGHT = 1

class CPURacket(pygame.sprite.Sprite):

    def __init__(self,
                 color,
                 width,
                 height,
                 display_size):

        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.display_size = display_size
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = 300
        self.rect.y = 20

    def update(self):
        self.rect.x = BallPosition.x - self.width//2
        #self.rect.y += self.display_size[1] - 10
        if (self.rect.x + self.width) > self.display_size[0]:
            self.rect.x = self.display_size[0] - self.width
        elif self.rect.x < 0:
            self.rect.x = 0

class Pong_v2(Pong_v1):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A version of Pong"):
        
        super().__init__(width, height, caption)

        self.racket_width = 128
        self.racket_height = 2
        self.racket_color = Color.green

        self.CPU_racket = CPURacket(
            color = self.racket_color,
            width = self.racket_width,
            height = self.racket_height,
            display_size = self.display_size)
        self.all_sprites_list.add(self.CPU_racket)

    def update_model(self):
        super().update_model()
        if pygame.sprite.collide_mask(self.ball, self.CPU_racket):         
            self.ball.vertical_rebound()

if __name__ == "__main__":
    display = Pong_v2()
    display.run()
