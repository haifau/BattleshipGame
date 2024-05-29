import pygame


class PlayerSpaceShipNew(pygame.sprite.Sprite):

    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_spaceship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.rect.center = [x, y]
        #self.health

    def update(self):
        # speed
        speed = 5

        keys_player = pygame.key.get_pressed()
        if keys_player[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if keys_player[pygame.K_RIGHT] and self.rect.right < 0:
            self.rect.x += speed
