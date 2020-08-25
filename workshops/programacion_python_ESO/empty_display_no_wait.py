import pygame
from empty_display import EmptyDisplay

class EmptyDisplayNoWait(EmptyDisplay):

    def get_event(self):
        return pygame.event.get()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__ == "__main__":
    display = EmptyDisplayNoWait()
    display.run()
