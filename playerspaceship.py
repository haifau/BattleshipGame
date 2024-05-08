import pygame

class Player_spaceship:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_spaceship.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 200, self.image_size[1] * 100)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_balloon(self, keys_pressed):
        if keys_pressed[pygame.K_SPACE]:
            self.y -= self.delta
        else:
            self.y += self.delta

        if self.y < 0:
            self.y = 0
        elif self.y > 600 - self.image_size[1]:
            self.y = 600 - self.image_size[1]
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])