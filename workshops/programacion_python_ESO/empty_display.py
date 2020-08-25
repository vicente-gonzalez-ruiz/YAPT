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
        self.running = True
        
    def __del__(self):
        print("Goodbye!")
        pygame.quit()

    def get_event(self):
        return pygame.event.wait().type

    def run(self):
        self.running = True
        while running:
            event = self.get_event()
            if event.type == pygame.QUIT:
                self.running = False

if __name__ == "__main__":
    display = EmptyDisplay()
    display.run()
