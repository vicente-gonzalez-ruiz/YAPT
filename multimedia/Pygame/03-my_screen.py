import pygame

class Screen:
    def __init__(self, width=800, height=600, caption=""):
        pygame.init()
        self.width = width
        self.height = height
        screen_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(caption)

    def run(self):
        running = True
        while running:
            event = pygame.event.wait().type
            if event == pygame.QUIT:
                running = False

    def __del__(self):
        pygame.quit()
        print("Goodbye!")

if __name__ == "__main__":
    screen = Screen(caption="Empty Screen")
    screen.run()
