import pygame
import threading
import time
from bouncing_ball import BouncingBall

class BouncingBallFPS(BouncingBall):

    def print_FPS(self):
        while self.running:
            FPS = self.clock.get_fps() # Frames Per Second
            print(f"FPS={FPS:03.2f}")
            time.sleep(1) # 1 second

    def update_frame(self):
        super().update_frame()
        self.clock.tick() # Necessary to compute the FPS value

    def run(self):
        self.clock = pygame.time.Clock()
        self.print_FPS__thread = threading.Thread(target = self.print_FPS)
        self.print_FPS__thread.start()
        super().run()
        self.print_FPS__thread.join() # Waits until the thread terminates

if __name__ == "__main__":
    display = BouncingBallFPS()
    display.run()
