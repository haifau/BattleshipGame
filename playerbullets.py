import pygame

class PlayerBullets:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_bullets.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.delta = 3
        self.current_direction = "up"

    def shoot_playerbullets(self, direction):
        if direction == "up":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    # write a piece of code that would make the bullets follow the spaceship