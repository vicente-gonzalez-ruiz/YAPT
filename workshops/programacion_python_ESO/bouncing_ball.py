import pygame
from empty_display import EmptyDisplay
import lib.colors as Color

WIDTH = 0
HEIGHT = 1

class Ball(pygame.sprite.Sprite):

    def __init__(self,
                 color,
                 width,
                 height,
                 initial_x_coordinate,
                 initial_y_coordinate):

        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = initial_x_coordinate
        self.rect.y = initial_y_coordinate
        self.x_direction_step = 1 # Go to the right, one pixel
        self.y_direction_step = 1 # Go to bottom, one pixel

    def update(self):
        #print(self.x_direction_step)
        self.rect.x += self.x_direction_step
        self.rect.y += self.y_direction_step

class BouncingBall(EmptyDisplay):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A bouncing ball of size 16x16"):
        
        super().__init__(width, height, caption)
        self.running = True

        self.ball_width = 16
        self.ball_height = 16
        self.initial_x_coordinate = self.display_size[WIDTH]//2 - self.ball_width//2
        self.initial_y_coordinate = 3*self.display_size[HEIGHT]//4 - self.ball_height//2

        self.ball_color = Color.white

        self.ball = Ball(
            color = self.ball_color,
            width = self.ball_width,
            height = self.ball_height,
            initial_x_coordinate = self.initial_x_coordinate,
            initial_y_coordinate = self.initial_y_coordinate)
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.ball)

    def horizontal_rebound(self):
        print(self.x_direction_step)
        self.x_direction_step = -self.x_direction_step

    def vertical_rebound(self):
        self.y_direction_step = -self.y_direction_step

    def update_frame(self):
        display_width = self.display_size[WIDTH]
        display_height = self.display_size[HEIGHT]
        self.display.fill(Color.black)
        pygame.draw.rect(
            self.display,
            self.ball_color, (
                self.ball.rect.x,
                self.ball.rect.y,
                self.ball.width,
                self.ball.height))
        self.all_sprites_list.update()
        self.all_sprites_list.draw(self.display)
        pygame.display.update()

        print(self.ball.rect.x)
        self.ball.rect.x += self.x_direction_step
        if (self.ball.rect.x + self.ball.width) > display_width or self.ball.rect.x < 0:
            self.horizontal_rebound()

        self.ball.rect.y += self.y_direction_step
        if (self.ball.rect.y + self.ball.height) > display_height or self.ball.rect.y < 0:
            self.vertical_rebound()
            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def run(self):
        self.ball.rect.x = self.initial_x_coordinate
        self.ball.rect.y = self.initial_y_coordinate
        self.x_direction_step = 1  # Go to right, one pixel
        self.y_direction_step = 1  # Go to bottom, one pixel

        while self.running:
            self.update_frame()
            self.process_events()

if __name__ == "__main__":
    display = BouncingBall()
    display.run()
