import pygame
from empty_display import EmptyDisplay
import lib.colors as color

WIDTH = 0
HEIGHT = 1

class BouncingBall(EmptyDisplay):

    def __init__(self, width = 800, height = 600, caption = ""):
        super().__init__(width, height, caption)
        self.running = True
    
    def do_some_extra_stuff(self):
        pass
    
    def run(self):
        ball_width = 16
        ball_height = 16

        initial_x_coordinate = self.display_size[WIDTH]//2 - ball_width//2
        initial_y_coordinate = 3*self.display_size[HEIGHT]//4 - ball_height//2
        x_coordinate = initial_x_coordinate
        y_coordinate = initial_y_coordinate
        x_direction = 1  # Go to right
        y_direction = 1  # Go to bottom

        while self.running:
            self.display.fill(color.black)
            pygame.draw.rect(self.display, color.white, (x_coordinate, y_coordinate, ball_width, ball_height))
            pygame.display.update()
            x_coordinate += x_direction
            if (x_coordinate + ball_width) > self.display_size[WIDTH]:
                x_direction = -1
            elif x_coordinate < 0:
                x_direction = 1
            y_coordinate += y_direction
            if (y_coordinate + ball_height) > self.display_size[HEIGHT]:
                y_direction = -1
            elif y_coordinate < 0:
                y_direction = 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.do_some_extra_stuff()  # Útil en clases descendientes

if __name__ == "__main__":
    display = BouncingBall(caption = "A bouncing ball of size 16x16")
    display.run()
