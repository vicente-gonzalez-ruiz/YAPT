# La pelota (un sprite) rebotando en las paredes de la ventana.

import pygame
import threading
import time
from empty_display import EmptyDisplay
import lib.colors as Color

WIDTH = 0
HEIGHT = 1
SPEED = 4

class BallPosition:
    x = 1

class Ball(pygame.sprite.Sprite):
    
    def __init__(self,
                 color,
                 width,
                 height,
                 initial_x_coordinate,
                 initial_y_coordinate,
                 display_size):

        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.display_size = display_size
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = initial_x_coordinate
        self.rect.y = initial_y_coordinate
        self.x_direction_step = SPEED # Go to the right, one pixel
        self.y_direction_step = SPEED # Go to bottom, one pixel

    def horizontal_rebound(self):
        self.x_direction_step = -self.x_direction_step

    def vertical_rebound(self):
        self.y_direction_step = -self.y_direction_step

    def ball_hits_bottom(self):
        #self.horizontal_rebound()
        self.y_direction_step = -SPEED

    def ball_hits_top(self):
        self.y_direction_step = SPEED
        #self.horizontal_rebound()

    def ball_hits_left(self):
        #self.vertical_rebound()
        self.x_direction_step = SPEED
        
    def ball_hits_right(self):
        #self.vertical_rebound()
        self.x_direction_step = -SPEED
        
    def update(self):
        display_width = self.display_size[0]
        display_height = self.display_size[1]
        self.rect.x += self.x_direction_step
        self.rect.y += self.y_direction_step
        if (self.rect.x + self.width) > display_width:
            self.ball_hits_right()
            ##self.rect.x = display_width - self.width - SPEED
        elif self.rect.x < 0:
            self.ball_hits_left()
            #self.rect.x = 0
        if (self.rect.y + self.height) > display_height:
            self.ball_hits_bottom()
            #self.rect.y = display_height - self.height - SPEED
        elif self.rect.y < 0:
            self.ball_hits_top()
            #self.rect.y = 0
        BallPosition.x = self.rect.x

class Pong_v0(EmptyDisplay):

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
            initial_y_coordinate = self.initial_y_coordinate,
            display_size = self.display_size
        )
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.ball)

        self.FPS = 0

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update_model(self):
        self.all_sprites_list.update()

    def draw_frame(self):
        self.display.fill(Color.black)
        self.all_sprites_list.draw(self.display)

    def draw(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_frame()
            self.update_model()
            pygame.display.update()
            self.process_events()
            clock.tick(60)
            self.FPS = clock.get_fps()

#    def run_model(self):
#        clock = pygame.time.Clock()
#        while self.running:
#            #self.all_sprites_list.draw(self.display)
#            self.update_model()
#            clock.tick(1000)

    def print_FPS(self):
        while self.running:
            print(f"FPS={self.FPS:04.2f}", end='\r' )
            time.sleep(1)
            
    def run(self):
        #self.draw_frame__thread = multiprocessing.Process(target = self.draw_frame)
        #self.draw_frame__thread.start()
        self.print_FPS__thread = threading.Thread(target = self.print_FPS)
        self.print_FPS__thread.start()
        #self.run_model()
        self.draw()
        #self.draw_frame__thread.join()
        self.print_FPS__thread.join()

if __name__ == "__main__":
    display = Pong_v0()
    display.run()
