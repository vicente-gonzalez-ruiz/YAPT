import pygame
import empty_display_wait

class EmptyDisplayNoWait(EmptyDisplayWait):

    def get_event(self):
        return pygame.event.get()

if __name__ == "__main__":
    display = EmptyDisplay()
    display.run()
