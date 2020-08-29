# Anadimos puntuaciones. Cada pelota incrementa un contador cuando
# rebota en el fondo del contrario.

import pygame
from pong_v0 import SharedState
from pong_v1 import PlayerRacket
from pong_v2 import Pong_v2
from pong_v2 import CPURacket
import lib.colors as Color
from pong_v0 import Ball

WIDTH = 0
HEIGHT = 1

class ScoreBall(Ball):

    #def __init__(self,
    #             color,
    #             width,
    #             height,
    #             initial_x_coordinate,
    #             initial_y_coordinate,
    #             display_size):
        
        #super().__init__(color, width, height, initial_x_coordinate, initial_y_coordinate, display_size)
        #self.player_score = 0
        #self.CPU_score = 0

    def ball_hits_bottom(self):
        super().ball_hits_bottom()
        #self.CPU_score += 10
        SharedState.CPU_score += 10
        #self.CPU_score -= BallPosition.CPU_motion

    def ball_hits_top(self):
        super().ball_hits_top()
        SharedState.player_score += 10
        #self.player_score += 10
        #self.player_score -= BallPosition.player_motion

class PlayerRacketMotion(PlayerRacket):
    
    def update(self):
        super().update()
        SharedState.player_score -= abs(self.motion)/1000
        if SharedState.player_score < 0:
            SharedState.player_score = 0
        #self.player_score -= BallPosition.player_motion
        #print("*")

class CPURacketMotion(CPURacket):

    def update(self):
        super().update()
        SharedState.CPU_score -= abs(self.motion)/1000
        if SharedState.CPU_score < 0:
            SharedState.CPU_score = 0

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

        self.all_sprites_list.remove(self.player_racket)
        self.racket_width = 128
        self.racket_height = 2
        self.racket_color = Color.green

        self.player_racket = PlayerRacketMotion(
            color = self.racket_color,
            width = self.racket_width,
            height = self.racket_height,
            display_size = self.display_size)
        self.all_sprites_list.add(self.player_racket)

        self.all_sprites_list.remove(self.CPU_racket)
        self.CPU_racket = CPURacketMotion(
            color = self.racket_color,
            width = self.racket_width,
            height = self.racket_height,
            display_size = self.display_size)
        self.all_sprites_list.add(self.CPU_racket)
        
    def draw_frame(self):
        super().draw_frame()
        #self.ball.CPU_score -= BallPosition.CPU_motion
        #self.ball.player_score -= BallPosition.player_motion
    
        font = pygame.font.Font(None, 74)
        text = font.render(str(int(SharedState.CPU_score)), 1, Color.white)
        self.display.blit(text, (10, 10))
        text = font.render(str(int(SharedState.player_score)), 1, Color.white)
        self.display.blit(text, (10, self.display_size[1] - 50))

if __name__ == "__main__":
    display = Pong_v3()
    display.run()
