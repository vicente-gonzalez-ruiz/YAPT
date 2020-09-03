# Añadimos las raquetas del jugador y de la CPU. El jugador usa el
# ratón y la CPU sigue la pelota.

import pygame
from Pong_v0 import Pong_v0
import lib.colors as Color
import random

CPU_DIFFICULTY = 4  # 1 es el mínimo

class PlayerRacket(pygame.sprite.Sprite):

    def __init__(self, color, width, height, display_size):

        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.display_size = display_size
        self.image = pygame.Surface([width, height])
        #self.image.fill(Color.black)                                  
        self.image.fill(color)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        #pygame.draw.rect(self.image,
        #                 color,
        #                 [self.rect.x, self.rect.y, width, height])
        self.rect.x = pygame.mouse.get_rel()[0]
        self.rect.y = self.display_size[1] - 20

    def update(self):
        self.motion = pygame.mouse.get_rel()[0]
        self.rect.x += self.motion

class CPURacket(pygame.sprite.Sprite):

    def __init__(self, color, width, height, display_size, ball):

        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.display_size = display_size
        self.image = pygame.Surface([width, height])
        self.image.fill(color)                                  
        self.image.set_colorkey(Color.black)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 20
        self.prev_ball_position = 0
        self.motion = 0
        self.ball = ball
        self.speed = 1.0

    def update(self):
        #self.motion = self.ball.rect.x - self.prev_ball_position 
        self.prev_ball_position = self.ball.rect.x
        self.rect.x = self.ball.rect.x * self.speed - self.width//2

class Pong_v1(Pong_v0):

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "A version of Pong"):
        
        super().__init__(width, height, caption)
        self.racket_sound = pygame.mixer.Sound(file="243749__unfa__metronome-1khz-weak-pulse.wav")

        self.racket_width = 128
        self.racket_height = 2
        self.racket_color = Color.green

        self.player_racket = PlayerRacket(
            color = self.racket_color,
            width = self.racket_width,
            height = self.racket_height,
            display_size = self.display_size)
        self.all_sprites_list.add(self.player_racket)

        self.CPU_racket = CPURacket(
            color = self.racket_color,
            width = self.racket_width,
            height = self.racket_height,
            display_size = self.display_size,
            ball = self.ball)
        self.all_sprites_list.add(self.CPU_racket)

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

    def compute_reflection(self):
        distance_to_the_racket_center = self.player_racket.rect.x - self.ball.rect.x + 64 - 16
        angle = distance_to_the_racket_center / 5
        angle += random.randrange(-3, 3)
        if angle > 8:
            angle = 8
        elif angle < -8:
            angle = -8
        return angle

    def update_model(self):

        super().update_model()

        if pygame.sprite.collide_mask(self.CPU_racket, self.left_wall):
            if self.CPU_racket.rect.x < 0:
                self.CPU_racket.rect.x = 1

        if pygame.sprite.collide_mask(self.CPU_racket, self.right_wall):
            if (self.CPU_racket.rect.x + 128) > self.display_size[1]:
                self.CPU_racket.rect.x = self.display_size[0] - 128

        if pygame.sprite.collide_mask(self.ball, self.CPU_racket):
            self.racket_sound.play()
            self.CPU_racket.speed = 1 + (random.random() - 0.5)/CPU_DIFFICULTY
            print(self.CPU_racket.speed)
            angle = self.compute_reflection()
            self.ball.x_direction_step = -angle
            self.ball.y_direction_step = -self.ball.y_direction_step
            

        if pygame.sprite.collide_mask(self.player_racket, self.left_wall):
            if self.player_racket.rect.x < 1:
                self.player_racket.rect.x = 1

        if pygame.sprite.collide_mask(self.player_racket, self.right_wall):
            if (self.player_racket.rect.x + 128) > self.display_size[1] - 1:
                self.player_racket.rect.x = self.display_size[0] - 128 - 1
        if pygame.sprite.collide_mask(self.ball, self.player_racket):
            self.racket_sound.play()
            angle = self.compute_reflection()
            #self.ball.vertical_rebound()
            self.ball.x_direction_step = -angle
            self.ball.y_direction_step = -self.ball.y_direction_step

if __name__ == "__main__":
    display = Pong_v1()
    try:
        display.run()
    finally:
        # Importante si por alguna razón pygame.quit() no fuera
        # llamado antes. Ver:
        # https://stackoverflow.com/questions/51901008/pygame-event-set-grab-remains-turned-on-after-exception-crash-and-makes-progra
        pygame.quit()
