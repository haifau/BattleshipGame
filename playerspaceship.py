import pygame

class PlayerSpaceShip:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.delta = 5
        self.current_direction = "up"

    def move_player_ship(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())