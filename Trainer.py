import pygame

class Trainer:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.speed = 1
        self.width = width
        self.height = height
        self.image = pygame.image.load('assets/images/sprite.png')
        self.color = color


    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))