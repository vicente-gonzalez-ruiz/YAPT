import pygame
from empty_display import EmptyDisplay
import lib.colors as color

class DrawRectangle(EmptyDisplay):

    def run(self):
        pygame.draw.rect(self.display, color.blue, (200, 150, 100, 50))
        pygame.display.update()
        running = True
        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    display = DrawRectangle(caption = "Draw a blue rectangle at (x=200, y=150) with size (width=100, height=50)")
    display.run()
