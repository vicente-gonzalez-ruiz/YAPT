import pygame
from empty_display import EmptyDisplay
import lib.colors as color

class DrawRectangle(EmptyDisplay):

    def run(self):
        running = True
        while running:
            pygame.draw.rect(self.display, color.blue,
                             (200, 150, 100, 50))
            pygame.display.update()
            event = pygame.event.wait()  # Wait for an (input) event
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    display = DrawRectangle(caption = "Draw a blue rectangle at (200, 150, 100, 50)")
    display.run()
