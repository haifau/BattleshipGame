import pygame

player_bullet_state = "ready"

class PlayerBullets:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_bullet.png")
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def fire_bullet(self, x, y):
        global player_bullet_state
        player_bullet_state = "fire"
        x += 16
        y += 30
