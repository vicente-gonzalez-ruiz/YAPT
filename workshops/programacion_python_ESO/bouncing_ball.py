import pygame
from empty_display import EmptyDisplay
import lib.colors as color

WIDTH = 0
HEIGHT = 1

class BouncingBall(EmptyDisplay):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A bouncing ball of size 16x16"):
        
        super().__init__(width, height, caption)
        self.running = True
        self.ball_width = 16
        self.ball_height = 16
        self.ball_color = color.white
        self.initial_x_coordinate = self.display_size[WIDTH]//2 - self.ball_width//2
        self.initial_y_coordinate = 3*self.display_size[HEIGHT]//4 - self.ball_height//2

    def horizontal_rebound(self):
        self.x_direction_step = -self.x_direction_step

    def vertical_rebound(self):
        self.y_direction_step = -self.y_direction_step

    def update_frame(self):
        display_width = self.display_size[WIDTH]
        display_height = self.display_size[HEIGHT]
        self.display.fill(color.black)
        pygame.draw.rect(self.display, self.ball_color, (self.x_coordinate, self.y_coordinate, self.ball_width, self.ball_height))
        pygame.display.update()

        self.x_coordinate += self.x_direction_step
        if (self.x_coordinate + self.ball_width) > display_width or self.x_coordinate < 0:
            self.horizontal_rebound()

        self.y_coordinate += self.y_direction_step
        if (self.y_coordinate + self.ball_height) > display_height or self.y_coordinate < 0:
            self.vertical_rebound()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def run(self):
        self.x_coordinate = self.initial_x_coordinate
        self.y_coordinate = self.initial_y_coordinate
        self.x_direction_step = 1  # Go to right, one pixel
        self.y_direction_step = 1  # Go to bottom, one pixel

        while self.running:
            self.update_frame()
            self.process_events()

if __name__ == "__main__":
    display = BouncingBall()
    display.run()
