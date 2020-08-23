import pygame
from empty_display import EmptyDisplay
import lib.colors as color

class PlotPixels(EmptyDisplay):
    
    def run(self):
        running = True
        while running:
            self.display.set_at((1, 1), color.white)
            self.display.set_at((10, 100), color.green)
            pygame.display.update()
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    display = PlotPixels(caption = "Search the green pixel at the coordinates (x=10, y=100)")
    display.run()

