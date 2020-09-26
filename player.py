import pygame
from projectile import Projectile

class player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_helth = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
        self.rect.x += self.velocity

    def move_Left(self):
        self.rect.x -= self.velocity
