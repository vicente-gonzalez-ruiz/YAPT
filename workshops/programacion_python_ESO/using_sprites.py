import pygame
import threading
import time
from lib import colors as color

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, ball_width, ball_height, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Size of the screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Place where the ball appears the first time in the screen.
        initial_x_coordinate = screen_width/2 - ball_width/2
        initial_y_coordinate = 3*screen_height/4 - ball_height/2

        # Coordinates of the ball.
        self.x_coordinate = initial_x_coordinate
        self.y_coordinate = initial_y_coordinate

        # Size of the ball.
        self.ball_width = ball_width
        self.ball_height = ball_height

        # Draw the ball.
        pygame.draw.rect(self.image, color, [initial_x_coordinate, initial_y_coordinate, ball_width, ball_height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.ball_rectangle = self.image.get_rect()

        # Initial direction of the ball.
        self.x_direction = 1 # Go to right
        self.y_direction = 1 # Go to bottom

        self.ping_sound = pygame.mixer.Sound(file="4391__noisecollector__pongblipf-5.wav")

    def update(self):
        
        self.x_coordinate += self.x_direction
        if (self.x_coordinate + self.ball_width) > self.screen_width or self.x_coordinate < 0:
            self.x_direction = -self.x_direction
            self.ping_sound.play()
            
        self.y_coordinate += self.y_direction
        if (selfy_coordinate + self.ball_height) > self.screen_height or self.y_coordinate < 0:
            self.y_direction = -self.y_direction
            self.ping_sound.play()

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
all_sprites_list = pygame.sprite.Group()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A bouncing rectangle using a sprite")

rectangle_width = 100
rectangle_height = 50

clock = pygame.time.Clock()
running = True

def print_outputs():
    while running:
        FPS = clock.get_fps() # Frames Per Second
        print(f"FPS={FPS:03.2f}")
        time.sleep(1) # 1 second
    print("Goodbye")

print_outputs__thread = threading.Thread(target = print_outputs)
print_outputs__thread.start()

# Create the ball
ball = Ball(color = color.white, ball_width = 16, ball_height = 16, screen_width = screen_width, screen_height = screen_height)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)

while running:
    #screen.fill(color.black)
    pygame.draw.rect(screen, color.blue, (new_x_coordinate, new_y_coordinate, rectangle_width, rectangle_height))
    pygame.display.update()
    new_x_coordinate += x_direction
    if (new_x_coordinate + rectangle_width) > screen_width:
        x_direction = -1
        ping.play()
    elif new_x_coordinate < 0:
        x_direction = 1
        ping.play()
    new_y_coordinate += y_direction
    if (new_y_coordinate + rectangle_height) > screen_height:
        y_direction = -1
        ping.play()
    elif new_y_coordinate < 0:
        y_direction = 1
        ping.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick() # Necessary to compute the FPS value

print_outputs__thread.join() # Waits until the thread terminates
pygame.quit()
