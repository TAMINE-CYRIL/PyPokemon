import pygame
from Hero import Hero


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame RPG")
        self.clock = pygame.time.Clock()
        self.running = True
        self.hero = Hero(400, 300, 50, 50, (255, 255, 255))

    def run(self):
        while self.running:
            self.handle_events()
            self.movehero()
            self.draw()
            self.clock.tick(40)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def movehero(self):
        keys = pygame.key.get_pressed()
        self.hero.move(keys)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.hero.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    main = Main()
    main.run()
