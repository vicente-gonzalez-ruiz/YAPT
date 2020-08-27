import pygame
import threading
import time
from bouncing_ball_FPS import BouncingBallFPS as BouncingBall
import lib.colors as color

class BouncingBallSound(BouncingBall):

    def __init__(self, width = 800, height = 600, caption = ""):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        super().__init__(width, height, caption)
        self.ping_sound = pygame.mixer.Sound(file="4391__noisecollector__pongblipf-5.wav")

    def horizontal_rebound(self):
        self.ping_sound.play()
        super().horizontal_rebound()

    def vertical_rebound(self):
        self.ping_sound.play()
        super().vertical_rebound()

if __name__ == "__main__":
    display = BouncingBallSound(caption = "A bouncing ball of size 16x16")
    display.run()
