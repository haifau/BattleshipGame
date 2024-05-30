import pygame

start_size = (1000, 500)
start_screen = pygame.display.set_mode(start_size)
player_health = 100
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
class PlayerSpaceShipNew(pygame.sprite.Sprite):

    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health

    def update(self):
        # speed
        speed = 5

        # movement
        keys_player = pygame.key.get_pressed()
        if keys_player[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if keys_player[pygame.K_RIGHT] and self.rect.right < 1000:
            self.rect.x += speed

        # draw health bar
        pygame.draw.rect(start_screen, RED, (self.rect.x, (self.rect)))
        pygame.draw.rect(start_screen, GREEN, (200, 400, player_health, 5))

