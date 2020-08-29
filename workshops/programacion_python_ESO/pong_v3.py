# Anadimos puntuaciones. Cada pelota incrementa un contador cuando
# rebota en el fondo del contrario.

import pygame
from pong_v0 import BallPosition
from pong_v2 import Pong_v2
import lib.colors as Color
from pong_v0 import Ball

WIDTH = 0
HEIGHT = 1

class ScoreBall(Ball):

    def __init__(self,
                 color,
                 width,
                 height,
                 initial_x_coordinate,
                 initial_y_coordinate,
                 display_size):
        
        super().__init__(color, width, height, initial_x_coordinate, initial_y_coordinate, display_size)
        self.player_score = 0
        self.CPU_score = 0

    def ball_hits_bottom(self):
        super().ball_hits_bottom()
        self.CPU_score += 10
        self.CPU_score -= BallPosition.CPU_motion
    
    def ball_hits_top(self):
        super().ball_hits_bottom()
        self.player_score += 10
        self.player_score -= BallPosition.player_motion

class Pong_v3(Pong_v2):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A version of Pong"):
        
        super().__init__(width, height, caption)
        self.all_sprites_list.remove(self.ball)
        self.ball_width = 16
        self.ball_height = 16
        self.initial_x_coordinate = self.display_size[WIDTH]//2 - self.ball_width//2
        self.initial_y_coordinate = 3*self.display_size[HEIGHT]//4 - self.ball_height//2

        self.ball_color = Color.white

        self.ball = ScoreBall(
            color = self.ball_color,
            width = self.ball_width,
            height = self.ball_height,
            initial_x_coordinate = self.initial_x_coordinate,
            initial_y_coordinate = self.initial_y_coordinate,
            display_size = self.display_size
        )
        self.all_sprites_list.add(self.ball)
    
    def draw_frame(self):
        super().draw_frame()
        font = pygame.font.Font(None, 74)
        text = font.render(str(self.ball.CPU_score), 1, Color.white)
        self.display.blit(text, (10, 10))
        text = font.render(str(self.ball.player_score), 1, Color.white)
        self.display.blit(text, (10, self.display_size[1] - 50))

if __name__ == "__main__":
    display = Pong_v3()
    display.run()
