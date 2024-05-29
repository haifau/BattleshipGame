import pygame


class PlayerBulletsNew(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_bullets.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
