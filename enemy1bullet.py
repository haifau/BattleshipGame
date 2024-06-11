import pygame

class Enemy1Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("enemy_bullets.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.delta = 3
        self.current_direction = "down"


    def fire_enemy1_bullet(self, x, y):
        global enemy1_bullet_state
        enemy1_bullet_state = "fire"
        x -= 16
        y -= 30
