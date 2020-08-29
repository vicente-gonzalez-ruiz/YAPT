# Una pelota rebotando contra 4 paredes. Tanto la pelota como las
# paredes son sprites.

import pygame
import threading
import time
from empty_display import EmptyDisplay
import lib.colors as Color

WIDTH = 0
HEIGHT = 1
SPEED = 8

class SharedState:
    ball_x_coor = 1
    CPU_motion = 0
    player_motion = 0
    player_score = 0
    CPU_score = 0

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

    def update(self):
        self.rect.x += self.x_direction_step
        self.rect.y += self.y_direction_step

class UpperWall(pygame.sprite.Sprite):
    
    def __init__(self, color, display_size):

        super().__init__()
        width = display_size[0] - 2
        height = 1
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = 1
        self.rect.y = 0
        pygame.draw.rect(self.image, color, [self.rect.x, self.rect.y, width, height])

class LowerWall(pygame.sprite.Sprite):
    
    def __init__(self, color, display_size):

        super().__init__()
        width = display_size[0] - 2
        height = 1
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = 1
        self.rect.y = display_size[1] - 1

class LeftWall(pygame.sprite.Sprite):
    
    def __init__(self, color, display_size):

        super().__init__()
        width = 1
        height = display_size[1] - 2
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = 0
        self.rect.y = 1

class RightWall(pygame.sprite.Sprite):
    
    def __init__(self, color, display_size):

        super().__init__()
        width = 1
        height = display_size[1] - 2
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.black)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,
                         color,
                         [self.rect.x, self.rect.y, width, height])
        self.rect.x = display_size[0] - 1
        self.rect.y = 1

class Pong_v0(EmptyDisplay):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A bouncing ball of size 16x16"):

        pygame.mixer.pre_init(44100, -16, 1, 512)
        super().__init__(width, height, caption)
        self.ping_sound = pygame.mixer.Sound(file="4391__noisecollector__pongblipf-5.wav")
        
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

        self.upper_wall = UpperWall(Color.blue, self.display_size)
        self.all_sprites_list.add(self.upper_wall)
        
        self.lower_wall = LowerWall(Color.blue, self.display_size)
        self.all_sprites_list.add(self.lower_wall)
        
        self.left_wall = LeftWall(Color.blue, self.display_size)
        self.all_sprites_list.add(self.left_wall)
        
        self.right_wall = RightWall(Color.blue, self.display_size)
        self.all_sprites_list.add(self.right_wall)
        
        self.FPS = 0

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def horizontal_rebound(self):
        self.ball.x_direction_step = -self.ball.x_direction_step
        self.ping_sound.play()
                
    def vertical_rebound(self):
        self.ball.y_direction_step = -self.ball.y_direction_step
        self.ping_sound.play()

    def update_model(self):
        self.all_sprites_list.update()
        if pygame.sprite.collide_mask(self.ball, self.upper_wall):
            self.vertical_rebound()
        if pygame.sprite.collide_mask(self.ball, self.lower_wall):
            self.vertical_rebound()
        if pygame.sprite.collide_mask(self.ball, self.right_wall):
            self.horizontal_rebound()
        if pygame.sprite.collide_mask(self.ball, self.left_wall):
            self.horizontal_rebound()

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
