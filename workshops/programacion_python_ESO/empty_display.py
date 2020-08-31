import pygame

# Crea una ventana vacía y espera a que la cerremos.
class EmptyDisplay():

    def __init__(self,
                 width = 800,
                 height = 600,
                 caption = "Empty Screen"):
        pygame.init()
        self.display_size = (width, height)
        self.display = pygame.display.set_mode(self.display_size)
        pygame.display.set_caption(caption)
        
    def __del__(self):
        print("Goodbye!")
        pygame.quit()

    def process_events(self):
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False

    def run(self):
        running = True
        while running:
            self.process_events()

if __name__ == "__main__":
    display = EmptyDisplay()
    display.run()
