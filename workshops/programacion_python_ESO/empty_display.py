import pygame

class EmptyDisplay():
    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "Empty Screen"):
        pygame.init()
        display_size = (width, height)
        display = pygame.display.set_mode(display_size)
        pygame.display.set_caption(caption)

    def __del__(self):
        print("Goodbye!")
        pygame.quit()

    def run(self):
        running = True
        while running:
            event = pygame.event.wait().type
            if event == pygame.QUIT:
                running = False

if __name__ == "__main__":
    display = EmptyDisplay()
    display.run()
