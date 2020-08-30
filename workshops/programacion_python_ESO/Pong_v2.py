# Añadimos puntuaciones.

import pygame
from Pong_v1 import Pong_v1
import lib.colors as Color

class Pong_v2(Pong_v1):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A version of Pong"):
        
        super().__init__(width, height, caption)
        self.player_score = 0
        self.CPU_score = 0

    def ball_hits_upper_wall(self):
        super().ball_hits_upper_wall()
        self.player_score += 1

    def ball_hits_lower_wall(self):
        super().ball_hits_lower_wall()
        self.CPU_score += 1
        
    def draw_frame(self):
        super().draw_frame()
        #self.ball.CPU_score -= BallPosition.CPU_motion
        #self.ball.player_score -= BallPosition.player_motion
    
        font = pygame.font.Font(None, 74)
        text = font.render(str(int(self.CPU_score)), 1, Color.red)
        self.display.blit(text, (10, 20))
        text = font.render(str(int(self.player_score)), 1, Color.red)
        self.display.blit(text, (10, self.display_size[1] - 60))

if __name__ == "__main__":
    display = Pong_v2()
    display.run()
