import pygame
import threading
import time
from lib import colors as color

# In Pygame, the Sprite class helps to detect collisions between
# sprites. This is not our case (yet) because there is only a bouncing
# ball in the screen, and the limits of the screen should not be
# considered as an huge sprite with a big hole inside. However, we are
# going to use it only to know how to instantiate the class (allocate
# a sprite-ball).

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, ball_width, ball_height, initial_x_coordinate, initial_y_coordinate):
        # Compulsory.
        super().__init__()

        # Size of the sprite.
        self.image = pygame.Surface([ball_width, ball_height])

        # Color of the transparent pixels of the sprite.
        self.image.fill(color)                                  
        self.image.set_colorkey(color)

        # Initial position of the ball in the screen.
        self.x_coordinate = initial_x_coordinate
        self.y_coordinate = initial_y_coordinate

        # Draw the (squared) ball.
        pygame.draw.rect(self.image, color, [self.x_coordinate, self.y_coordinate, ball_width, ball_height])
        
        # Fetch the rectangle object that has the dimensions of the
        # image. This should return [ball_width, ball_height] (see
        # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect).
        self.ball_rectangle = self.image.get_rect()
        assert self.ball_rectangle == [ball_width, ball_height]

        # Initial direction of the ball.
        self.x_direction_step = 1 # Go to the right, one pixel
        self.y_direction_step = 1 # Go to bottom, one pixel

    # This method controls the sprite behaviour
    # (https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.update)
    # and we will use it to control were to move (blit) the ball. It
    # is called by Sprite.draw() (see below).
    def update(self):
        self.x_coordinate += self.x_direction_step
        self.y_coordinate += self.y_direction_step

# Basic initialization stuff.
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# Sound of the ball when it bounces off the walls.
self.ping_sound = pygame.mixer.Sound(file="4391__noisecollector__pongblipf-5.wav")

# Create the (sprite) ball.
# ball_height = 16
# ball_width = 16
initial_x_coordinate = screen_width/2 - ball_width/2
initial_y_coordinate = 3*screen_height/4 - ball_height/2
ball = Ball(color.white, ball_width = 16, ball_height = 16, initial_x_coordinate, initial_y_coordinate)

# All sprites of this list are drawn by a single call of Sprite.call()
# (see below).
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)

# Size of the screen.
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A bouncing squared sprite")

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

while running:
    #screen.fill(color.black)
    pygame.draw.rect(screen, color.blue, (new_x_coordinate, new_y_coordinate, rectangle_width, rectangle_height))
    pygame.display.update()
    if (self.x_coordinate + self.ball_width) > self.screen_width or self.x_coordinate < 0:
    self.x_direction = -self.x_direction
    self.ping_sound.play()
if (selfy_coordinate + self.ball_height) > self.screen_height or self.y_coordinate < 0:
    self.y_direction = -self.y_direction
    self.ping_sound.play()

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
