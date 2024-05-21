import pygame
import random

class EnemySpaceShip1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("enemy_spaceship_1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def reset_position(self, SCREEN_WIDTH, screen_height):
        self.x = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())