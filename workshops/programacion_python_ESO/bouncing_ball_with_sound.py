import pygame
from bouncing_ball_60Hz import BouncingBall60Hz

class BouncingBallSound(BouncingBall60Hz):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A bouncing ball of size 16x16"):

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
    display = BouncingBallSound()
    display.run()
