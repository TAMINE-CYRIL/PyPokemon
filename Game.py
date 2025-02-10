import pygame
from Screen import Screen
from Hero import Hero

class Game:
    def __init__(self):
        self.screen = Screen()
        self.running = True
        self.hero = Hero(400, 300, 50, 50, (255, 255, 255))  # Ajout du héros

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.screen.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.hero.move(keys)
        self.hero.draw(self.screen.screen)
