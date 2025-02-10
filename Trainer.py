import pygame

class Trainer:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.speed = 5
        self.width = width
        self.height = height
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
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
