import pygame


class Button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("button.png")
        self.image_size = pygame.transform.scale(self.image, (300, 400))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())