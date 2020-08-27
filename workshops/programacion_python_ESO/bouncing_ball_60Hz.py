import pygame
from bouncing_ball import BouncingBall 
from bouncing_ball_FPS import BouncingBallFPS

class BouncingBall60Hz(BouncingBallFPS):

    def update_frame(self):
        BouncingBall.update_frame(self)
        self.clock.tick(60)

if __name__ == "__main__":
    display = BouncingBall60Hz()
    display.run()
