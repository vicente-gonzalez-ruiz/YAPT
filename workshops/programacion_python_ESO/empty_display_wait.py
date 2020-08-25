import pygame
import empty_display

class EmptyDisplayWait(EmptyDisplay):

    def get_event(self):
        return pygame.event.wait().type

    def run(self):
        self.running = True
        while running:
            event = self.get_event()
            if event == pygame.QUIT:
                running = False
            
if __name__ == "__main__":
    display = EmptyDisplay()
    display.run()
