import pygame
import random

class SpaceRock(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("space_rock.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def reset_position(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())