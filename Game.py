import pygame
from Screen import Screen
from Trainer import Trainer




class Game:
    def __init__(self):
        self.screen = Screen()
        pygame.mixer.init()
        self.running = True
        self.trainer = Trainer(400, 300, 50, 50, (255, 255, 255))
        self.backgroundmusic = "assets/audio/background.mp3"
        self.playmusic()


    def playmusic(self):
        pygame.mixer.music.load(self.backgroundmusic)
        pygame.mixer.music.play()



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
        self.trainer.move(keys)
        self.trainer.draw(self.screen.screen)
